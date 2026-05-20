# Solange die Bedinung (start_value ‹ abbruch_value)erfüllt ist,
# wiederhole die Anweisungen 1 bis N
# Sorge dafür dass irgendwann die Bedingung falsch wird (Fale)
# start_value = wert
# while start_value > abbruch_value:
# Anweisung_1
# Anweisung_N
# update start_value: damit die Abbruchsbedingung True wird

start = 0
while start < 3 : # 3 < 3 => FALSE
    print("start-wert am Anfang eines Durchlaufs", start)
    print ("Guten morgne Barbara")
    print("Wie geht es Dir heute? :-) ")
    start = start + 1
    print ("start-wert Am Ende des Durchlaufs", start) 
    print("==============================") #print("==========110111011013333=="）
    
    start-wert am Anfang eines Durchlaufs 0
    Guten morgne Barbara
    Wie geht es Dir heute? :-) 
    start-wert Am Ende des Durchlaufs 1
    ==============================
    start-wert am Anfang eines Durchlaufs 1
    Guten morgne Barbara
    Wie geht es Dir heute? :-) 
    start-wert Am Ende des Durchlaufs 2
    ==============================
    start-wert am Anfang eines Durchlaufs 2
    Guten morgne Barbara
    Wie geht es Dir heute? :-) 
    start-wert Am Ende des Durchlaufs 3

# start-wert am Anfang eines neuen Durchlaufs" O
# Guten morgne Barbara
# Wie geht es Dir heute? :-)
# start-wert Am Ende des Durchlaufs 1
# ==============================
# start-wert am Anfang eines neuen Durchlaufs" 1
# Guten morgne Barbara
# Wie geht es Dir heute? :-)
# start-wert Am Ende des Durchlaufs 2