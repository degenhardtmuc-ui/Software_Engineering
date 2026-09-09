# ab Zeile 140 
# https://www.geeksforgeeks.org/python/python-match-case-statement/

    if account is None:
        return (
            login_message,
            "",
            "",
            "Bitte zuerst anmelden.",
            gr.update(
                value=None,
                visible=False,
            ),
            "🔒 **Nicht angemeldet**",
        )

    role = account[0]

========================================
# synonym zu:

def check_number(x):

    match x:

        case 10:

            print("It's 10")

        case 20:

            print("It's 20")

        case _:

            print("It's neither 10 nor 20")

check_number(10)

check_number(30)

case n if n < 0:

case [x, y, z]:
===============================================
# keine unnötigen Leerzeilen in der syntax
dependencies = [

    ]
