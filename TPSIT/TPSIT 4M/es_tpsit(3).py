import threading
import math
import os

def calcola_cubo(number):
    print(f"Il cubo di {number} è {number ** 3}")

def calcola_radice(number):
    print(f"La radice quadrata di {number} è {math.sqrt(number)}")
    
    get_id = os.getpid()
    print(f"ID del processo: {get_id}")
    

if __name__ == "__main__":
    number = 9

    thread1 = threading.Thread(target=calcola_cubo, args=(number,))
    thread2 = threading.Thread(target=calcola_radice, args=(number,))

    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()

    print("Calcoli eseguiti")