def start_v3():
    computer_nr = get_computer_nr()

    while True:
        usr_nr = get_user_nr()

        if bewerte(usr_nr, computer_nr):
            print("Du hast gewonnen!")
            break

