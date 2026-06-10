from typing import Callable


def raise_and_handle_error(exception_type: Callable):
    # Diese Funktion bekommt einen Fehlertyp übergeben.
    # Zum Beispiel: IndexError, ValueError oder LookupError.

    print("      raise_and_handle_error(): before try")
    # Diese Ausgabe zeigt: Wir sind in der Funktion angekommen,
    # aber der try-Block hat noch nicht angefangen.

    try:
        # Ab hier probiert Python den Code aus.
        # Wenn hier ein Fehler passiert, sucht Python unten nach einem passenden except.

        print("      raise_and_handle_error(): before raise")
        # Diese Ausgabe kommt direkt bevor der Fehler absichtlich erzeugt wird.

        raise exception_type(f"Raising {exception_type.__name__}")
        # Hier wird absichtlich ein Fehler erzeugt.
        # exception_type ist der Fehlertyp, den wir vorher übergeben haben.
        # Wenn wir zum Beispiel IndexError übergeben,
        # wird hier ein IndexError erzeugt.
        #
        # f"..." ist ein f-String.
        # Damit kann man Werte direkt in einen Text einsetzen.
        #
        # exception_type.__name__ gibt den Namen des Fehlertyps als Text zurück.
        # Bei IndexError ist das also "IndexError".
        #
        # Das Ergebnis ist dann ungefähr:
        # raise IndexError("Raising IndexError")

    except LookupError as error:
        # Dieser Block fängt Fehler aus der LookupError-Familie.
        # Wichtig:
        # IndexError gehört auch zur LookupError-Familie.
        # Deshalb wird ein IndexError hier zuerst gefangen.

        print(f"<<< raise_and_handle_error(): caught LookupError [{error}]")
        # Hier wird ausgegeben, dass ein LookupError gefangen wurde.
        # In [error] steht die Fehlermeldung.

        raise
        # raise alleine bedeutet:
        # Wir werfen denselben Fehler nochmal weiter.
        # Der Fehler wird also nicht hier beendet,
        # sondern an die nächste Funktion weitergegeben.

    except ValueError as error:
        # Dieser Block fängt einen ValueError.
        # Ein ValueError ist ein Fehler bei einem falschen Wert.

        print(f"<<< raise_and_handle_error(): caught ValueError [{error}]")
        # Hier wird ausgegeben, dass ein ValueError gefangen wurde.
        # Dieser Fehler wird hier NICHT weitergeworfen.
        # Deshalb ist er hier erledigt.

    print("      raise_and_handle_error(): after except")
    # Diese Zeile kommt nur, wenn der Fehler in dieser Funktion wirklich beendet wurde.
    # Bei ValueError passiert das.
    # Bei IndexError passiert das nicht, weil der Fehler mit raise weitergeworfen wird.


