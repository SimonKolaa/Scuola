class MaterialeBiblioteca:
    def __init__(self, titolo, anno_pubblicazione, disponibile=True):
        self.titolo = titolo
        self.anno_pubblicazione = anno_pubblicazione
        self.disponibile = disponibile

    def prestito(self):
        if self.disponibile:
            self.disponibile = False

    def restituzione(self):
        if not self.disponibile:
            self.disponibile = True

class Libro(MaterialeBiblioteca):
    def __init__(self, titolo, anno_pubblicazione, autore, numero_pagine, disponibile=True):
        super().__init__(titolo, anno_pubblicazione, disponibile)
        self.autore = autore
        self.numero_pagine = numero_pagine

class Rivista(MaterialeBiblioteca):
    def __init__(self, titolo, anno_pubblicazione, numero_edizione, mese_pubblicazione, disponibile=True):
        super().__init__(titolo, anno_pubblicazione, disponibile)
        self.numero_edizione = numero_edizione
        self.mese_pubblicazione = mese_pubblicazione

class DVD(MaterialeBiblioteca):
    def __init__(self, titolo, anno_pubblicazione, regista, durata, disponibile=True):
        super().__init__(titolo, anno_pubblicazione, disponibile)
        self.regista = regista
        self.durata = durata