class Piatto:
    def __init__(self, nome, prezzo, disponibile=True):
        self.nome = nome
        self.prezzo = prezzo
        self.disponibile = disponibile

    def ordina(self):
        if self.disponibile:
            self.disponibile = False
            
    def disponi(self):
        if not self.disponibile:
            self.disponibile = True

    def __str__(self):
        return f"{self.nome} - {self.prezzo}€ - {'active' if self.disponibile else 'non ce'}"

class Antipasto(Piatto):
    def __init__(self, nome, prezzo, ingredienti, porzione, disponibile=True):
        super().__init__(nome, prezzo, disponibile)
        self.ingredienti = ingredienti
        self.porzione = porzione

class Primo(Piatto):
    def __init__(self, nome, prezzo, tipo_pasta, sugo, disponibile=True):
        super().__init__(nome, prezzo, disponibile)
        self.tipo_pasta = tipo_pasta
        self.sugo = sugo

class Secondo(Piatto):
    def __init__(self, nome, prezzo, tipo_carne, cottura, disponibile=True):
        super().__init__(nome, prezzo, disponibile)
        self.tipo_carne = tipo_carne
        self.cottura = cottura

class Dolce(Piatto):
    def __init__(self, nome, prezzo, tipo_dolce, calorie, disponibile=True):
        super().__init__(nome, prezzo, disponibile)
        self.tipo_dolce = tipo_dolce
        self.calorie = calorie

def calcola_conto(lista_piatti=[]):
    totale = 0
    for piatto in lista_piatti:
        totale += piatto.prezzo
    return totale

def stampa_menu(lista_piatti=[]):
    for piatto in lista_piatti:
        print(piatto)

# Esempio di utilizzo
antipasto = Antipasto("Bruschetta con casali sopra", 50, ["Pane", "Pomodoro", "Basilico, casali"], "Piccola")
primo = Primo("Spaghetti alla Carbonara", 12.0, "Spaghetti", "Carbonara")
secondo = Secondo("Bistecca alla Fiorentina", 25.0, "Manzo", "Media")
dolce = Dolce("Tiramisù", 6.0, "Tiramisù", 450)

piatti_ordinati = [antipasto, primo, secondo, dolce]
conto_totale = calcola_conto(piatti_ordinati)
print(f"Il conto totale è: {conto_totale}€")

print("\nMenu del Ristorante:")
stampa_menu(piatti_ordinati)