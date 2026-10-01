"""
PySide6 – Workshop 08
Eigene Widgets und Painting

Datei:
    session08_drawing_canvas.py

Workshop-Ziel:
- eigenes Canvas(QWidget)
- paintEvent + QPainter + update()
- Kreis / Quadrat per Mausklick platzieren
- Shape auswählen
- Shape per Drag verschieben
- Add / Move / Delete über QUndoStack rückgängig machen
- Edit-Menü mit Undo / Redo / Delete
- Stretch-Goal: Farbe über zweite ComboBox

Wichtige Architektur:

    STATE
      ↓
    paintEvent()
      ↓
    PIXEL

Maus-Handler zeichnen NICHT direkt.
Sie ändern nur den State und rufen update() auf.
"""

import sys
from dataclasses import dataclass

from PySide6.QtCore import Qt, Signal

from PySide6.QtGui import (
    QAction,
    QBrush,
    QColor,
    QKeySequence,
    QPainter,
    QPen,
    QUndoCommand,
    QUndoStack,
)

from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QLabel,
    QMainWindow,
    QWidget,
)


# ============================================================
# 1. SHAPE-DATENKLASSE
# ============================================================

@dataclass
class Shape:
    """
    Repräsentiert eine Form auf dem Canvas.

    Attributes:
        kind (str):
            "circle" oder "square"

        x (int):
            X-Koordinate des Mittelpunkts.

        y (int):
            Y-Koordinate des Mittelpunkts.

        color (str):
            Qt-Farbname, z. B. "lightblue".
    """

    kind: str
    x: int
    y: int
    color: str = "lightblue"


# ============================================================
# 2. COMMAND: SHAPE HINZUFÜGEN
# ============================================================

class AddShapeCommand(QUndoCommand):
    """Macht das Hinzufügen einer Form undoable."""

    def __init__(self, canvas, shape, index=None):
        """Speichert Canvas, Shape und Einfügeposition."""

        super().__init__("Add shape")

        self.canvas = canvas
        self.shape = shape

        if index is None:
            index = len(canvas.shapes)

        self.index = index

    def redo(self):
        """Fügt die Form ein."""

        self.canvas.insert_shape(
            self.index,
            self.shape,
        )

    def undo(self):
        """Entfernt die zuvor eingefügte Form wieder."""

        self.canvas.remove_shape(
            self.index
        )


# ============================================================
# 3. COMMAND: SHAPE LÖSCHEN
# ============================================================

class DeleteShapeCommand(QUndoCommand):
    """Macht das Löschen einer Form undoable."""

    def __init__(self, canvas, index):
        """Merkt sich Form und ursprünglichen Index."""

        shape = canvas.shapes[index]

        super().__init__("Delete shape")

        self.canvas = canvas
        self.index = index
        self.shape = shape

    def redo(self):
        """Löscht die Form."""

        self.canvas.remove_shape(
            self.index
        )

    def undo(self):
        """Stellt die Form an derselben Stelle wieder her."""

        self.canvas.insert_shape(
            self.index,
            self.shape,
        )

        self.canvas.set_selected_index(
            self.index
        )


# ============================================================
# 4. COMMAND: SHAPE VERSCHIEBEN
# ============================================================

class MoveShapeCommand(QUndoCommand):
    """
    Macht eine Drag-Bewegung rückgängig.

    old_position und new_position sind Tupel:
        (x, y)
    """

    def __init__(
        self,
        canvas,
        index,
        old_position,
        new_position,
    ):
        """Speichert Formindex sowie alte und neue Position."""

        super().__init__("Move shape")

        self.canvas = canvas
        self.index = index
        self.old_position = old_position
        self.new_position = new_position

    def redo(self):
        """Wendet die neue Position an."""

        x, y = self.new_position

        self.canvas.set_shape_position(
            self.index,
            x,
            y,
        )

    def undo(self):
        """Stellt die alte Position wieder her."""

        x, y = self.old_position

        self.canvas.set_shape_position(
            self.index,
            x,
            y,
        )


# ============================================================
# 5. CUSTOM WIDGET: CANVAS
# ============================================================

