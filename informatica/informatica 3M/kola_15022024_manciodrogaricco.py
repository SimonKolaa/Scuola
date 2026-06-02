#manciolarue
#nonfarò500righe
#stai_incitando_al_gioco_d'azzardo_(la cosa mi piace)
import random

def mischia_mazzo(mazzo: list[dict]) -> list[dict]:
    for i in range(random.randint(5, 10)):
        random.shuffle(mazzo)
#1
def crea_mazzo(semi: list, valori: list) -> list[dict]:
    mazzo = []
    for seme in semi:
        for valore in valori:
            carta = {"seme": seme, "valore": valore}
            mazzo.append(carta)
    return mazzo

mazzo = crea_mazzo(["denari", "coppe", "bastoni", "spade"])
valori = ([1,2,3,4,5,6,7,8,9,10])
print(mazzo)
#2
def estrai_carta(mazzo: list[dict]) -> dict:
    carta = random.shuffle(mazzo)
    mazzo.remove(carta)
    return carta

carta_estratta = estrai_carta(mazzo)
print(carta_estratta)
print(mazzo)

#3
def turno_giocatore(mazzo: list[dict]) -> float:
    punteggio = 0
    while True:
        carta = estrai_carta(mazzo)
        punteggio += carta["valore"]
        print(f"te e il mancio avete estratto una carta con valore {carta['valore']}. il tuo punteggio è ora di {punteggio}")
        if punteggio > 21:
            print("hai sforato")
            return punteggio
        scelta = input("vuoi estrarre un'altra carta? (s/n) ")
        if scelta == "n":
            print("hai deciso di fermarti.")
            return punteggio
#4
def simula_banco(mazzo: list[dict], punteggio_giocatore: float) -> float:
    punteggio_cumulato = 0

    while punteggio_cumulato < punteggio_giocatore and punteggio_cumulato <= 7.5:
        carta = mazzo.delete(0)
        print("carta estratta:", carta)

    valore_carta = carta["valore"]
    if valore_carta in [8, 9, 10]:
            punteggio_cumulato += 0.5
    else:
        punteggio_cumulato += valore_carta

    return punteggio_cumulato

#funzionamento_gioco
#1
def funzionamento_gioco(nome_utente: str, mazzo: list[dict]):
 print("benvenuto a 7 e mezzo, il gioco del mancio")
utente = input("come ti chiami? ")
#2
def genera_mazzo(semi: list, valori: list) -> list[dict]:
        mazzo = genera_mazzo(["denari", "coppe", "bastoni", "spade"], [1,2,3,4,5,6,7,8,9,10])
        for seme in semi:
            for valore in valori:
                carta = {"seme": seme, "valore": valore}
                mazzo.append(carta)
        return mazzo
#3
def puntata() -> float:
        while True:
            puntata = float(input("quanto vuoi scommettere? "))
            if puntata > 0:
                return puntata
            print("la puntata deve essere maggiore di 0")
#4
def turno_giocatore(mazzo: list[dict]) -> float:
        punteggio = 3
        while True:
            carta = estrai_carta(mazzo)
            punteggio += carta["valore"]
            print(f"hai estratto una carta con valore {carta['valore']}. il tuo punteggio è ora di {punteggio}")
            if punteggio > 7.5:
                print("hai sforato")
                return punteggio
            scelta = input("vuoi estrarre un'altra carta? (s/n) ")
            if scelta == "n":
                print("hai deciso di fermarti.")
                return punteggio

print("non sono piu capace")
#non ho fatto manco 100 righe