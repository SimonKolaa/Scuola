import threading
import random

class Scatola:
    def __init__(self):
        self.num_caramelle = 20
        self.lock = threading.Lock()

    def aggiungi_caramelle(self, quantita):
        with self.lock:
            self.num_caramelle += quantita
            print(f"Aggiunte {quantita} caramelle | Totale: {self.num_caramelle}")

    def consuma_caramella(self):
        with self.lock:
            if self.num_caramelle > 0:
                self.num_caramelle -= 1
                print(f"Consumata 1 caramella | Totale: {self.num_caramelle}")

def produttore(scatola):
    for _ in range(10):
        quantita = random.randint(1, 10)
        scatola.aggiungi_caramelle(quantita)
        if random.random() < 0.5:
            scatola.consuma_caramella()

def consumatore(scatola):
    for _ in range(10):
        scatola.consuma_caramella()
        if random.random() < 0.5:
            quantita = random.randint(1, 10)
            scatola.aggiungi_caramelle(quantita)

if __name__ == "__main__":
    scatola = Scatola()

    thread_produttore = threading.Thread(target=produttore, args=(scatola,))
    thread_consumatore = threading.Thread(target=consumatore, args=(scatola,))

    thread_produttore.start()
    thread_consumatore.start()

    thread_produttore.join()  
    thread_consumatore.join()