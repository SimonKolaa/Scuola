import threading
import time

class Numero:
    def __init__(self) -> None:
        self.numero = 20
        self.lock = threading.Lock()

    def pari(self):
            while self.numero <= 40:
                with self.lock:
                    if self.numero % 2 == 0:
                        print(self.numero)
            self.numero += 1



    def dispari(self):
          while self.numero <= 40:
            if self.numero % 2 == 0:
                print(self.numero)
            self.numero += 1
           

n = Numero()
t1 = threading.Thread(target=n.pari())
t2 = threading.Thread(target=n.dispari())

t1.start()
t2.start()
t1.join()
t2.join()
print("fine")