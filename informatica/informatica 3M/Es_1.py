eta = int(input("Inserisci la tua età: "))

if eta < 12 or eta == 12:
    print("Sei Un Bambino")

    elif eta >= 13 and eta < 20:
    print("Sei Un Adolescente")


    elif eta >= 20 and eta < 65:
    print("Sei Un Adulto")


    elif eta >= 65:
    print("Sei Un Vecchio")