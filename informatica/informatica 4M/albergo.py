#Descrizione dell'esercizio
#Il sistema permette di gestire le prenotazioni in un albergo. L'albergo ha diverse camere, e ogni camera ha un numero, un tipo (singola, doppia, suite) e una disponibilità (occupata o libera). Il sistema deve permettere di:
#
#- Aggiungere nuove camere all'albergo.
#- Prenotare una camera (verificando se è disponibile).
#- Visualizzare le camere disponibili.
#- Visualizzare le prenotazioni effettuate.
#
#Il sistema deve includere due classi principali:
#1. Camera: rappresenta una singola camera dell'albergo.
#2. Albergo: rappresenta l'albergo che gestisce le camere e le prenotazioni.

class Camera:
    def __init__(self, numero, tipo, prezzo, prenotata=False):
        self.numero = numero
        self.tipo = tipo
        self.prezzo = prezzo
        self.prenotata = prenotata

class Albergo:
    def __init__(self):
        self.camere = []
        
    def aggiungi_camera(self, camera):
        self.camere.append(camera)

    def prenota_camera(self, numero):
        for camera in self.camere:
            if camera.numero == numero:
                if camera.prenotata:
                    print("Camera non disponibile")
                else:
                    camera.prenotata = True
                    print("Prenotazione effettuata")
                return
        print("Camera non trovata")

    def camere_disponibili(self):
        for camera in self.camere:
            if not camera.prenotata:
                print(f"Camera {camera.numero} ({camera.tipo}) - {camera.prezzo}€")

    def prenotazioni_effettuate(self):
        for camera in self.camere:
            if camera.prenotata:
                print(f"Camera {camera.numero} ({camera.tipo}) - {camera.prezzo}€")

if __name__ == "__main__":
    albergo = Albergo()
    albergo.aggiungi_camera(Camera(101, "singola", 50))
    albergo.aggiungi_camera(Camera(102, "doppia", 80))
    albergo.aggiungi_camera(Camera(103, "suite", 150))

    print("Camere disponibili:")
    albergo.camere_disponibili()

    print("Prenotazione camera 102:")
    albergo.prenota_camera(102)

    print("Camere disponibili dopo la prenotazione:")
    albergo.camere_disponibili()

    print("Prenotazioni effettuate:")
    albergo.prenotazioni_effettuate()



