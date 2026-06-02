class Ricetta:
    def __init__(self, nome, tempo_preparazione, ingredienti, difficolta):
        self.nome = nome
        self.tempo_preparazione = tempo_preparazione
        self.ingredienti = ingredienti
        self.difficolta = difficolta

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_tempo_preparazione(self):
        return self.tempo_preparazione

    def set_tempo_preparazione(self, tempo_preparazione):
        self.tempo_preparazione = tempo_preparazione

    def get_ingredienti(self):
        return self.ingredienti

    def set_ingredienti(self, ingredienti):
        self.ingredienti = ingredienti

    def get_difficolta(self):
        return self.difficolta

    def set_difficolta(self, difficolta):
        self.difficolta = difficolta

    def aggiungi_ingrediente(self, ingrediente):
        self.ingredienti.append(ingrediente)

    def calcola_tempo_totale(self, ricette):
        return sum(ricetta.get_tempo_preparazione() for ricetta in ricette)

    def __str__(self):
        return f"ricetta: {self.nome}, tempo: {self.tempo_preparazione} min, difficoltà: {self.difficolta}, ingredienti: {', '.join(self.ingredienti)}"


class Primo(Ricetta):
    def __init__(self, nome, tempo_preparazione, ingredienti, difficolta, tipo_pasta, sugo):
        super().__init__(nome, tempo_preparazione, ingredienti, difficolta)
        self.tipo_pasta = tipo_pasta
        self.sugo = sugo

    def get_tipo_pasta(self):
        return self.tipo_pasta

    def set_tipo_pasta(self, tipo_pasta):
        self.tipo_pasta = tipo_pasta

    def get_sugo(self):
        return self.sugo

    def set_sugo(self, sugo):
        self.sugo = sugo

    def __str__(self):
        return super().__str__() + f", tipo pasta: {self.tipo_pasta}, sugo: {self.sugo}"


class Secondo(Ricetta):
    def __init__(self, nome, tempo_preparazione, ingredienti, difficolta, tipo_carne, cottura):
        super().__init__(nome, tempo_preparazione, ingredienti, difficolta)
        self.tipo_carne = tipo_carne
        self.cottura = cottura

    def get_tipo_carne(self):
        return self.tipo_carne

    def set_tipo_carne(self, tipo_carne):
        self.tipo_carne = tipo_carne

    def get_cottura(self):
        return self.cottura

    def set_cottura(self, cottura):
        self.cottura = cottura

    def __str__(self):
        return super().__str__() + f", Tipo Carne: {self.tipo_carne}, Cottura: {self.cottura}"


class Dolce(Ricetta):
    def __init__(self, nome, tempo_preparazione, ingredienti, difficolta, zucchero, tipo_dolce):
        super().__init__(nome, tempo_preparazione, ingredienti, difficolta)
        self.zucchero = zucchero
        self.tipo_dolce = tipo_dolce

    def get_zucchero(self):
        return self.zucchero

    def set_zucchero(self, zucchero):
        self.zucchero = zucchero

    def get_tipo_dolce(self):
        return self.tipo_dolce

    def set_tipo_dolce(self, tipo_dolce):
        self.tipo_dolce = tipo_dolce

    def __str__(self):
        return super().__str__() + f", Zucchero: {self.zucchero}, Tipo Dolce: {self.tipo_dolce}"


def verifica_ingredienti(ricette, ingredienti_disponibili):
    ricette_possibili = []
    for ricetta in ricette:
        if all(ingrediente in ingredienti_disponibili for ingrediente in ricetta.get_ingredienti()):
            ricette_possibili.append(ricetta)
    return ricette_possibili


def stampa_ricette(ricette):
    for ricetta in ricette:
        print(ricetta)