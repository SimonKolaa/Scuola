class Frazione:

    def __init__(self, numeratore, denominatore):
        self.numeratore = numeratore
        self.denominatore = denominatore
        
    def __add__(self, other):
        if self.denominatore == other.denominatore:
            return Frazione(self.numeratore + other.numeratore, self.denominatore)
        else:
            raise ValueError("i denominatori devono essere uguali per sommare le frazioni.")
    
    def __sub__(self, other):
        if self.denominatore == other.denominatore:
            return Frazione(self.numeratore - other.numeratore, self.denominatore)
        else:
            raise ValueError("i denominatori devono essere uguali per sottrarre le frazioni.")
    
    def __mul__(self, other):
        return Frazione(self.numeratore * other.numeratore, self.denominatore * other.denominatore)
    
    def __str__(self):
        return f"{self.numeratore}/{self.denominatore}"