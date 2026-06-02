import threading
import os
risultato1 = 0
risultato2 = 0

def calcola_addizione():
    pid = os.getpid()
    id_thread = threading.current_thread().ident
    print(f"Thread 1 - PID: {pid}, ID Thread: {id_thread}")
    risultato1 = 5 + 3 
    print(f"Risultato dell'addizione (5 + 3): {risultato1}")

def calcola_sottrazione():
    pid = os.getpid()
    id_thread = threading.current_thread().ident
    print(f"Thread 2 - PID: {pid}, ID Thread: {id_thread}")
    risultato2 = 4 - 2
    print(f"Risultato della sottrazione (4 - 2): {risultato2}")

if __name__ == "__main__":
    print(f"Processo principale - PID: {os.getpid()}")
    print(f"Processo padre - PPID: {os.getppid()}")
    
    thread1 = threading.Thread(target=calcola_addizione)
    thread2 = threading.Thread(target=calcola_sottrazione)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    risultato_finale = risultato1 * risultato2
    print(f"Risultato finale (8) * (2): {risultato_finale}")
