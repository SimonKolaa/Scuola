class Prenotazione:
    def __init__(self, nome, data, ora, numero_persone, stato):
        self.nome = nome
        self.data = data
        self.ora = ora
        self.numero_persone = numero_persone
        self.stato = stato

    def __str__(self):
        return f"{self.nome} - {self.data} - {self.ora} - {self.numero_persone} - {self.stato}"


def aggiungi_prenotazione
    nome = input("Nome: ")
    data = input("Data: ")
    ora = input("Ora: ")
    numero_persone = int(input("Numero persone: "))
    stato = input("Stato: ")
    prenotazione = Prenotazione(nome, data, ora, numero_persone, stato)
    return prenotazione











#Gestire le prenotazioni in un ristorante. Ogni prenotazione ha un nome del cliente, una data e ora, un numero di persone e uno stato (confermata, in attesa, cancellata). Il sistema deve permettere di:
#Aggiungere nuove prenotazioni.
#Cercare prenotazioni per nome del cliente o data.
#Visualizzare tutte le prenotazioni.
#Cancellare una prenotazione.
#Il sistema deve includere due classi principali:
#: rappresenta una singola prenotazione nel ristorante.
#: gestisce le prenotazioni e le operazioni associate.