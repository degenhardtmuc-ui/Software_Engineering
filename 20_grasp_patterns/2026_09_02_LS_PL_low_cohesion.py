from typing import Protocol # 1. Schnittstelle definieren class Renderbar(Protocol): def render(self) -> str: ... # 2. Klassen implementieren (ohne Vererbung) class Button: def render(self) -> str: return "<button>OK</button>" class Image: def render(self) -> str: return "<img src='test.png' />" # 3. Funktion nutzen def display(item: Renderbar) -> None: print(item.render())

# 1. Schnittstelle definieren class Renderbar(Protocol): def render(self) -> str: ...

# 2. Klassen implementieren (ohne Vererbung) class Button: def render(self) -> str: return "<button>OK</button>"

class Image: def render(self) -> str: return "<img src='test.png' />"

# 3. Funktion nutzen def display(item: Renderbar) -> None: print(item.render())

item: Renderbar