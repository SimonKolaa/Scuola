import threading
import random

class Buffer:
    def __init__(self):
        self.areacondivisa = 0
        self.produttore_lock = threading.Lock()
        self.consumatore_lock = threading.Lock()
        self.consumatore_lock.acquire()

    def get_dato(self):
        self.consumatore_lock.acquire()
        dato = self.areacondivisa
        self.produttore_lock.release()
        return dato
    
    def set_dato(self, dato):
        self.produttore_lock.acquire()
        self.areacondivisa = dato
        self.consumatore_lock.release()
    
    def produttore(self):
        for i in range(5):
            self.set_dato(i)
            print("Produttore ha prodotto", i)

    def consumatore(self):
        for i in range(5):
            print("Consumatore ha consumato", self.get_dato())

buffer = Buffer()
produttore = threading.Thread(target=buffer.produttore)
consumatore = threading.Thread(target=buffer.consumatore)
consumatore.start()
produttore.start()
consumatore.join()
produttore.join()

print("Fine problemi")
