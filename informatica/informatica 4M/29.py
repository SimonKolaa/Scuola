from typing import List, Dict
from dataclasses import dataclass
from enum import Enum

class TipoDispositivo(Enum):
    IRRIGATORE = "irrigatore"
    VENTILATORE = "ventilatore"
    LUCE = "luce"

class TipoZona(Enum):
    GIARDINO = "giardino"
    AIUOLA = "aiuola"

@dataclass
class Dispositivo:
    nome: str
    tipo: TipoDispositivo
    stato: bool = False
    
    def attiva(self) -> None:
        self.stato = True
        
    def disattiva(self) -> None:
        self.stato = False
        
    def verifica_stato(self) -> bool:
        return self.stato

@dataclass
class Zona:
    tipo: TipoZona
    posizione: str
    dispositivi: List[Dispositivo]
    temperatura: float = 25.0
    umidita: float = 70.0
    qualita_aria: float = 80.0
    
    def monitora_parametri(self) -> Dict:
        return {
            "temperatura": self.temperatura,
            "umidita": self.umidita,
            "qualita_aria": self.qualita_aria
        }
    
    def gestisci_dispositivi(self) -> None:
        for dispositivo in self.dispositivi:
            if dispositivo.tipo == TipoDispositivo.VENTILATORE:
                if self.temperatura > 30 or self.qualita_aria < 40:
                    dispositivo.attiva()
                else:
                    dispositivo.disattiva()
            elif dispositivo.tipo == TipoDispositivo.IRRIGATORE:
                if self.umidita < 60:
                    dispositivo.attiva()
                else:
                    dispositivo.disattiva()

class Parco:
    def __init__(self, nome: str, superficie: float):
        self.nome = nome
        self.superficie = superficie
        self.zone: List[Zona] = []
        
    def aggiungi_zona(self, zona: Zona) -> None:
        self.zone.append(zona)
        
    def monitora_parametri(self) -> Dict:
        return {zona.posizione: zona.monitora_parametri() for zona in self.zone}
    
    def attiva_controllo_automatico(self) -> None:
        for zona in self.zone:
            zona.gestisci_dispositivi()