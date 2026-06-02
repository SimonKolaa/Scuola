from threading import Thread
from threading import Lock
import time

mutex = Lock()

class threadconcorrenti(Thread):
    def __init__(self, nome, mutex):
        Thread.__init__(self)
        self.nome = nome
        self.mutex = mutex

    def run(self):
        self.mutex.acquire()
        print("Ciao sono il thread ferdinando magellano", self.nome)
        time.sleep(1)
        self.mutex.release()

    def run(self):
            self.mutex.acquire()
            print("Ciao sono il thread franco campanino", self.nome)
            time.sleep(1)
            self.mutex.release()

print("Inizio problemi")
t1 = threadconcorrenti("1", mutex)
t2 = threadconcorrenti("2", mutex)
t1.start()
t2.start()
t1.join()
t2.join()
print("Fine problemi")
