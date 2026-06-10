"""
1. Mehrere Funktionen rufen sich gegenseitig auf.
2. Ganz unten in fN() wird absichtlich ein Fehler ausgelöst.
3. f3() hat ein try / except und fängt den Fehler zuerst ab.
4. f1() hat zwar auch ein try / except, aber f1() bekommt den Fehler nicht mehr,
   weil f3() ihn schon behandelt hat.
Kette:
f1() -> f2() -> f3() -> f4() -> fN()
"""


def f1():
    """
    f1() ist der Startpunkt der Kette.

    f1() hat auch einen try/except-Block.
    Aber: Dieser except-Block wird nur benutzt, wenn der Fehler nicht schon
    weiter unten, zum Beispiel in f3(), abgefangen wurde.
    """
    print("in f1() call f2()")

    try:
        # f1() ruft f2() auf.
        # Wenn in f2() oder tiefer ein Fehler passiert und NICHT abgefangen wird,
        # dann würde der Fehler hier im except von f1() landen.
        f2()

        # Diese Zeilen laufen nur, wenn f2() am Ende normal zurückkommt.
        print("f2() erfolgreich ausgeführt")
        print("Also weiter machen mit f1()")

    except Exception as e:
        # Dieser Block wird in diesem Beispiel NICHT ausgeführt,
        # weil f3() den Fehler schon vorher abfängt.
        print("Exception wurde in f1() behandelt")
        print("Fehlermeldung:", e)

    print("Fertig mit f1()")


def f2():
    """
    f2() ist eine Zwischenstation.

    f2() hat KEIN try/except.
    Wenn ein Fehler aus f3() hochkommt, würde f2() ihn einfach weitergeben.
    In diesem Beispiel kommt aber kein Fehler mehr bei f2() an,
    weil f3() den Fehler schon behandelt.
    """
    print("in f2() call f3()")

    # f2() ruft f3() auf.
    f3()

    # Diese Zeilen werden ausgeführt, weil f3() den Fehler abfängt
    # und danach normal zu f2() zurückkommt.
    print("weiter machen mit f2()")
    print("Fertig mit f2()")


def f3():
    """
    f3() ist in diesem Beispiel der wichtigste Punkt.

    f3() hat einen try/except-Block.
    Das bedeutet:
    Wenn in f4() oder in fN() ein Fehler passiert, kann f3() ihn abfangen.
    """
    try:
        print("in f3() call f4()")

        # f3() ruft f4() auf.
        # In f4() wird später fN() aufgerufen.
        # Dort entsteht der Fehler.
        f4()

        # Diese Zeilen werden NICHT ausgeführt,
        # weil f4() wegen des Fehlers nicht normal zurückkommt.
        print("weiter machen mit f3()")
        print("Fertig mit f3() im try")

    except Exception as e:
        # Hier landet der Fehler aus fN().
        # f3() ist näher am Fehler als f1(), deshalb fängt f3() ihn zuerst ab.
        print("Exception wurde in f3() behandelt")
        print("Fehlermeldung:", e)

    # Nach dem except geht es hier weiter.
    print("Fertig mit f3()")


def f4():
    """
    f4() ruft fN() auf.

    f4() hat KEIN try/except.
    Wenn fN() einen Fehler wirft, kann f4() den Fehler nicht behandeln.
    Der Fehler geht dann zurück nach f3().
    """
    print("in f4() call fN()")

    # fN() löst absichtlich einen Fehler aus.
    fN()

    # Diese Zeilen werden NICHT ausgeführt,
    # weil fN() vorher mit raise einen Fehler wirft.
    print("fN() erfolgreich ausgeführt")
    print("Also weiter machen mit f4()")
    print("Fertig mit f4()")


def fN():
    """
    fN() ist die tiefste Funktion.

    Hier wird absichtlich ein ValueError ausgelöst.
    raise bedeutet: Wir werfen einen Fehler.
    """
    raise ValueError("Raising ValueError")

    # Diese Zeile wird NIE ausgeführt,
    # weil nach raise der normale Ablauf sofort stoppt.
    print("code nach ValueError in fN()")


# Programm starten:
# Erst durch diesen Aufruf beginnt die Kette wirklich zu laufen.
f1()

===============================================================================
# Except ist bei f3() und f1()

# Wenn mehrere try / except-Blöcke existieren, fängt der erste passende except den Fehler ab, den Python auf dem Rückweg findet.



# Fehler entsteht in fN()
# f3 fängt ihn ab
# f1 bekommt den Fehler gar nicht mehr
# f3() ist näher am Fehler als f1(). Deshalb behandelt f3() den Fehler zuerst. 
# Danach läuft das Programm normal weiter.



def f1():
    try:
        print("in f1() call f2()")
        f2()
        print("f2() erfolgreich ausgeführt")
        print("Fertig mit f1()")
    except Exception:
        print("Exception wurde in f1() behandelt")


def f2():
    print("in f2() call f3()")
    f3()
    print("weiter machen mit f2()")
    print("Fertig mit f2()")


def f3():
    try:
        print("in f3() call f4()")
        f4()
        print("weiter machen mit f3()")
        print("Fertig mit f3()")
    except Exception:
        print("Exception wurde in f3() behandelt")
    else:
        print("kein Fehler in f3() passiert") # läuft nur weiter, wenn kein Fehler passiert
    finally:
        print("will always run") # wird immer ausgeführt, egal ob Fehler oder kein Fehler

def f4():
    print("in f4() call fN()")
    fN()
    print("weiter machen mit f4()")


def fN():
    raise ValueError("Raising ValueError")


f1()

# Der erste passende except-Block auf dem Rückweg fängt den Fehler.
# fN macht Fehler
# f4 gibt weiter
# f3 fängt ab
# f2 läuft weiter
# f1 läuft weiter

# Obwohl f1() auch ein try/except hat, wird der Fehler nicht dort behandelt, weil f3() näher am Fehler ist und ihn zuerst abfängt!