def intermediate_fun(exception_type: Callable):
    # Diese Funktion ist die mittlere Station.
    # Sie ruft raise_and_handle_error() auf.

    print("   intermediate_fun(): before try")
    # Ausgabe: Wir sind in intermediate_fun angekommen.

    try:
        # Python probiert jetzt den folgenden Code aus.

        print("   intermediate_fun(): before calling")
        # Ausgabe direkt bevor die innere Funktion aufgerufen wird.

        raise_and_handle_error(exception_type)
        # Hier wird die innere Funktion aufgerufen.
        # Der Fehlertyp wird weitergegeben.
        # Beispiel:
        # Wenn exception_type IndexError ist,
        # dann bekommt raise_and_handle_error auch IndexError.

        print("   intermediate_fun(): after calling")
        # Diese Zeile kommt nur, wenn der Funktionsaufruf ohne weitergeworfenen Fehler endet.
        # Bei IndexError kommt diese Zeile NICHT,
        # weil der Fehler vorher weitergeworfen wurde.

    except IndexError as error:
        # Dieser Block fängt speziell einen IndexError.
        # Das passiert bei unserem Test mit IndexError.

        print(f"<<< intermediate_fun(): caught IndexError [{error}]")
        # Ausgabe: intermediate_fun hat den IndexError gefangen.

        raise TypeError(f"Raising inner TypeError from [{error}]") from error
        # Hier wird ein neuer Fehler erzeugt: TypeError.
        #
        # Das bedeutet:
        # Aus dem alten IndexError wird jetzt ein neuer TypeError.
        #
        # from error bedeutet:
        # Der alte Fehler ist die Ursache für den neuen Fehler.
        #
        # Ganz einfach:
        # Python merkt sich:
        # Erst gab es IndexError.
        # Danach wurde daraus TypeError.

    except LookupError as error:
        # Dieser Block würde andere LookupError-Fehler fangen.
        # Zum Beispiel KeyError.
        #
        # Aber Achtung:
        # IndexError wird schon vorher im except IndexError gefangen.
        # Deshalb kommt IndexError nicht hier rein.

        print(f"<<< intermediate_fun(): caught LookupError [{error}]")
        # Ausgabe: Ein LookupError wurde gefangen.

        raise TypeError("Raising inner TypeError")
        # Hier wird auch ein neuer TypeError geworfen.
        # Aber ohne from error.
        # Das heißt: Die Ursache wird nicht so sauber verbunden wie oben.

    except Exception as error:
        # Exception ist sehr allgemein.
        # Dieser Block fängt fast alle normalen Fehler,
        # die oben noch nicht gefangen wurden.

        print(f"<<< intermediate_fun(): caught Exception [{error}]")
        # Ausgabe: Ein allgemeiner Fehler wurde gefangen.

        print("   intermediate_fun(): re-raising exception")
        # Ausgabe: Wir sagen, dass der Fehler gleich weitergeworfen wird.

        raise
        # Derselbe Fehler wird weitergeworfen.
        # Er wird also nicht hier beendet.

    print("   intermediate_fun(): after except")
    # Diese Zeile kommt nur, wenn intermediate_fun den Fehler wirklich erledigt hat.
    # Bei IndexError kommt diese Zeile nicht,
    # weil daraus ein TypeError gemacht und weitergeworfen wird.


def outer_caller_with_try(error_type: Callable = ValueError):
    # Diese Funktion ist außen.
    # Sie startet den ganzen Ablauf.
    #
    # error_type: Callable = ValueError bedeutet:
    # Wenn nichts angegeben wird, nimmt Python automatisch ValueError.

    print("outer_caller(): before try")
    # Ausgabe: Wir sind in outer_caller angekommen.

    try:
        # Python probiert jetzt den folgenden Code.

        print("outer_caller(): before calling")
        # Ausgabe direkt bevor intermediate_fun aufgerufen wird.

        intermediate_fun(error_type)
        # Hier wird die mittlere Funktion aufgerufen.
        # Der Fehlertyp wird weitergegeben.

        print("outer_caller(): after calling")
        # Diese Zeile kommt nur, wenn intermediate_fun ohne Fehler zurückkommt.
        # Bei IndexError kommt diese Zeile nicht,
        # weil am Ende ein TypeError außen ankommt.

    except Exception as error:
        # Dieser Block fängt alle normalen Fehler,
        # die von innen bis hier nach außen kommen.

        print(f"<<< outer_caller(): caught Exception: {error}")
        # Hier wird der Fehler außen gefangen und ausgegeben.
        # Danach ist der Fehler behandelt.
        # Das Programm stürzt deshalb nicht ab.

    print("outer_caller(): after except")
    # Diese Zeile kommt am Ende.
    # Sie zeigt:
    # outer_caller ist fertig.


outer_caller_with_try(IndexError)
# Hier startet das Programm.
# Wir übergeben IndexError.
# Das bedeutet:
# Innen wird absichtlich ein IndexError erzeugt.

===================================================================