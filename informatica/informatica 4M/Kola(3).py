from datetime import date

class Libro:
    def __init__(self, titolo, data_pubblicazione, autore):
        self.titolo = titolo
        self.data_pubblicazione = data_pubblicazione
        self.autore = autore
        self.utente_prestito = None
        self.data_prestito = None
        self.data_restituzione = None

    def __str__(self):
        return f"{self.titolo} ({self.autore})"

class Autore:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome
        self.libri = []

    def __str__(self):
        return f"{self.nome} {self.cognome}"

class Utente:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome
        self.libri_prestati = []

    def __str__(self):
        return f"{self.nome} {self.cognome}"

class Biblioteca:
    def __init__(self):
        self.libri = []
        self.utenti = []
        self.autori = []

    def aggiungi_libro(self, libro):
        self.libri.append(libro)
        if libro.autore not in self.autori:
            self.autori.append(libro.autore)
        libro.autore.libri.append(libro)

    def aggiungi_utente(self, utente):
        self.utenti.append(utente)

    def presta_libro(self, libro, utente, data_prestito):
        if libro.utente_prestito is None:
            libro.utente_prestito = utente
            libro.data_prestito = data_prestito
            utente.libri_prestati.append(libro)

    def restituisci_libro(self, libro, data_restituzione):
        if libro.utente_prestito is not None:
            libro.utente_prestito.libri_prestati.remove(libro)
            libro.utente_prestito = None
            libro.data_restituzione = data_restituzione

    def libri_disponibili(self):
        return [libro for libro in self.libri if libro.utente_prestito is None]

    def cerca_libri_per_autore(self, autore):
        return [libro for libro in self.libri if libro.autore == autore]

    def cerca_libro_per_titolo(self, titolo):
        return [libro for libro in self.libri if titolo.lower() in libro.titolo.lower()]

    def ottieni_libri(self):
        return self.libri

    def ottieni_utenti(self):
        return self.utenti

def main():
    biblioteca = Biblioteca()

    autore1 = Autore("Alessandro", "Manzoni")
    autore2 = Autore("Italo", "Calvino")

    libro1 = Libro("I Promessi Sposi", date(1827, 1, 1), autore1)
    libro2 = Libro("Il barone rampante", date(1957, 1, 1), autore2)
    biblioteca.aggiungi_libro(libro1)
    biblioteca.aggiungi_libro(libro2)

    utente1 = Utente("Mario", "Rossi")
    utente2 = Utente("Laura", "Bianchi")
    biblioteca.aggiungi_utente(utente1)
    biblioteca.aggiungi_utente(utente2)

    # Test operazioni
    print("Libri disponibili:", [str(l) for l in biblioteca.libri_disponibili()])

    # Prestito libro
    biblioteca.presta_libro(libro1, utente1, date.today())
    print(f"\nLibro '{libro1}' prestato a {utente1}")

    # Verifica disponibilità
    print("\nLibri disponibili dopo il prestito:",
          [str(l) for l in biblioteca.libri_disponibili()])

    # Ricerca per autore
    print(f"\nLibri di {autore1}:",
          [str(l) for l in biblioteca.cerca_libri_per_autore(autore1)])

    # Restituzione libro
    biblioteca.restituisci_libro(libro1, date.today())
    print(f"\nLibro '{libro1}' restituito")

    print("\nLibri disponibili dopo la restituzione:",
          [str(l) for l in biblioteca.libri_disponibili()])

    # Ricerca libro per titolo
    libri_trovati = biblioteca.cerca_libro_per_titolo("Promessi")
    print(f"\nLibri trovati con titolo contenente 'Promessi':", [str(l) for l in libri_trovati])

    # Ottieni tutti i libri
    print("\nTutti i libri in biblioteca:", [str(l) for l in biblioteca.ottieni_libri()])

    # Ottieni tutti gli utenti
    print("\nTutti gli utenti in biblioteca:", [str(u) for u in biblioteca.ottieni_utenti()])

if __name__ == "__main__":
    main()


print ("posso dire buon natale?")
if True:
    "buon natale ragazzi mieiiiiiiiii"
