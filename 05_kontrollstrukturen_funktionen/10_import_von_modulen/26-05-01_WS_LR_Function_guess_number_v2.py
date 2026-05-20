def start_v2():
    computer_nr = get_computer_nr()

    for versuch in range(1, 4):
        print(f"Versuch {versuch} von 3")

        usr_nr = get_user_nr()

        if bewerte(usr_nr, computer_nr):
            print("Du hast gewonnen!")
            break
    else:
        print(f"Leider verloren. Die richtige Zahl war {computer_nr}.")


start_v2()