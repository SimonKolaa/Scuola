class Dispositivo:
    numero_dispositivi = 0
     def __init__(self, marca, modello, prezzo, disponibile=True):
        self.marca = marca
        self.modello = modello
        self.prezzo = prezzo
     Dispositivo.numero_dispositivi += 1

    def vendi(self, disponibile=False):
        
    def rifornisci(self, disponibile=True):
        
    @classmethod
    def conta_dispositivi(cls):
        return cls.numero_dispositivi

    @staticmethod
    def calcola_sconto(prezzo, sconto):
        return (prezzo * sconto / 100)

class Smartphone(Dispositivo):
    def __init__(self, marca, modello, prezzo, memoria):
        super().__init__(marca, modello, prezzo)
        self.memoria = memoria

    def descrizione(self):
        return f"smartphone {self.marca} {self.modello} con {self.memoria}GB di memoria"

class Laptop(Dispositivo):
    def __init__(self, marca, modello, prezzo, ram):
        super().__init__(marca, modello, prezzo)
        self.ram = ram

    def descrizione(self):
        return f"laptop {self.marca} {self.modello} con {self.ram}GB di RAM"

class Tablet(Dispositivo):
    def __init__(self, marca, modello, prezzo, dimensione_schermo):
        super().__init__(marca, modello, prezzo)
        self.dimensione_schermo = dimensione_schermo

    def descrizione(self):
        return f"tablet {self.marca} {self.modello} con schermo da {self.dimensione_schermo} pollici"

class Inventario:
    def __init__(self):
    def aggiungi_dispositivo(self, dispositivo):
        self.dispositivi.append(dispositivo)
inventario = Inventario()
inventario.aggiungi_dispositivo(smartphone)
inventario.aggiungi_dispositivo(laptop)
inventario.aggiungi_dispositivo(tablet)

