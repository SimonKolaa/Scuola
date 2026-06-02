class Studente:
    def __init__(self, nome, matricola):
        self.nome = nome
        self.matricola = matricola
        self.corsi = []

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_matricola(self):
        return self.matricola

    def set_matricola(self, matricola):
        self.matricola = matricola

    def add_corso(self, corso):
        if isinstance(corso, Corso) and corso not in self.corsi:
            self.corsi.append(corso)
            corso.add_studente(self)

    def get_corsi(self):
        return self.corsi
    
class Corso:
    def __init__(self, titolo, codice):
        self.titolo = titolo
        self.codice = codice
        self.studenti = []

    def get_titolo(self):
        return self.titolo

    def set_titolo(self, titolo):
        self.titolo = titolo

    def get_codice(self):
        return self.codice

    def set_codice(self, codice):
        self.codice = codice

    def add_studente(self, studente):
        if isinstance(studente, Studente) and studente not in self.studenti:
            self.studenti.append(studente)
            studente.add_corso(self)

    def get_studenti(self):
        return self.studenti
    
    
studente1 = Studente("Mario Rossi", "12345")
studente2 = Studente("Luigi Bianchi", "67890")

corso1 = Corso("Matematica", "MAT101")
corso2 = Corso("Fisica", "FIS102")

studente1.aggiungi_corso(corso1)
studente1.aggiungi_corso(corso2)
studente2.aggiungi_corso(corso1)


print(f"Studente {studente1.get_nome()} ({studente1.get_matricola()}) è iscritto ai corsi:")
for corso in studente1.get_corsi():
    print(f"- {corso.get_titolo()} ({corso.get_codice()})")

print(f"Studente {studente2.get_nome()} ({studente2.get_matricola()}) è iscritto ai corsi:")
for corso in studente2.get_corsi():
    print(f"- {corso.get_titolo()} ({corso.get_codice()})")

print(f"Corso {corso1.get_titolo()} ({corso1.get_codice()}) ha gli studenti:")
for studente in corso1.get_studenti():
    print(f"- {studente.get_nome()} ({studente.get_matricola()})")

print(f"Corso {corso2.get_titolo()} ({corso2.get_codice()}) ha gli studenti:")
for studente in corso2.get_studenti():
    print(f"- {studente.get_nome()} ({studente.get_matricola()})")

