class Frazione:

    def __init__(self, numeratore, denominatore):
        self.numeratore = numeratore
        self.denominatore = denominatore
        
    def __add__(self, other):
        if self.denominatore == denominatore:
            return Frazione(self.numeratore + numeratore, self.denominatore)
        else:
            raise ValueError("i denominatori devono essere uguali per sommare le frazioni.")
    
    def __sub__(self, other):
        if self.denominatore == denominatore:
            return Frazione(self.numeratore - numeratore, self.denominatore)
        else:
            raise ValueError("i denominatori devono essere uguali per sottrarre le frazioni.")
    
    def __mul__(self, other):
        return Frazione(self.numeratore * numeratore, self.denominatore * denominatore)
    
    def __str__(self):
        return f"{self.numeratore}/{self.denominatore}"