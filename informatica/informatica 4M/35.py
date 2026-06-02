import os
import datetime
from datetime import datetime
from enum import Enum


class TipoStrumento(Enum):
    BATTERIA = "Batteria"
    CHITARRA = "Chitarra"
    BASSO = "Basso"

class TipoEffetto(Enum):
    RIVERBERO = "Riverbero"
    DISTORSIONE = "Distorsione"
    DELAY = "Delay"

class Utente:
    def __init__(self, id: str, nome: str, email: str):
        self.id = id
        self.nome = nome
        self.email = email
        self.progetti = []

    def crea_progetto(self, titolo: str, genere_musicale: str, id_progetto: str):
        progetto = ProgettoMusicale(titolo, id_progetto, genere_musicale)
        self.progetti.append(progetto)
        return progetto
    
class ProgettoMusicale:
    def __init__(self, titolo, id_progetto, genere_musicale: str):
        self.id_progetto = id_progetto
        self.titolo = titolo
        self.data_creazione = datetime.now()
        self.genere_musicale = genere_musicale 
        self.tracce = []

    def aggiungi_traccia(self, nome: str, durata: int = 0, volume: int = 50, sequenza_note: str = "", strumento_utilizato: str = ""):
        traccia = TracciaAudio(nome, durata, volume, sequenza_note, strumento_utilizato)
        self.tracce.append(traccia)
        return traccia

class TracciaAudio:
    def __init__(self, nome, durata, volume, sequenza_note, strumento_utilizato: str):
        self.nome = nome
        self.durata = durata
        self.volume = volume
        self.strumento_utilizato = strumento_utilizato
        self.sequenza_note = sequenza_note
        self.effetti = []
        self.sequenza_note 

    def modifica_volume(self, volume: int):
        self.volume += volume

    def aggiungi_strumento(self, strumento_utilizato):
        self.strumento_utilizato = strumento_utilizato

    def applica_effetto(self, effetto):
        self.effetti.append(effetto)

    def rimuovi_effetto(self, effetto):
            if effetto in self.effetti:
                self.effetti.remove(effetto)

    def imposta_sequenza_note(self, sequenza_note: str):
        self.sequenza_note = sequenza_note

class StrumentoVirtuale:
    def __init__(self,id,nome, tipo: str):
        self.id = id
        self.nome = nome
        self.tipo = tipo

def suona_nota(self, nota: str, durata: float):
        print(f"Suonando {nota} per {durata} secondi con {self.nome}")

class EffettoAudio:
    def __init__(self, id, nome, tipo):
        self.id = id
        self.nome = nome
        self.tipo = tipo

def main():
    utente = Utente("1", "Luca Santini", "santiniluca@hotmail.com")
    progetto = utente.crea_progetto("diabete freestyle", "trap", "1")  
    
    traccia1 = progetto.aggiungi_traccia("Traccia 1", durata = 20, volume = 10)
    traccia1.durata = 180
    traccia1.volume = 50
    traccia1.sequenza_note = "C D E F G A B"
    traccia1.strumento_utilizato = "Chitarra"
    
    # def aggiungi_traccia(self, nome: str, durata: int = 0, volume: int = 50, sequenza_note: str = "", strumento_utilizato: str = ""):
    traccia2 = progetto.aggiungi_traccia(nome="Traccia 2", durata = 50, volume = 30)
    # traccia2.durata = 200
    # traccia2.volume = 60
    traccia2.sequenza_note = "A B C D E F G"
    traccia2.strumento_utilizato = "Pianoforte"
    
    effetto1 = EffettoAudio("1", "Riverbero", "Spaziale")
    traccia1.applica_effetto(effetto1)
    
    effetto2 = EffettoAudio("2", "Distorsione", "Elettrico")
    traccia2.applica_effetto(effetto2)
    
    print(f"Utente: {utente.nome} ({utente.email})")
    print(f"Progetto: {progetto.titolo} - Genere: {progetto.genere_musicale}")
    print("Tracce:")
    for traccia in progetto.tracce:
        print(f"  Nome: {traccia.nome}, Durata: {traccia.durata}s, Volume: {traccia.volume}, Strumento: {traccia.strumento_utilizato}")
        print(f"  Sequenza Note: {traccia.sequenza_note}")
        print(f"  Effetti: {[effetto.nome for effetto in traccia.effetti]}")

if __name__ == "__main__":
    main()

