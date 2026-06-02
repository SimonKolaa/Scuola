import threading

class CalcolaThread(threading.Thread):
    def __init__(self, threadID, name, x, y):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.x = x
        self.y = y
        
    def run(self):
        print(str(self.threadID) + ""+ str(self.threadID))

x = int(input("Inserisci il valore di x: "))
y = int(input("Inserisci il valore di y: "))

thread1 = CalcolaThread(1, "Thread-1", x, y)
thread1.start()
thread2 = CalcolaThread(2, "Thread-2", x, y)
thread2.start()
