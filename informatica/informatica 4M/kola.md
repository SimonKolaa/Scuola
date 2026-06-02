### Istruzioni

1. Consegnare un file cognome.md
2. Salvare il file periodicamente sul disco D: (se il computer si spegne il file rimane)

### Sistema di controllo qualità abbigliamento

L'azienda necessita di un sistema per gestire il controllo qualità dei capi di abbigliamento ricevuti dai fornitori. Ogni fornitore invia delle commesse contenenti diversi capi di abbigliamento che devono essere controllati. I capi appartengono a diversi modelli, ognuno dei quali è prodotto da una specifica marca.

Il personale addetto al controllo qualità esamina i capi e compila delle schede di controllo, una per ogni modello presente nella commessa. Durante l'ispezione vengono verificate eventuali problematiche come macchie, scuciture o buchi, annotando tutte le informazioni rilevanti insieme alla data del controllo.

Ogni capo ha caratteristiche specifiche come taglia e colore, ed è importante mantenere traccia della sua appartenenza sia al modello che alla commessa originale. Le schede di controllo vengono associate al personale che ha effettuato l'ispezione, permettendo così di tracciare chi ha svolto quali controlli.

I fornitori sono identificati attraverso la loro ragione sociale, partita IVA e indirizzo, e possono inviare multiple commesse nel tempo.



```mermaid
classDiagram

 class Fornitore {
    +List[Commessa] commesse
    +str nome
    +int partita_iva
    +str indirizzo
    +getNome() str
    }

class Personale {
    +List[SchedaControllo] schedecontrollo
    +List[Capo] capi
    +str membri
    +str id
    +str tipo
    + esamina_capo()
    + compila_scheda_controllo()
     }

class SchedaControllo {
    +List[Personale] personale
    +List[Modello] modelli
    +str tipo_ispezione
    +str qualita
    +str macchie
    +str scuciture
    +str buchi
    + informazioni_rilevate(data_controllo: str) str
      }


class Capo {
    +List[Modello] modelli
    +Personale personale
    +Commessa commesse
    +str taglia
    +str colore
    +str modello
    +str marca
    +appartenenza(modello: str, commessa: str) str
    }

class Commessa {
    +List[Capo] capi
    +Fornitore fornitori
    +int quantita
    +str id
    +str tipo
    +str modello
    }

class Modello {
    +Capo capi
    +SchedaControllo schedacontrollo
    +str materiale
    +int taglia
    +str colore
    +str id


}

Fornitore "1" -- "*" Commessa : invia
Personale "1" -- "*" Capo : esamina
SchedaControllo "*" -- "*" Personale : associate
Commessa "1" -- "*" Capo: contengono
Capo "1" -- "*" Modello: appartengono
SchedaControllo "1" -- "1" Modello: appartiene

%%note
%% capo inteso come vestito
%% - La classe con cardinalità "1" avrà una lista degli oggetti della classe con cardinalità "N".
%%- La classe con cardinalità "N" avrà un riferimento singolo all'oggetto della classe con cardinalità "1".
