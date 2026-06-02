import os

class Film:
    def __init__(self, titolo, regista, anno, genere, valutazione):
        self.titolo = titolo
        self.regista = regista
        self.anno = anno
        self.genere = genere
        self.valutazione = valutazione

    def __str__(self):
        return f"{self.titolo} di {self.regista} ({self.anno}) - {self.genere} ({self.valutazione})"
    
class Libreria:
    def __init__(self):
        self.films = []

    def aggiungi_film(self, film):
        self.films.append(film)

    def cerca_film(self, chiave):
        risultati = []
        for film in self.films:
            if chiave.lower() in film.titolo.lower() or chiave.lower() in film.regista.lower():
                risultati.append(film)
        return risultati

    def visualizza_film(self):
        for film in self.films:
            print(film)

    def valutazione_media(self):
        totale = 0
        for film in self.films:
            totale += film.valutazione
        return totale / len(self.films)
    
def main():
    libreria = Libreria()
    libreria.aggiungi_film(Film("subnetting e supernetting", "Dario Casali", 2021, "Azione", 10.0))
    libreria.aggiungi_film(Film("The Godfather", "Francis Ford Coppola", 1972, "Drammatico", 9.2))
    libreria.aggiungi_film(Film("The Dark Knight", "Di matteo pietro", 2025, "Azione", 3.0))
    libreria.aggiungi_film(Film("after earth", "M. Night Shyamalan", 2013, "Azione", 4.8))
    libreria.aggiungi_film(Film("angelo e pierluigi", "Gobetti", 2025, "Azione", 10.0))
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n1. Aggiungi film")
        print("2. Cerca film")
        print("3. Visualizza film")
        print("4. Valutazione media")
        print("5. Esci")
        scelta = input("Cosa vuoi fare? ")
        if scelta == "1":
            titolo = input("Titolo: ")
            regista = input("Regista: ")
            anno = int(input("Anno: "))
            genere = input("Genere: ")
            valutazione = float(input("Valutazione: "))
            libreria.aggiungi_film(Film(titolo, regista, anno, genere, valutazione))
            input("\nFilm aggiunto. Premi Invio per continuare...")
        elif scelta == "2":
            chiave = input("Cerca: ")
            risultati = libreria.cerca_film(chiave)
            if len(risultati) == 0:
                print("Nessun risultato")
            else:
                for film in risultati:
                    print(film)
            input("\nPremi Invio per continuare...")
        elif scelta == "3":
            libreria.visualizza_film()
            input("\nPremi Invio per continuare...")
        elif scelta == "4":
            print(f"Valutazione media: {libreria.valutazione_media()}")
            input("\nPremi Invio per continuare...")
        elif scelta == "5":
            break
        else:
            print("Scelta non valida")
            input("\nPremi Invio per continuare...")

if __name__ == "__main__":
    main()