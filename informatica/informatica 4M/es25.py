class Prenotazione:
    def __init__(self, nome, data, ora, numero_persone, stato):
        self.nome = nome
        self.data = data
        self.ora = ora
        self.numero_persone = numero_persone
        self.stato = stato

    def __str__(self):
        return f"{self.nome} - {self.data} - {self.ora} - {self.numero_persone} - {self.stato}"


def aggiungi_prenotazione():
    nome = input("Nome: ")
    data = input("Data: ")
    ora = input("Ora: ")
    numero_persone = int(input("Numero persone: "))
    stato = input("Stato: ")
    prenotazione = Prenotazione(nome, data, ora, numero_persone, stato)
    return prenotazione

def cerca_prenotazioni(lista_prenotazioni):
    ricerca = input("Ricerca: ")
    for prenotazione in lista_prenotazioni:
        if ricerca in prenotazione.nome or ricerca in prenotazione.data:
            print(prenotazione)
            
            
def visualizza_prenotazioni(lista_prenotazioni):
    for prenotazione in lista_prenotazioni:
        print(prenotazione)
        
def cancella_prenotazione(lista_prenotazioni):
    nome = input("Nome: ")
    for prenotazione in lista_prenotazioni:
        if prenotazione.nome == nome:
            lista_prenotazioni.remove(prenotazione)
            
def main():
    lista_prenotazioni = []
    lista_prenotazioni.append(Prenotazione("Dario", "2021-05-12", "12:00", 4, "confermata"))
    lista_prenotazioni.append(Prenotazione("Angelo", "2021-05-12", "16:00", 2, "confermata"))
    lista_prenotazioni.append(Prenotazione("pierluigi", "2021-05-12", "19:00", 6, "confermata"))
    lista_prenotazioni.append(Prenotazione("Pietro", "2021-05-12", "21:00", 3, "confermata"))
    lista_prenotazioni.append(Prenotazione("Eleonora", "2021-05-13", "12:00", 4, "confermata"))
    lista_prenotazioni.append(Prenotazione("Michele", "2021-05-13", "16:00", 2, "confermata"))
    
    while True:
        print("1. Aggiungi prenotazione")
        print("2. Cerca prenotazioni")
        print("3. Visualizza prenotazioni")
        print("4. Cancella prenotazione")
        print("5. Esci")
        scelta = input("Cosa vuoi fare? ")
        if scelta == "1":
            lista_prenotazioni.append(aggiungi_prenotazione())
        elif scelta == "2":
            cerca_prenotazioni(lista_prenotazioni)
            print(lista_prenotazioni)
        elif scelta == "3":
            visualizza_prenotazioni(lista_prenotazioni)
        elif scelta == "4":
            cancella_prenotazione(lista_prenotazioni)
        elif scelta == "5":
            break
        else:
            print("Scelta non valida")
            
if __name__ == "__main__":
    main()










#Gestire le prenotazioni in un ristorante. Ogni prenotazione ha un nome del cliente, una data e ora, un numero di persone e uno stato (confermata, in attesa, cancellata). Il sistema deve permettere di:
#Aggiungere nuove prenotazioni.
#Cercare prenotazioni per nome del cliente o data.
#Visualizzare tutte le prenotazioni.
#Cancellare una prenotazione.
#Il sistema deve includere due classi principali:
#: rappresenta una singola prenotazione nel ristorante.
#: gestisce le prenotazioni e le operazioni associate.