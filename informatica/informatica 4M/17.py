class Insegnante:
    def __init__(self, nome, cognome, strumento):
        self.nome = nome
        self.cognome = cognome
        self.strumento = strumento

    def get_nome(self):
        return self.nome

    def get_cognome(self):
        return self.cognome

    def get_strumento(self):
        return self.strumento

class Studente:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome
        self.corsi = []
        self.insegnante = None

    def get_nome(self):
        return self.nome

    def get_cognome(self):
        return self.cognome

    def get_corsi(self):
        return self.corsi

    def get_insegnante(self):
        return self.insegnante

    def iscrivi_corso(self, corso):
        self.corsi.append(corso)

    def set_insegnante(self, insegnante):
        self.insegnante = insegnante

    def __str__(self):
        return f'Studente: {self.nome} {self.cognome}, Insegnante: {self.insegnante.get_nome()} {self.insegnante.get_cognome()}, Corsi: {[corso.get_nome() for corso in self.corsi]}'

class Corso:
    def __init__(self, nome, durata):
        self.nome = nome
        self.durata = durata

    def get_nome(self):
        return self.nome

    def get_durata(self):
        return self.durata

def main():
    insegnante1 = Insegnante("Mario", "Rossi", "Pianoforte")
    insegnante2 = Insegnante("Luca", "Bianchi", "Chitarra")

    studente1 = Studente("Anna", "Verdi")
    studente2 = Studente("Marco", "Neri")

    studente1.set_insegnante(insegnante1)
    studente2.set_insegnante(insegnante2)

    corso1 = Corso("Teoria Musicale", "3 mesi")
    corso2 = Corso("Tecnica Pianistica", "6 mesi")

    studente1.iscrivi_corso(corso1)
    studente1.iscrivi_corso(corso2)
    studente2.iscrivi_corso(corso1)

    print(studente1)
    print(studente2)

if __name__ == "__main__":
    main()