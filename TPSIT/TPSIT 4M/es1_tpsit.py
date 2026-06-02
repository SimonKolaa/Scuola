import threading

class ContoBancario:
    def __init__(self, saldo_iniziale=0):
        self.saldo = saldo_iniziale
        self.lock = threading.Lock()

    def deposito(self, importo):
        with self.lock:
            self.saldo += importo
            print(f"Deposito di {importo} effettuato. saldo attuale: {self.saldo}")

    def prelievo(self, importo):
        with self.lock:
            if self.saldo >= importo:
                self.saldo -= importo
                print(f"prelievo di {importo} effettuato. saldo attuale: {self.saldo}")
            else:
                print(f"prelievo di {importo} fallito. saldo insufficiente. saldo attuale: {self.saldo}")

def operazioni_utente(conto, operazioni):
    for operazione, importo in operazioni:
        if operazione == 'deposito':
            conto.deposito(importo)
        elif operazione == 'prelievo':
            conto.prelievo(importo)

if __name__ == "__main__":
    conto = ContoBancario(100)

    operazioni_utente1 = [('deposito', 50), ('prelievo', 30), ('prelievo', 70)]
    operazioni_utente2 = [('prelievo', 20), ('deposito', 100), ('prelievo', 50)]

    thread1 = threading.Thread(target=operazioni_utente, args=(conto, operazioni_utente1))
    thread2 = threading.Thread(target=operazioni_utente, args=(conto, operazioni_utente2))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print(f"saldo finale: {conto.saldo}")