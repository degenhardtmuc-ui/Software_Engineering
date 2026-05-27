woche = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]

feiertag = "Sa"

index = 0

for item in woche: 

    if item == feiertag:

        item = "Samstag"

    index = index + 1

    if(index) > len(woche):

     index = len(woche)-1

    print(index)

woche[index] = item

========

index = 0

for item in woche: 

    if item == feiertag:

        item = "Samstag"

        index = index + 1

        if(index) > len(woche):

            index = len(woche)-1

        print(index)