class Auto:
    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello
        self.motore = None

    def get_marca(self):
        return self.marca

    def set_marca(self, marca):
        self.marca = marca

    def get_modello(self):
        return self.modello

    def set_modello(self, modello):
        self.modello = modello

    def associa_motore(self, motore):
        if isinstance(motore, Motore):
            if self.motore is not None:
                self.motore.auto = None
            self.motore = motore
            if motore.auto is not self:
                motore.associa_auto(self)

class Motore:
    def __init__(self, numero_seriale, tipo):
        self.numero_seriale = numero_seriale
        self.tipo = tipo
        self.auto = None

    def get_numero_seriale(self):
        return self.numero_seriale

    def set_numero_seriale(self, numero_seriale):
        self.numero_seriale = numero_seriale

    def get_tipo(self):
        return self.tipo

    def set_tipo(self, tipo):
        self.tipo = tipo

    def associa_auto(self, auto):
        if isinstance(auto, Auto):
            if self.auto is not None:
                self.auto.motore = None
            self.auto = auto
            if auto.motore is not self:
                auto.associa_motore(self)


auto1 = Auto("Fiat", "Punto")
motore1 = Motore("12345", "Benzina")


auto1.associa_motore(motore1)

print(f"L'auto {auto1.get_marca()} {auto1.get_modello()} ha il motore con numero seriale {auto1.motore.get_numero_seriale()} e tipo {auto1.motore.get_tipo()}.")
print(f"Il motore con numero seriale {motore1.get_numero_seriale()} e tipo {motore1.get_tipo()} è associato all'auto {motore1.auto.get_marca()} {motore1.auto.get_modello()}.")