class Canvas(QWidget):
    """
    Benutzerdefinierte Zeichenfläche.

    State:
        self.shapes
        self.selected_index
        self.drag_index
        self.current_kind
        self.current_color

    Darstellung:
        ausschließlich in paintEvent()

    Interaktion:
        mousePressEvent()
        mouseMoveEvent()
        mouseReleaseEvent()
    """

    shape_selected = Signal(int)

    SHAPE_SIZE = 30
    HALF_SIZE = SHAPE_SIZE // 2
    SELECTION_PADDING = 4

    def __init__(self, undo_stack, parent=None):
        """Initialisiert State und Mindestgröße des Canvas."""

        super().__init__(parent)

        self.undo_stack = undo_stack

        self.setMinimumSize(
            500,
            350,
        )

        self.shapes = []

        self.selected_index = None

        self.drag_index = None
        self.drag_start = None

        self.current_kind = "circle"
        self.current_color = "lightblue"


    # ========================================================
    # 6. TOOLBAR-EINSTELLUNGEN
    # ========================================================

    def set_shape_kind(self, text):
        """Setzt den Shape-Typ für neue Formen."""

        self.current_kind = text.lower()

    def set_shape_color(self, text):
        """Setzt die Farbe für neue Formen."""

        self.current_color = text


    # ========================================================
    # 7. AUSWAHL
    # ========================================================

    def set_selected_index(self, index):
        """
        Setzt die aktuelle Auswahl.

        Args:
            index:
                int oder None.
        """

        if index is not None:

            if not 0 <= index < len(self.shapes):
                index = None

        self.selected_index = index

        self.shape_selected.emit(
            index if index is not None else -1
        )

        self.update()


    # ========================================================
    # 8. LOW-LEVEL-MUTATIONEN
    # ========================================================

    def insert_shape(self, index, shape):
        """
        Fügt eine Shape an einem bestimmten Index ein.

        Diese Methode zeichnet nicht direkt.
        Sie verändert State + update().
        """

        if not 0 <= index <= len(self.shapes):
            return False

        if (
            self.selected_index is not None
            and self.selected_index >= index
        ):
            self.selected_index += 1

        if (
            self.drag_index is not None
            and self.drag_index >= index
        ):
            self.drag_index += 1

        self.shapes.insert(
            index,
            shape,
        )

        self.update()

        return True

    def remove_shape(self, index):
        """
        Entfernt eine Shape.

        Löschen während eines Drags wird abgesichert.
        """

        if not 0 <= index < len(self.shapes):
            return None

        shape = self.shapes.pop(
            index
        )

        if self.selected_index == index:

            self.selected_index = None

            self.shape_selected.emit(
                -1
            )

        elif (
            self.selected_index is not None
            and self.selected_index > index
        ):

            self.selected_index -= 1

        if self.drag_index == index:

            self.drag_index = None
            self.drag_start = None

        elif (
            self.drag_index is not None
            and self.drag_index > index
        ):

            self.drag_index -= 1

        self.update()

        return shape

    def set_shape_position(
        self,
        index,
        x,
        y,
    ):
        """
        Verschiebt eine Shape auf eine neue Position.

        Wird von MoveShapeCommand.redo()/undo() benutzt.
        """

        if not 0 <= index < len(self.shapes):
            return False

        shape = self.shapes[
            index
        ]

        shape.x = int(x)
        shape.y = int(y)

        self.update()

        return True


    # ========================================================
    # 9. DELETE-AKTION
    # ========================================================

    def delete_selected(self):
        """Löscht die ausgewählte Shape über einen Command."""

        if self.selected_index is None:
            return

        if not 0 <= self.selected_index < len(self.shapes):

            self.set_selected_index(
                None
            )

            return

        command = DeleteShapeCommand(
            self,
            self.selected_index,
        )

        self.undo_stack.push(
            command
        )


    # ========================================================
    # 10. HIT-TEST
    # ========================================================

    def shape_at(self, x, y):
        """
        Liefert den Index der obersten Shape unter (x, y).

        Wichtig:
        Wir iterieren rückwärts, weil später gezeichnete Shapes
        visuell oben liegen.
        """

        for index in range(
            len(self.shapes) - 1,
            -1,
            -1,
        ):

            shape = self.shapes[
                index
            ]

            dx = x - shape.x
            dy = y - shape.y

            if shape.kind == "circle":

                if (
                    dx * dx + dy * dy
                    <= self.HALF_SIZE * self.HALF_SIZE
                ):
                    return index

            elif shape.kind == "square":

                if (
                    abs(dx) <= self.HALF_SIZE
                    and abs(dy) <= self.HALF_SIZE
                ):
                    return index

        return None


    # ========================================================
    # 11. PAINT EVENT
    # ========================================================

    def paintEvent(self, event):
        """
        Zeichnet den AKTUELLEN STATE.

        Es wird niemals in einem Mouse-Handler direkt gezeichnet.
        """

        painter = QPainter(
            self
        )

        painter.setRenderHint(
            QPainter.RenderHint.Antialiasing,
            True,
        )

        painter.fillRect(
            self.rect(),
            QColor("white"),
        )

        for index, shape in enumerate(
            self.shapes
        ):

            normal_pen = QPen(
                QColor("navy")
            )

            normal_pen.setWidth(
                2
            )

            painter.setPen(
                normal_pen
            )

            painter.setBrush(
                QBrush(
                    QColor(shape.color)
                )
            )

            left = (
                shape.x
                - self.HALF_SIZE
            )

            top = (
                shape.y
                - self.HALF_SIZE
            )

            if shape.kind == "circle":

                painter.drawEllipse(
                    left,
                    top,
                    self.SHAPE_SIZE,
                    self.SHAPE_SIZE,
                )

            elif shape.kind == "square":

                painter.drawRect(
                    left,
                    top,
                    self.SHAPE_SIZE,
                    self.SHAPE_SIZE,
                )

            if index == self.selected_index:

                selection_pen = QPen(
                    QColor("black")
                )

                selection_pen.setWidth(
                    2
                )

                selection_pen.setStyle(
                    Qt.PenStyle.DashLine
                )

                painter.setPen(
                    selection_pen
                )

                painter.setBrush(
                    QBrush(
                        Qt.BrushStyle.NoBrush
                    )
                )

                padding = (
                    self.SELECTION_PADDING
                )

                painter.drawRect(
                    left - padding,
                    top - padding,
                    self.SHAPE_SIZE + 2 * padding,
                    self.SHAPE_SIZE + 2 * padding,
                )

        painter.end()


    # ========================================================
    # 12. MOUSE PRESS
    # ========================================================

    def mousePressEvent(self, event):
        """
        Linksklick:

        Auf Shape:
            auswählen und Drag vorbereiten.

        Auf leere Fläche:
            bestehende Auswahl aufheben und neue Shape als
            AddShapeCommand platzieren.
        """

        if (
            event.button()
            != Qt.MouseButton.LeftButton
        ):

            super().mousePressEvent(
                event
            )

            return

        position = (
            event.position()
        )

        x = int(
            position.x()
        )

        y = int(
            position.y()
        )

        index = self.shape_at(
            x,
            y,
        )

        if index is not None:

            self.set_selected_index(
                index
            )

            self.drag_index = index

            shape = self.shapes[
                index
            ]

            self.drag_start = (
                shape.x,
                shape.y,
            )

            event.accept()

            return

        self.set_selected_index(
            None
        )

        self.drag_index = None
        self.drag_start = None

        shape = Shape(
            kind=self.current_kind,
            x=x,
            y=y,
            color=self.current_color,
        )

        command = AddShapeCommand(
            self,
            shape,
        )

        self.undo_stack.push(
            command
        )

        event.accept()


    # ========================================================
    # 13. MOUSE MOVE
    # ========================================================

    def mouseMoveEvent(self, event):
        """
        Verschiebt die Shape während des Drags live.

        Das ist nur die visuelle Vorschau.
        Der eigentliche Undo-Command wird erst beim Loslassen
        auf den Stack gelegt.
        """

        if self.drag_index is None:

            super().mouseMoveEvent(
                event
            )

            return

        if not 0 <= self.drag_index < len(self.shapes):

            self.drag_index = None
            self.drag_start = None

            return

        position = event.position()

        x = int(
            position.x()
        )

        y = int(
            position.y()
        )

        shape = self.shapes[
            self.drag_index
        ]

        shape.x = x
        shape.y = y

        self.update()

        event.accept()


    # ========================================================
    # 14. MOUSE RELEASE
    # ========================================================

    def mouseReleaseEvent(self, event):
        """Beim Loslassen wird aus dem Drag eine Undoable-Aktion."""

        if (
            event.button()
            != Qt.MouseButton.LeftButton
        ):

            super().mouseReleaseEvent(
                event
            )

            return

        if (
            self.drag_index is None
            or self.drag_start is None
        ):

            super().mouseReleaseEvent(
                event
            )

            return

        index = self.drag_index

        if not 0 <= index < len(self.shapes):

            self.drag_index = None
            self.drag_start = None

            return

        old_position = (
            self.drag_start
        )

        shape = self.shapes[
            index
        ]

        new_position = (
            shape.x,
            shape.y,
        )

        self.drag_index = None
        self.drag_start = None

        if new_position != old_position:

            command = MoveShapeCommand(
                self,
                index,
                old_position,
                new_position,
            )

            self.undo_stack.push(
                command
            )

        event.accept()


