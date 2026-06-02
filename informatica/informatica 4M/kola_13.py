class Casa:
    def __init__(self, indirizzo, proprietario):
        self.indirizzo = indirizzo
        self.proprietario = proprietario
        self.stanze = []

    def get_indirizzo(self):
        return self.indirizzo

    def set_indirizzo(self, indirizzo):
        self.indirizzo = indirizzo

    def get_proprietario(self):
        return self.proprietario

    def set_proprietario(self, proprietario):
        self.proprietario = proprietario

    def aggiungi_stanza(self, stanza):
        if isinstance(stanza, Stanza):
            self.stanze.append(stanza)

    def get_stanze(self):
        return self.stanze
    
    def stampa_stanze(self):
        for stanza in self.stanze:
            print(f"{stanza.get_nome()} ({stanza.get_superficie()} mq)")


class Stanza:
    def __init__(self, nome, superficie):
        self.nome = nome
        self.superficie = superficie

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_superficie(self):
        return self.superficie

    def set_superficie(self, superficie):
        self.superficie = superficie
        
        
    
casa = Casa("Via Roma 1", "Mario Rossi")


stanza1 = Stanza("cucina", 20)
stanza2 = Stanza("soggiorno", 30)
stanza3 = Stanza("camera da letto", 25)


casa.aggiungi_stanza(stanza1)
casa.aggiungi_stanza(stanza2)
casa.aggiungi_stanza(stanza3)

print(f"la casa in {casa.get_indirizzo()} di {casa.get_proprietario()} ha le seguenti stanze:")
for stanza in casa.get_stanze():
    print(f"- {stanza.get_nome()} di {stanza.get_superficie()} mq")