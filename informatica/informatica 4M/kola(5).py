import math

class VeicoloSpaziale:
    numero_veicoli = 0

    def __init__(self, nome, velocita_massima, massa, posizione):
        self._nome = nome
        self._velocita_massima = velocita_massima
        self._massa = massa
        self._posizione = posizione
        VeicoloSpaziale.numero_veicoli += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value

    @property
    def velocita_massima(self):
        return self._velocita_massima

    @velocita_massima.setter
    def velocita_massima(self, value):
        self._velocita_massima = value

    @property
    def massa(self):
        return self._massa

    @massa.setter
    def massa(self, value):
        self._massa = value

    @property
    def posizione(self):
        return self._posizione

    @posizione.setter
    def posizione(self, value):
        self._posizione = value

    def __str__(self):
        return f"Veicolo: {self._nome} - Velocità Massima: {self._velocita_massima} km/s - Massa: {self._massa} kg"

    def calcola_tempo_comunicazione(self, altro_veicolo):
        distanza = math.sqrt(
            (self._posizione[0] - altro_veicolo.posizione[0]) ** 2 +
            (self._posizione[1] - altro_veicolo.posizione[1]) ** 2 +
            (self._posizione[2] - altro_veicolo.posizione[2]) ** 2
        )
        tempo = distanza / 299792
        return tempo

    @staticmethod
    def veicoli_totali():
        return VeicoloSpaziale.numero_veicoli


class Sonda(VeicoloSpaziale):
    def __init__(self, nome, velocita_massima, massa, posizione, tipo_missione, energia, consumo_energia):
        super().__init__(nome, velocita_massima, massa, posizione)
        self._tipo_missione = tipo_missione
        self._energia = energia
        self._consumo_energia = consumo_energia

    @property
    def tipo_missione(self):
        return self._tipo_missione

    @tipo_missione.setter
    def tipo_missione(self, value):
        self._tipo_missione = value

    @property
    def energia(self):
        return self._energia

    @energia.setter
    def energia(self, value):
        self._energia = value

    @property
    def consumo_energia(self):
        return self._consumo_energia

    @consumo_energia.setter
    def consumo_energia(self, value):
        self._consumo_energia = value

    def __str__(self):
        return super().__str__() + f" - missione: {self._tipo_missione} - energia: {self._energia} MJ/h"

    def simula_missione(self, durata):
        consumo = self._consumo_energia * durata
        if consumo <= self._energia:
            self._energia -= consumo
            return True
        else:
            return False


class Astronave(VeicoloSpaziale):
    def __init__(self, nome, velocita_massima, massa, posizione, numero_equipaggio, carburante, consumo_carburante):
        super().__init__(nome, velocita_massima, massa, posizione)
        self._numero_equipaggio = numero_equipaggio
        self._carburante = carburante
        self._consumo_carburante = consumo_carburante
        
        @property
        def numero_equipaggio(self):
            return self.numero_equipaggio
        
        @numero_equipaggio.setter
        def numero_equipaggio(self, value):
            self.numero_equipaggio = value
            
        @property
        def carburante(self):
           return self.carburante
       
        @carburante.setter
        def carburante(self, value):
            self.carburante = value
            
        @property
        def consumo_carburante(self, value):
            self._consumo_carburante = value
            
        @consumo_carburante.setter
        def consumo_carburante(self, value):
            self.consumo_carburante = value
        
        def __str__(self):
            return super().__str__() + f" - numero_equipaggio: {self._numero_equipaggio} - carburante: {self._consumo_carburante} tonnellate/km"

    def puo_raggiungere(self, distanza):
        carburante_necessario = self._carburantenecessario * distanza
        if carburante_necessario <= self._carburante:
            return True
        else:
            return False
        
    class StazioneOrbitante(VeicoloSpaziale):
        def __init__(self, nome, moduli, capacita_aggancio):
            super().__init__(nome)
            self._moduli = moduli
            self._capacita_aggancio = capacita_aggancio  
            self._veicoli_agganciati = []  

    
    @property
    def moduli(self):
        return self._moduli

    @moduli.setter
    def moduli(self, moduli):
        self._moduli = moduli

    @property
    def capacita_aggancio(self):
        return self._capacita_aggancio

    @capacita_aggancio.setter
    def capacita_aggancio(self, capacita):
        self._capacita_aggancio = capacita

    @property
    def veicoli_agganciati(self):
        return self._veicoli_agganciati

    def __str__(self):
        moduli_str = (self._moduli)
        veicoli_str =([veicolo.nome for veicolo in self._veicoli_agganciati])
        return f'Stazione: {self.nome}, Moduli: [{moduli_str}], Veicoli agganciati: [{veicoli_str}]'

    def aggancia_veicolo(self, veicolo):
        if len(self._veicoli_agganciati) < self._capacita_aggancio:
            self._veicoli_agganciati.append(veicolo)
            return True  
        return False  

    def sgancia_veicolo(self, veicolo):
        if veicolo in self._veicoli_agganciati:
            self._veicoli_agganciati.remove(veicolo)
            return True  
        return False  

    def elenca_veicoli_agganciati(self):
        return [veicolo.nome for veicolo in self._veicoli_agganciati]