# ============================================================
# 15. HAUPTFENSTER
# ============================================================

class DrawingWindow(QMainWindow):
    """
    Hauptfenster des Drawing Canvas.

    Enthält:
    - Canvas als Central Widget
    - Toolbar für Shape und Farbe
    - Edit-Menü für Undo / Redo / Delete
    """

    def __init__(self):
        """Erstellt Undo-Stack, Canvas, Toolbar und Edit-Menü."""

        super().__init__()

        self.setWindowTitle(
            "Drawing Canvas"
        )

        self.resize(
            760,
            520,
        )

        self.undo_stack = QUndoStack(
            self
        )

        self.canvas = Canvas(
            self.undo_stack
        )

        self.setCentralWidget(
            self.canvas
        )


        # ====================================================
        # 16. TOOLBAR: SHAPE
        # ====================================================

        toolbar = self.addToolBar(
            "Drawing"
        )

        toolbar.addWidget(
            QLabel("Shape:")
        )

        self.shape_combo = QComboBox()

        self.shape_combo.addItems(
            [
                "Circle",
                "Square",
            ]
        )

        toolbar.addWidget(
            self.shape_combo
        )

        self.shape_combo.currentTextChanged.connect(
            self.canvas.set_shape_kind
        )


        # ====================================================
        # 17. STRETCH-GOAL: FARBE
        # ====================================================

        toolbar.addSeparator()

        toolbar.addWidget(
            QLabel("Color:")
        )

        self.color_combo = QComboBox()

        self.color_combo.addItems(
            [
                "lightblue",
                "lightgreen",
                "tomato",
                "gold",
            ]
        )

        toolbar.addWidget(
            self.color_combo
        )

        self.color_combo.currentTextChanged.connect(
            self.canvas.set_shape_color
        )


        # ====================================================
        # 18. EDIT-MENÜ
        # ====================================================

        edit_menu = self.menuBar().addMenu(
            "&Edit"
        )

        self.undo_action = (
            self.undo_stack.createUndoAction(
                self,
                "&Undo",
            )
        )

        self.undo_action.setShortcut(
            QKeySequence.StandardKey.Undo
        )

        self.redo_action = (
            self.undo_stack.createRedoAction(
                self,
                "&Redo",
            )
        )

        self.redo_action.setShortcut(
            QKeySequence.StandardKey.Redo
        )

        self.delete_action = QAction(
            "&Delete",
            self,
        )

        self.delete_action.setShortcut(
            QKeySequence("Delete")
        )

        self.delete_action.setEnabled(
            False
        )

        self.delete_action.triggered.connect(
            self.canvas.delete_selected
        )

        edit_menu.addAction(
            self.undo_action
        )

        edit_menu.addAction(
            self.redo_action
        )

        edit_menu.addSeparator()

        edit_menu.addAction(
            self.delete_action
        )


        # ====================================================
        # 19. AUSWAHL-SIGNAL
        # ====================================================

        self.canvas.shape_selected.connect(
            self.on_shape_selected
        )

        self.statusBar().showMessage(
            "Click empty space to add. "
            "Click a shape to select. "
            "Drag to move."
        )


    # ========================================================
    # 20. DELETE-ACTION
    # ========================================================

    def on_shape_selected(self, index):
        """Aktiviert Delete nur bei gültiger Auswahl."""

        self.delete_action.setEnabled(
            index >= 0
        )


# ============================================================
# 21. PROGRAMMSTART
# ============================================================

def main():
    """Startet die PySide6-Anwendung."""

    app = QApplication(
        sys.argv
    )

    window = DrawingWindow()

    window.show()

    return app.exec()


if __name__ == "__main__":

    sys.exit(
        main()
    )