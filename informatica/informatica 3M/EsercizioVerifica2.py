Anno = int(input("Inserisci un anno: "))

if Anno < 0
and Anno < 2100:

    if Anno %= 400 == 0:
        print("anno", Anno, "è bisestile")

    if Anno %= 4 == 0
    and Anno % 100 != 0:
        print("anno", Anno, "è bisestile")

    else:
        print("anno", Anno, "non è bisestile")
    