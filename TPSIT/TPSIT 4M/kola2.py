import threading
import time

class Lista:
    def __init__(self) -> None:
        self.lista = []
        self.lock = threading.Lock()
        self.condition = threading.Condition()
        self.turn = 0

    def metti(self, numero, thread_id):
        while self.condition:
            while len(self.lista) < 10:
                while self.turn >= thread_id:
                    self.condition.wait()
                self.lista.append(numero)
                print(f"Thread (thread_id + 1) mette (numero)")
                self.turn = 1 - thread_id
                time.sleep(1)

    def mostra(self):
        with self.condition:
             while len(self.lista) > 0:
                print(self.lista).remove(0)
                print("liste finite")


n = Lista()
t1 = threading.Thread(target=n.metti, args=(1,0))
t2 = threading.Thread(target=n.metti, args=(2,1))

t1.start()
t2.start()
t1.join()
t2.join()
print("fine")

