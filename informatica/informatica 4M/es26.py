class Veicolo:
    def __init__(self, marca, modello, carburante):
        self.marca = marca
        self.modello = modello
        self.carburante = carburante
        
class Auto(Veicolo):
    def __init__(self, marca, modello, carburante):
        super().__init__(marca, modello, carburante)
        
class Camion(Veicolo):
    def __init__(self, marca, modello, carburante):
        super().__init__(marca, modello, carburante)
        
class Flotta:
    def __init__(self):
        self.lista_veicoli = []
        
    def aggiungi_veicolo(self, veicolo):
        self.lista_veicoli.append(veicolo)
        
    def visualizza_veicoli(self):
        for veicolo in self.lista_veicoli:
            print(f"Marca: {veicolo.marca}, Modello: {veicolo.modello}, Carburante: {veicolo.carburante}")
        
        
def main():
    flotta = Flotta()
    flotta.aggiungi_veicolo(Auto("Fiat", "Punto", "Benzina"))
    flotta.aggiungi_veicolo(Auto("lamberjamber", "urus", "benzina"))
    flotta.aggiungi_veicolo(Auto("Ford", "Fiesta", "Benzina"))
    flotta.aggiungi_veicolo(Auto("Mercedes", "Classe G", "benzina"))
    flotta.aggiungi_veicolo(Auto("Audi", "A3", "Diesel"))
    flotta.aggiungi_veicolo(Camion("Iveco", "Eurocargo", "Diesel"))
    flotta.aggiungi_veicolo(Camion("Mercedes", "Actros", "Diesel"))
    
    
    while True:
        print("1. Aggiungi veicolo")
        print("2. Visualizza veicoli")
        print("3. Esci")
        scelta = input("Cosa vuoi fare? ")
        if scelta == "1":
            marca = input("Marca: ")
            modello = input("Modello: ")
            carburante = input("Carburante: ")
            flotta.aggiungi_veicolo(Auto(marca, modello, carburante))
        elif scelta == "2":
            flotta.visualizza_veicoli()
        elif scelta == "3":
            break
        else:
            print("Scelta non valida")
            
if __name__ == "__main__":
    main()
    
            
         
        
        
            

















#Il programma ci permette di gestire una flotta aziendale di veicoli. Ogni veicolo ha una marca, un modello e un tipo di carburante. Esistono due tipologie di veicoli: *auto* e *camion*. Ogni veicolo può essere aggiunto alla flotta, e il programma deve consentire di visualizzare le informazioni sui veicoli.
#Requisiti:
#1. Creare una classe `Veicolo` con gli attributi di base: `marca`, `modello` e `carburante`.
#2. Creare due sottoclassi: `Auto` e `Camion`. Ogni sottoclasse deve semplicemente ereditare gli attributi da `Veicolo`.
#3. La classe `Flotta` deve gestire una lista di veicoli, permettere l’aggiunta di nuovi veicoli, e la visualizzazione delle informazioni di tutti i veicoli.