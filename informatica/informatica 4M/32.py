class Quiz:
    def __init__(self, corso, studenti, corsi, domande, risposte, punteggio, tempo, difficolta, argomento, tentativi, testo):
        self.corso = corso
        self.studenti = studenti
        self.corsi = corsi
        self.domande = domande
        self.risposte = risposte
        self.punteggio = punteggio
        self.tempo = tempo
        self.difficolta = difficolta
        self.argomento = argomento
        self.tentativi = tentativi
        self.testo = testo

    def aggiungi_domanda(self, domande):
        self.domande.append(domande)

    def rimuovi_domanda(self, domande):
        self.domande.remove(domande)

    def aggiungi_risposta(self, risposte):
        self.risposte.append(risposte)

    def rimuovi_risposta(self, risposte):
        self.risposte.remove(risposte)

    def calcola_punteggio_finale(self):
        self.punteggio = 0
        for risposta in self.risposte:
            if risposta == True:
                self.punteggio += 1
        return self.punteggio

    def punteggio_minimo(self):
        self.punteggio = 0
        for punteggio in self.punteggio:
            if punteggio < self.punteggio:
                self.punteggio = punteggio
        return self.punteggio

    def valuta_rispote(self, calcola_punteggio_finale):
        self.punteggio = calcola_punteggio_finale
        if self.punteggio >= 6:
            return True
        else:
            return False
        


class Corso:
    def __init__(self, studenti, quiz, titolo, descrizione, docente):
        self.studenti = studenti
        self.quiz = quiz
        self.titolo = titolo
        self.descrizione = descrizione
        self.docente = docente


class Studente:
    def __init__(self, quiz, corsi, nome, cognome, matricola):
        self.quiz = quiz
        self.corsi = corsi
        self.nome = nome
        self.cognome = cognome
        self.matricola = matricola

    def quiz_effettuati(self):
        self.quiz = 0
        for quiz in self.quiz:
            self.quiz += 1
        return self.quiz

    def registra_risposta(self):
        self.risposta = True
        return self.risposta

    def punteggio_ottenuto(self):
        self.punteggio = 0
        for quiz in self.quiz:
            self.punteggio += quiz.calcola_punteggio_finale()
        return self.punteggio

    def quiz_superati(self):
        self.quiz = 0
        for quiz in self.quiz:
            if quiz.valuta_rispote() == True:
                self.quiz += 1
        return self.quiz

    def quiz_falliti(self):
        self.quiz = 0
        for quiz in self.quiz:
            if quiz.valuta_rispote() == False:
                self.quiz += 1
        return self.quiz

    def verifica_superamento(self, punteggio_ottenuto):
        self.punteggio = punteggio_ottenuto
        if self.punteggio >= 18:
            return True
        else:
            return False


