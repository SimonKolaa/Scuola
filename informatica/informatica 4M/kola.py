from datetime import date

class SistemaGestionaleZoo:
     def __init__(self):
        self.animali = []
        self.habitat = []
        self.visite = []
        self.veterinari = []
        
     def aggiungi_animale(self, animale):
            self.animali.append(self, animale)
            animale.habitat = self
    
     def rimuovi_animale(self, animale):
            self.animali.remove(self, animale)
            animale.habitat = self
             
def assegna_habitat(self, habitat. animale):
            habitat.disponibile = True
            
            
    
def registra_visite(self, visita):
        self.visita.append(self, visita)
    
def get_storico_visite(self, animale):
        return self.animali
        
    
def get_habitat_compatibili(self, animale):
        habitat_compatibili = []
        for animale  in self.habitat:
             if habitat_compatibili == habitat_compatibili:
                habitat_compatibili.append(animale)
        return habitat_compatibili
    
   
                

    

class Animale:
    def __init__(self, codiceidentificativo, nome, eta, peso) -> None:
        self.codiceidentificativo= codiceidentificativo
        self.nome = nome
        self.eta = eta
        self.peso = peso
        self.visite = []
        
    def aggiungi_visita(self, visita) -> None:
        self.visite.append(visita)
        visita.animale = self
    
        
class Mammifero(Animale):
     def __init__(self, codiceidentificativo, nome, eta, peso, tipoPelliccia, temperaturaCorpo, periodoGestazionale) -> None:
        super().__init__(codiceidentificativo, nome, eta, peso)
        self.tipoPelliccia = tipoPelliccia
        self.temperaturaCorpo = temperaturaCorpo
        self.periodoGestazionale = periodoGestazionale
        
class Rettile(Animale):
     def __init__(self, codiceidentificativo, nome, eta, peso, velenoso) -> None:
        super().__init__(codiceidentificativo, nome, eta, peso)
        self.velenoso = True

        
class Habitat:
     def __init__(self, codiceArea, nome, dimensione) -> None:
        self.codiceArea = codiceArea
        self.nome = nome
        self.dimensione = dimensione
        self.animali = []
        self.habitat = []
        
     def aggiungi_animale(self, animale):
            self.animali.append(self, animale)
            animale.habitat = self
            
     def rimuovi_animale(self, animale):
            self.animali.remove(animale)
            animale.habitat = self
            
     def get_animali(self):
        return self.animali
    
     def get_eta_media(self):
         
         
    
        class VisitaVeterinaria:
            def __init__(self, data, diagnosi, trattamentoProposto, animale) -> None:
                self.Data = data
                self.diagnosi = diagnosi
                self.trattamentoProposto = trattamentoProposto
                self.animale = animale
        
class Veterinario:
     def __init__(self, matricola, nome, cognome, anniEsperienza, specializzazione) -> None:
        self.matricola = matricola
        self.nome = nome
        self.cognome = cognome
        self.anniEsperienza = anniEsperienza
        self.specializzazione = specializzazione
        
        
        def effettua_visita(self, diagnosi, trattamento):
            
        
        

    
        
        
        
        
        
def main():
    # Creazione del sistema
    zoo = SistemaGestioneZoo()

    # Creazione degli habitat
    savana = Habitat("H001", "Savana Africana", 1000.0)
    rettilario = Habitat("H002", "Rettilario", 500.0)
    zoo.habitats.extend([savana, rettilario])

    # Creazione dei veterinari
    vet1 = Veterinario("V001", "Mario", "Rossi", "Mammiferi", 10)
    vet2 = Veterinario("V002", "Laura", "Bianchi", "Rettili", 8)
    zoo.veterinari.extend([vet1, vet2])

    # Creazione degli animali
    leone = Mammifero("M001", "Simba", 5, 180.0, "Folta", 38.5, 110)
    serpente = Rettile("R001", "Kaa", 3, 5.0, True)
    giraffa = Mammifero("M002", "Melman", 7, 800.0, "Maculata", 38.0, 450)

    # Aggiunta degli animali al sistema
    for animale in [leone, serpente, giraffa]:
        zoo.aggiungi_animale(animale)

    # Assegnazione degli habitat
    zoo.assegna_habitat(leone, savana)
    zoo.assegna_habitat(giraffa, savana)
    success = zoo.assegna_habitat(serpente, savana)
    print("\nTentativo di mettere serpente in savana:", "Riuscito" if success else "Fallito")
    zoo.assegna_habitat(serpente, rettilario)

    # Effettuazione delle visite veterinarie
    visita1 = vet1.effettua_visita(leone, "Controllo di routine", "Somministrazione vaccino annuale")
    zoo.registra_visita(visita1)

    visita2 = vet2.effettua_visita(serpente, "Infezione batterica", "Antibiotico per 7 giorni")
    zoo.registra_visita(visita2)

    # Stampa delle informazioni
    print("\n=== Stato dello Zoo ===")

    print("\nAnimali nella Savana:")
    for animale in zoo.get_animali_habitat(savana):
        print(f"- {animale.nome} ({animale.codiceIdentificativo})")

    print("\nAnimali nel Rettilario:")
    for animale in zoo.get_animali_habitat(rettilario):
        print(f"- {animale.nome} ({animale.codiceIdentificativo})")

    print("\nEtà media per habitat:")
    for habitat, eta_media in zoo.calcola_eta_media_per_habitat().items():
        print(f"- {habitat}: {eta_media:.1f} anni")

    print("\nStorico visite di Simba:")
    for visita in zoo.get_storico_visite(leone):
        print(f"- Data: {visita.data}")
        print(f"  Veterinario: {visita.veterinario.nome} {visita.veterinario.cognome}")
        print(f"  Diagnosi: {visita.diagnosi}")
        print(f"  Trattamento: {visita.trattamentoProposto}")


if __name__ == "__main__":
    main()

# Tentativo di mettere serpente in savana: Fallito

# === Stato dello Zoo ===

# Animali nella Savana:
# - Simba (M001)
# - Melman (M002)

# Animali nel Rettilario:
# - Kaa (R001)

# Età media per habitat:
# - Savana Africana: 6.0 anni
# - Rettilario: 3.0 anni

# Storico visite di Simba:
# - Data: 2025-02-11 15:27:06.489484
#   Veterinario: Mario Rossi
#   Diagnosi: Controllo di routine
#   Trattamento: Somministrazione vaccino annuale
