def count_unique_words(text: str):
    """
    Ich zaehle, wie viele verschiedene Woerter in einem Text vorkommen.

    Gross- und Kleinschreibung ist egal.
    Satzzeichen wie Komma oder Punkt zaehle ich nicht mit.
    """

    # Ich mache den ganzen Text klein.
    text = text.lower()

    # Ich teile den Text in einzelne Woerter auf.
    words = text.split()

    # Ich mache aus der Liste eine Menge.
    # Dadurch wird jedes Wort nur einmal gespeichert.
    word_set = set(words)

    # Ich ziehe die Satzzeichen direkt von meiner Menge ab.
    word_set = word_set - {",", ".", "!", "?", ";", ":"}

    # Ich gebe die Anzahl der uebrigen verschiedenen Woerter zurueck.
    return len(word_set)


dickens = "It was the best of times , it was the worst of times"

philosophy = (
    "Half a bee , philosophically , must ipso facto half not be , "
    "But can it be an entire bee , if half of it is not a bee , "
    "due to some ancient injury ."
)


print(count_unique_words(dickens))
print(count_unique_words(philosophy))