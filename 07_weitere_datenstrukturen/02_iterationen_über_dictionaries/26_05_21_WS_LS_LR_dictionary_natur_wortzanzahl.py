# Aufgabe:
# Wir zählen, wie oft jedes Wort im Text vorkommt.
# Dafür erstelle ich ein Dictionary.
# Das Wort ist der key.
# Die Anzahl ist der value.


text = """Die Natur schenkt dem Menschen einen stillen Rückzugsort in einer zunehmend lauten Welt.
Wenn das moderne Leben zu hektisch wird, finden wir in den Wäldern die nötige Ruhe.
Es ist faszinierend, wie viel Kraft die Natur ausstrahlt.
Jeder Mensch sehnt sich tief im Inneren nach dieser Balance, doch im Alltag geht die Zeit für das Wesentliche oft verloren.
Wir rennen durch die Welt, getrieben von Verpflichtungen, und vergessen dabei, innezuhalten.
Wer aber bewusst neue Wege geht, kann die Ruhe wiederentdecken.
Das Leben fordert viel, doch die Natur gibt uns bedingungslose Energie zurück.
Ein einzelner Mensch mag klein sein, aber seine Verbindung zur Erde ist mächtig.
Nehmen wir uns also heute die Zeit, um neue Wege zu finden.
Es braucht oft nicht viel, um die innere Mitte zu stärken.
Wenn wir der Natur wieder Raum geben, verändert sich unsere gesamte Perspektive auf die Welt.
Jede Minute im Grünen ist wertvoll investierte Zeit."""


# Der Text wird in einzelne Wörter zerlegt.
woerter = text.split()


# Diese Satzzeichen sollen entfernt werden.
satzzeichen = [".", ",", "!"]


# Leeres Dictionary für die Wortzählung
wort_zaehlung = {}


# Ich gehe jedes Wort einzeln durch.
for wort in woerter:

    # Satzzeichen aus dem Wort entfernen
    for zeichen in satzzeichen:
        wort = wort.replace(zeichen, "")

    # Das Wort wird gezählt.
    # Wenn das Wort noch nicht existiert, nimmt get(wort, 0) den Wert 0.
    # Dann wird 1 dazugezählt.
    wort_zaehlung[wort] = wort_zaehlung.get(wort, 0) + 1


# Ausgabe des fertigen Dictionarys
print(wort_zaehlung)