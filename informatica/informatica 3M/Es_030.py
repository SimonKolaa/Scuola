import random

def genera_cartella(id):
    cartella = {}
    numeri = random.sample(range(1, 91), 15)
    for i in range(3):
        cartella[f"colonna_{i+1}"] = numeri[i*5:i*5+5]
    return {id: cartella}

def estrai_numero(numeri_estratti):
    numero = random.choice([x for x in range(1, 91) if x not in numeri_estratti])
    numeri_estratti.append(numero)
    return numero
def controlla_cartella(cartella, numeri_estratti):
    risultati = [False] * 5
    for i in range(3):
        
        for i in range(5):
            if all(num in numeri_estratti for num in cartella[f"colonna_{i+1}"]):
                risultati[i] = True
    return risultati

cartelle = [genera_cartella("cartella1"), genera_cartella("cartella2")]
numeri_estratti = []
while True:
    input("Premi Invio per estrarre un numero")
    nuovo_numero = estrai_numero(numeri_estratti)
    print(f"È stato estratto il numero {nuovo_numero}")
    for cartella in cartelle:
        print(controlla_cartella(cartella, numeri_estratti))