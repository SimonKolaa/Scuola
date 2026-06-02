import threading

vettore = [0] * 10

def pari():
    for i in range(0, 10, 2):  
        value = int(input(f"Thread 1: Inserisci un valore{i}:"))
        vettore[i] = value
        print(f"Thread 1: Inserito {value} in posizione {i}")
            
def dispari():
    for i in range(1, 10, 2):  
        value = int(input(f"Thread 2: Inserisci un valore {i}:"))
        vettore[i] = value
        print(f"Thread 2: Inserito {value} in posizione {i}")

if __name__ == "__main__":
    thread1 = threading.Thread(target=pari)
    thread2 = threading.Thread(target=dispari)

    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()

    print("Vettore finale:", vettore)
