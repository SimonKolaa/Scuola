class Volo:
    def __init__(self, numeroVolo, destinazione, dataOraPartenza, numeroMassimoPasseggeri):
        self.numeroVolo = numeroVolo
        self.destinazione = destinazione
        self.dataOraPartenza = dataOraPartenza
        self.numeroMassimoPasseggeri = numeroMassimoPasseggeri

class Prenotazione:
    def __init__(self, nomePasseggero, tipoClasse, volo):
        self.nomePasseggero = nomePasseggero
        self.tipoClasse = tipoClasse
        self.volo = volo

class SistemaPrenotazioni:
    def __init__(self):
        self.voli = []
        self.prenotazioni = []
    
    def aggiungiVolo(self, volo):
        self.voli.append(volo)
    
    def aggiungiPrenotazione(self, prenotazione):
        self.prenotazioni.append(prenotazione)
    
    def visualizzaVoli(self):
        for volo in self.voli:
            print('Numero volo:', volo.numeroVolo)
            print('Destinazione:', volo.destinazione)
            print('Data e ora di partenza:', volo.dataOraPartenza)
            print('Numero massimo passeggeri:', volo.numeroMassimoPasseggeri)
            print()
    
    def visualizzaPrenotazioni(self):
        for prenotazione in self.prenotazioni:
            print('Nome passeggero:', prenotazione.nomePasseggero)
            print('Tipo classe:', prenotazione.tipoClasse)
            print('Volo numero:', prenotazione.volo.numeroVolo)
            print('Destinazione:', prenotazione.volo.destinazione)
            print()

def main():
    sistema = SistemaPrenotazioni()
    
    volo1 = Volo(1, "Roma", "2024-03-20 10:00", 100)
    volo2 = Volo(2, "Milano", "2024-03-20 14:00", 150)
    sistema.aggiungiVolo(volo1)
    sistema.aggiungiVolo(volo2)
    
    while True:
        print("1. Aggiungi volo")
        print("2. Aggiungi prenotazione")
        print("3. Visualizza voli")
        print("4. Visualizza prenotazioni")
        print("5. Esci")
        
        scelta = input("Seleziona un'opzione: ")
        
        if scelta == "1":
            numeroVolo = int(input("Numero volo: "))
            destinazione = input("Destinazione: ")
            dataOra = input("Data e ora (YYYY-MM-DD HH:MM): ")
            maxPasseggeri = int(input("Numero massimo passeggeri: "))
            nuovo_volo = Volo(numeroVolo, destinazione, dataOra, maxPasseggeri)
            sistema.aggiungiVolo(nuovo_volo)
            
        elif scelta == "2":
            sistema.visualizzaVoli()
            numeroVolo = int(input("Inserisci il numero del volo: "))
            volo_selezionato = None
            for volo in sistema.voli:
                if volo.numeroVolo == numeroVolo:
                    volo_selezionato = volo
                    break
            if volo_selezionato:
                nome = input("Nome passeggero: ")
                tipo = input("Tipo classe (economy/business): ")
                nuova_prenotazione = Prenotazione(nome, tipo, volo_selezionato)
                sistema.aggiungiPrenotazione(nuova_prenotazione)
            else:
                print("Volo non trovato")
                
        elif scelta == "3":
            sistema.visualizzaVoli()
            
        elif scelta == "4":
            sistema.visualizzaPrenotazioni()
            
        elif scelta == "5":
            print("esci")
            break
            
        else:
            print("Opzione non valida")

if __name__ == "__main__":
    main()