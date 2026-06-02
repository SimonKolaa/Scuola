import threading
import os
result1 = 0
result2 = 0

def calculate_addition():
    pid = os.getpid()
    thread_id = threading.current_thread().ident
    print(f"Thread 1 - PID: {pid}, Thread ID: {thread_id}")
    result1 = 5 + 3 
    print(f"Risultato dell'addizione (5 + 3): {result1}")

def calculate_subtraction():
    pid = os.getpid()
    thread_id = threading.current_thread().ident
    print(f"Thread 2 - PID: {pid}, Thread ID: {thread_id}")
    result2 = 4 - 2
    print(f"Risultato della sottrazione (4 - 2): {result2}")

if __name__ == "__main__":
    print(f"Processo principale - PID: {os.getpid()}")
    print(f"Processo padre - PPID: {os.getppid()}")
    
    thread1 = threading.Thread(target=calculate_addition)
    thread2 = threading.Thread(target=calculate_subtraction)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    final_result = result1 * result2
    print(f"Risultato finale (8) * (2): {final_result}")
