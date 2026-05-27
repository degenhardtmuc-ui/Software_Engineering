assert ist_gerade(0) is True, f"Expected True, but ist_gerade(0) returned {ist_gerade(0)}"

assert ist_gerade(1) is False, f"Expected False, but ist_gerade(1) returned {ist_gerade(1)}"

assert ist_gerade(8) is True, f"Expected True, but ist_gerade(8) returned {ist_gerade(8)}"

  # if __name__ == '__main__':

  #check_number(read_number(1, 10), generate_number(1, 10))
  
  # Obige Zeile ist eine Kurzform fuer diese einzelne Schritte:
  #eingabe = read_number(1, 10)
  #generierung = generate_number(1, 10)
  #check_number(eingabe, generierung)

  assert ist_gerade(0) is True, f"Expected True, but ist_gerade(0) returned {ist_gerade(0)}"
  assert ist_gerade(1) is False, f"Expected False, but ist_gerade(1) returned {ist_gerade(1)}"
  assert ist_gerade(8) is True, f"Expected True, but ist_gerade(8) returned {ist_gerade(8)}"
  
  # Ruft ersten Teil von 04 Kontrollstrukturen (if) auf
  #drucke_ist_gerade(8)

  # Ruft zweiten Teil von 04 Kontrollstrukturen (if) auf
  #print_line('Hallo', 5)

# Das angesprochene Beispiel wie man eine zufaellig langen String erhaelt:
#import random
#import string
#
# Define the pool of characters (letters and digits)
#characters = string.ascii_letters + string.digits
#
# Generate a random string of length 10
# random.choices returns a list, so we "".join() it
#random_string = ''.join(random.choices(characters, k=10))
#
#print(random_string)