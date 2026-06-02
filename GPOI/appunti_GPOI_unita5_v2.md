# Appunti GPOI – Unità 5: Il Project Management nei Progetti Informatici e TLC
> Libro: *Nuova Gestione del Progetto e Organizzazione d'Impresa* – Hoepli | pp. 195–269

---

## Lezione 1 – I Progetti Informatici (p. 196)

### Generalità
I progetti informatici rientrano nella definizione classica di progetto, ma si differenziano per la **"strana natura del prodotto"**, cioè il software. Il fattore unico che li distingue è la necessità di **definire (e "inventare") un algoritmo risolutivo** del quale è difficile stimare il tempo di realizzazione, specie in situazioni di innovazione tecnologica.

Richiedono due tipologie di competenze:
1. **Top-down**: a partire dagli obiettivi del progetto li scompone in sotto-obiettivi, individua e formalizza le fasi e dettaglia le singole attività
2. **Bottom-up**: parte dalle attività, individua le risorse necessarie, valuta tempi e costi e le aggrega in un progetto

### Tipologie di progetti informatici
Un progetto informatico produce un **prodotto software** sviluppato in due circostanze:
- **Software ad hoc**: costruito da zero su richiesta di un cliente specifico (committente)
- **Prodotto pacchettizzato (COTS – Commercial Off The Shelf)**: soddisfa necessità standard per un gruppo di utenti (es. office automation, gestionale, app smartphone)

**Quattro categorie di progetti informatici:**
1. **Commerciali**: nascono su richiesta di un cliente, orientati a fornitura di prodotti/servizi
2. **Di innovazione e investimento**: necessari a seguito di cambiamenti tecnologici (prodotti, processi, mercati)
3. **Di miglioramento gestionale**: informatizzazione di base, diffusione di servizi (automazione ufficio, email, intranet) oppure installazione di sistemi applicativi su larga scala
4. **Di riorganizzazione aziendale**: realizzazione/reingegnerizzazione di sistemi applicativi, infrastrutture, outsourcing

> Durata tipica: poche settimane → decine di mesi. Oltre i 3 anni si parla di **programmi di sviluppo**.

### La "pianificazione" del progetto
Un progetto è un insieme di attività ordinate dotate di **durata e costo**, sistemate nel tempo. I tre elementi costituenti sono:
1. **Obiettivo**
2. **Tempi**
3. **Costi**

### La crisi del software degli anni Ottanta
Negli anni '80 si manifestò la prima vera **"crisi del software"**: l'evoluzione esponenziale dell'hardware e la riduzione dei suoi costi resero sproporzionati i costi di sviluppo e manutenzione del software. L'approccio "artigianale" portò al fallimento di molti progetti.

**Dati Government Accounting Office USA (1979) – 9 progetti:**
- 3,2 M$ per applicazioni **mai consegnate**
- 2 M$ per applicazioni consegnate ma **mai utilizzate**
- 1,3 M$ per sviluppi **abbandonati o rimodificati**
- 0,2 M$ per applicazioni **utilizzate solo dopo consistenti modifiche**
- Solo 0,1 M$ per applicazioni **effettivamente utilizzate** come consegnate

**Dati su 13.522 progetti:**
- 66% **fallivano** (nessun risultato utile)
- 82% **superavano i tempi** previsti
- 48% producevano sistemi **senza le funzioni richieste** dai clienti
- 55 miliardi di dollari di spreco in un anno (solo USA)

**Tre cause del fallimento:**
1. **Metodologie inefficaci** – carente formazione professionale in una disciplina giovane e poco formalizzata
2. **Complessità** – il software deve interagire con sistemi sociali/organizzativi aziendali o sistemi elettrici/meccanici nell'automazione industriale
3. **Natura del software** – non ha struttura regolare (funziona in certi casi e non in altri) e non ha requisiti stabili (cambiano per fattori esterni come leggi, o interni come nuovi prodotti/organizzazione)

### L'ingegneria del software
Nasce come risposta alla crisi. La programmazione è solo uno dei problemi: occorre aggiungere tecniche per stimare l'impegno, suddividere il lavoro, comunicare tra sviluppatori e committente, seguire l'evoluzione dei requisiti, valutare l'affidabilità.

**Definizione (Fritz Bauer):** *"L'istituzione e l'impiego di principi ingegneristici fondati, allo scopo di ottenere in modo economico software affidabile ed efficiente su macchine vere."*

Disciplina sia **metodologica** (studia metodi, teorie, strumenti) sia **empirica** (basata su esperienza e storia dei progetti).

**Problemi affrontati:**
- Metodi di analisi e progettazione
- Studio del processo di sviluppo
- Sviluppo degli strumenti di produzione
- Aspetti economici dei prodotti e processi
- Standardizzazione di processi e tecnologie

### Software engineer vs Programmatore

| | Programmatore | Software engineer |
|---|---|---|
| Lavoro | Individuale | Solo o in team |
| Ambito | Sviluppa un programma completo da specifiche | Progetta componenti da integrare in un prodotto |
| Visione | Limitata al codice | Ciclo di vita completo del prodotto |
| Termine | **Programming in the small** | **Programming in the large** |

### Conclusioni: il software è immaturo
Disciplina iniziata negli anni '60 → solo mezzo secolo di storia. Industria profondamente immatura. Statistiche attuali: 26% progetti riusciti, 46% in ritardo/con costi imprevisti/funzionalità inadeguate, 28% falliti.

---

## Lezione 2 – Il Processo di Produzione del Software (p. 204)

### Il prodotto software
Il software è una **creazione dell'intelletto** che include programmi, strutture dati, documentazione. Viene "sviluppato" (attività human intensive), non costruito come un prodotto industriale. Ogni progetto è diverso dal precedente → non si può industrializzare. Non si consuma ma viene continuamente manutenzionato.

### Il processo di produzione – tre macro-fasi

```
PROGETTO → SVILUPPO → MANUTENZIONE
```

#### Il progetto – due parti
**1. Preprogetto** (comune a tutti i modelli di sviluppo):
- Studio di fattibilità (o preanalisi): raccolta requisiti utente, definizione modelli (utente/funzionale/dati/tecnologico), prima valutazione rischi e costi, produzione documento di validazione
- Pianificazione: WBS, Gantt, PERT, individuazione milestone e deliverable

**2. Progetto vero e proprio (system design)**: dal preventivo, eventuale gara d'appalto, contratto, progettazione esecutiva, documentazione tecnica.

#### Lo sviluppo
Realizzazione del prodotto. Principale difficoltà: **coordinare molti sviluppatori in parallelo** rispettando i vincoli temporali.

#### La manutenzione – 4 tipi

| Tipo | % tempo | Descrizione |
|---|---|---|
| **Correttiva** | ~20% | Rimuove gli errori inevitabilmente presenti nel software |
| **Adattativa** | ~20% | Ritocchi per aggiunte alle specifiche o cambiamenti emersi in corso d'opera |
| **Perfettiva** | ~50% | La più consistente. **Migliorativa**: ottimizza funzionalità già presenti (operazioni lente, troppa memoria). **Evolutiva**: aggiunge nuovi requisiti funzionali secondari |
| **Preventiva** | residuo | Revisione del codice scritto "troppo in fretta" per migliorarne la strutturazione e facilitare il debugging futuro |

### I ruoli in un progetto

**Principali ruoli del cliente:**
- **Committente**: individua il fornitore, firma il contratto, gestisce le risorse economiche
- **Capo progetto (lato cliente)**: verifica obiettivi di qualità, costo, tempi
- **Sponsor**: responsabilità finale di proteggere il business; può interrompere il progetto in caso di perdite
- **Utenti di riferimento per i test**: verificano che si realizzi quanto ci si aspetta
- **Utenti finali**: chi utilizzerà il sistema
- **Specialisti di ambiente**: addetti CED, verificano l'integrazione con i sistemi esistenti

**Principali ruoli del fornitore:**
- **Responsabile commerciale**: cura l'offerta e il contratto
- **Supervisore**: responsabile delle risorse umane/strumentali su più progetti
- **Project manager**: responsabile degli obiettivi economici e della soddisfazione del cliente
- **Analisti programmatori**: sviluppo (web designer, DBA, analista, programmatore...)
- **Specialisti**: compiti tecnici di elevata difficoltà
- **Personale di supporto**: formazione, data entry, assistenza

### La gara d'appalto
La modalità più comune per scegliere il fornitore. **L'unica modalità con cui la PA può assegnare un lavoro** (= gara formale, disciplinata dal diritto amministrativo).

**Cinque fasi:**
1. **Pubblicazione del bando**: committente comunica l'intenzione con descrizione sommaria
2. **Preparazione e invio del capitolato**: documento dettagliato (anche centinaia di pagine) con specifiche, aspettative, termini di consegna, modalità offerte
3. **Preparazione e invio offerte**: i fornitori preparano preventivo + relazione tecnica
4. **Esame offerte e individuazione vincitore**: commissione con "griglia di confronto" → graduatoria
5. **Firma del contratto**: clausole, impegni economici/temporali, eventuali penali

### Conduzione dei progetti – 3 modalità

| Tipo | Caratteristiche |
|---|---|
| **Chiavi in mano** | Capitolato dettagliatissimo; progetti noti senza rischio; il fornitore gestisce tutto; rispetta tempi/costi ma **a scapito della qualità** |
| **Responsabilità condivisa** | Caso più diffuso; entrambe le parti attive; **migliori garanzie di qualità** ma spesso non rispetta tempi e costi |
| **Body rental** | Per piccole realizzazioni a basso costo; **completa responsabilità del cliente** che deve avere le competenze interne |

---

## Lezione 3 – Preprogetto: Fattibilità e Analisi dei Requisiti (p. 212)

### Studio di fattibilità
Strumento che riduce l'incertezza e i rischi del progetto. Permette di valutare gli obiettivi reali a fronte dei costi richiesti. Non deve essere considerato "perdita di tempo".

**Cinque aspetti analizzati:**
1. **Tecnico**: la tecnologia necessaria esiste sul mercato?
2. **Organizzativo**: il nuovo progetto si integra con la struttura aziendale esistente?
3. **Motivazionale**: il sistema è "desiderato" dai futuri utilizzatori?
4. **Economico**: analisi costi/benefici → i ritorni giustificano le risorse?
5. **Temporale**: realizzabile entro i tempi accettabili?

**Due sotto-fasi:**
1. Raccolta e analisi dei requisiti dell'utente (descrizione ad alto livello, prima stima dei costi, documento da validare col cliente)
2. Studio di fattibilità e valutazione dei costi (definizione specifiche, scomposizione del progetto, valutazione costi/tempi)

### Analisi dei requisiti nel preprogetto
1. **Analisi del problema**: cosa deve fare il sistema? Necessità degli utenti, ambiente operativo, condizioni di mercato
2. **Definizione delle funzionalità**, operatività, vincoli interni/esterni, prestazioni richieste
3. **Redazione del documento SRS** (Software Requirement Specification): risponde a **"Cosa deve fare il sistema?"** – NON a come le funzioni saranno realizzate
4. **Convalida delle specifiche**: l'SRS viene rivisto col committente prima di procedere

> Un errore in questa fase comporta necessariamente molti errori nel sistema finale.

### Requisiti software e stakeholder

> **REQUISITO**: ogni informazione circa le funzionalità, i servizi, le modalità operative e di gestione del sistema da sviluppare.

> **STAKEHOLDER** (def. Edward Freeman): *"Tutte quelle persone o gruppi che influenzano e/o sono influenzati dalle attività di un'organizzazione, dai suoi prodotti o servizi e dai relativi risultati di performance."*

Problemi nella raccolta: gli stakeholder usano il proprio linguaggio tecnico non noto all'analista; il cliente ha poca esperienza nello sviluppo software; i fabbisogni variano ai diversi livelli aziendali; i requisiti possono essere in conflitto tra stakeholder diversi.

### Classificazione dei requisiti

**Per livello di dettaglio:**

| Tipo | Descrizione |
|---|---|
| **Requisiti utente** | Linguaggio naturale del cliente, alto livello, "requisiti aperti" (propongono soluzioni con alternative) |
| **Requisiti di sistema** | Linguaggio tecnico/formale, vincolanti, "requisiti chiusi", spesso noti solo al programmatore |

**Per tipo (4 categorie):**

| Tipo | Descrizione | Esempio (carta di credito del libro) |
|---|---|---|
| **Funzionali** | Funzionalità e servizi offerti; devono essere completi e coerenti | Effettuare pagamento; prelevare contanti; visualizzare saldo |
| **Non funzionali** | Modalità operative, ciclo di vita, normative; indicati spesso in modo generico → difficili da verificare; si misura il grado di soddisfacimento | Tempo risposta < 1 min; architettura X86; disponibile a portatori di handicap |
| **Di dominio** | Dipendenti dal dominio operativo (leggi, sicurezza, settore specifico) | Pagamenti entro limite mensile; codice segreto per autenticazione |
| **Di qualità – FURPS** | Functionality, Usability, Reliability, Performance, Supportability + vincoli (implementazione, interfacce, operazioni, packaging, legali) | — |

**Classificazione di Sommerville per i non funzionali (3 categorie):**
- **Di prodotto** (affidabilità, portabilità, efficienza, usabilità)
- **Organizzativi** (consegna, implementazione, standard)
- **Esterni** (interoperabilità, etici, legislativi)

### Verifica e validazione dei requisiti
La validazione si effettua durante **tutto il ciclo di sviluppo** e verifica: correttezza, completezza, coerenza, chiarezza, realismo, verificabilità, tracciabilità.

I requisiti non funzionali non si verificano in modo binario → si misura il **grado di soddisfacimento** con indicatori quantitativi (es. transazioni/sec, occupazione RAM, tempo di formazione, frequenza delle failure...).

### Problematiche: studio Standish Group su 8.000 progetti
16% successi, 53% fallimenti parziali, 31% fallimenti completi.

**Prime 8 cause di fallimento (5 su 8 legate ai requisiti):**

| Motivo | % |
|---|---|
| Requisiti incompleti | 13,1% |
| Mancato coinvolgimento dell'utente | 12,4% |
| Mancanza di risorse | 10,6% |
| Attese irrealistiche | 9,9% |
| Mancanza del supporto della direzione | 9,3% |
| Cambiamento dei requisiti | 8,7% |
| Mancanza di pianificazione | 8,1% |
| Non serviva più | 7,5% |

---

## Lezione 4 – Preprogetto: Raccolta e Verifica dei Requisiti (p. 224)

### Ingegneria dei requisiti – 4 attività
1. Raccolta dei requisiti
2. Analisi dei requisiti
3. Stesura della documentazione SRS
4. Verifica e approvazione dei requisiti

> Fred Brooks: *"The most difficult part of building a software system is to decide, precisely, what must be built."*

### Tipi di raccolta (3 situazioni)

| Tipo | Situazione | Descrizione |
|---|---|---|
| **Greenfield engineering** | Sviluppo da zero, nessun sistema preesistente | Fonte: committente e stakeholder; valutare anche prodotti disponibili sul mercato |
| **Re-engineering** | Sistema esistente da riprogettare (obsoleto o da estendere) | Analisi pregi/difetti, funzionalità da migrare, miglioramenti da integrare |
| **Interface engineering** | Impossibile sostituire il software esistente; si aggiorna solo l'interfaccia | Il sistema **legacy** resta intatto; si riprogettano solo le interfacce con i nuovi ambienti |

> **LEGACY**: termine che evidenzia il "valore aziendale" e la "provenienza dal passato". Non indica qualcosa di vecchio ma uno strumento su cui l'azienda fa affidamento anche in futuro.

### La fase di esplorazione
**Stakeholder engagement**: processo di dialogo interattivo. Coinvolgere = comunicare interattivamente, confrontarsi, dialogare, saper ascoltare. NON significa fare sondaggi o proporre soluzioni già decise. Gli stakeholder devono sentirsi parte del gruppo di lavoro.

### Tecniche di esplorazione

| Tecnica | Obiettivi | Vantaggi | Svantaggi |
|---|---|---|---|
| **Interviste individuali** | Esplorare aspetti specifici e punti di vista | L'intervistatore orienta l'intervista; **migliore fonte per i requisiti** | Richiedono molto tempo; gli intervistati potrebbero non esprimersi con franchezza |
| **Focus group** | Mettere a fuoco un argomento con diversi punti di vista | Fanno emergere aree di consenso e conflitto; soluzioni condivise | Richiedono esperienza; possono emergere figure dominanti che monopolizzano |
| **Osservazioni sul campo** | Comprendere il contesto reale | Danno consapevolezza sull'uso reale che le altre tecniche non danno | Difficili e onerose; osservano funzioni già presenti |
| **Suggerimenti spontanei** | Individuare necessità di miglioramento | Bassi costi; molto specifici | Carattere episodico |
| **Questionari** | Rispondere a domande specifiche (scala di Likert 1-5) | Raggiungono molte persone con poco sforzo | Vanno progettati con grande cura; tasso di risposta basso; attendibilità generalmente bassa |
| **Analisi concorrenza / best practice** | Individuare soluzioni migliori nel settore | Evitare di "reinventare la ruota" | Analisi costosa in tempo e risorse |
| **Scenari e casi d'uso** | Descrivere ogni singola operazione del sistema | Utilizzati anche in fase di collaudo | Gli intervistati spesso non descrivono le criticità |

**Strutturazione delle interviste:**
- **Non strutturate**: domande aperte, spunti per approfondimenti liberi
- **Strutturate**: domande specifiche a risposta chiusa; per ricavare dati statistici
- **Semistrutturate**: mix di aperte e chiuse *(via di mezzo preferita)*

### Problemi nella fase di esplorazione (4 tipologie)
1. **Ambito**: difficile trovare il livello di dettaglio giusto; rischio di tralasciare aspetti essenziali o sconfinare
2. **Comprensione**: linguaggio tecnico diverso; gli stakeholder non danno importanza agli aspetti ovvi; spesso non sono esperti IT → richieste irrealizzabili o costosissime
3. **Conflitto**: lo stesso requisito descritto in modo diverso (o incompatibile) da stakeholder diversi; i conflitti devono emergere e risolversi in questa fase
4. **Volatilità**: i requisiti cambiano per fattori **esterni** (evoluzione tecnologica, mercati, leggi) o **interni** (ricambio management, ristrutturazione, nuove strategie)

---

## Lezione 5 – Preprogetto: Pianificazione Temporale del Progetto (p. 233)

### Pianificare le attività
Obiettivo primario: **fissare gli obiettivi temporali**. Per ogni subcomponente: insieme delle attività, vincoli di precedenza, durata, costi.

Due vincoli invalicabili: **durata temporale complessiva** e **risorse globali disponibili**.

### Milestone e deliverable

> **DELIVERABLE**: risultato intermedio o finale di progetto (specifiche di un prodotto, servizio, output accessorio, relazione o documento di project management).

Le **milestone** hanno **durata zero** → sono eventi di controllo, non attività. I deliverable vengono tendenzialmente rilasciati in corrispondenza delle milestone.

Esempi di deliverable: piani di progetto, report di avanzamento, documentazione di progettazione, elenco issue, consuntivi.

### Aspetti della pianificazione

**Per aspetti generali (4 tipi):**
1. **Pianificazione tecnica**: scelte operative fondamentali (modello di sviluppo, linguaggi, ambienti, prodotti intermedi)
2. **Pianificazione della qualità**: requisiti di qualità, metodologie di controllo, punti di verifica, rischi
3. **Pianificazione organizzativa**: individua e associa al progetto le risorse umane, tecnologiche, finanziarie
4. **Pianificazione dei tempi e degli incarichi**: scomposizione in macrofasi → attività e sotto-attività → dipendenze temporali → tempi → costi

**Per obiettivi operativi:**
- **Pianificazione delle attività**: schedulazione, data inizio e fine di ogni attività
- **Pianificazione del personale**: "chi fa cosa e per quanto tempo"; time sheet; skill management
- **Pianificazione dei costi**: ripartizione budget alle singole attività; monitoraggio continuo

### La WBS – Work Breakdown Structure

> **WBS** (def. PMI): *"Un albero di attività orientate a un obiettivo, che organizza, definisce e visualizza graficamente tutto il lavoro che deve essere fatto per raggiungere gli scopi finali di un progetto."*

> **Work Package (WP)**: insieme di attività elementari con input, output, attività interne; a esso sono associabili risorse, tempi e responsabilità.

**Struttura ad albero gerarchica con codice:**
- Livello 0: Progetto
- Livello 1: Sotto-progetto
- Livello 2: Attività
- Livello 3: Sotto-attività (= Work Package)

**Regola del 100%**: la WBS deve includere il 100% del lavoro – tutto il necessario (interno, esterno, appaltato, inclusa la gestione del progetto). La somma a ogni livello deve sempre essere 100%.

**Per ogni WP si definisce:**
- Durata in tempo solare (data inizio e fine – elapsed time)
- Durata in tempo/persona (giorni/uomo)
- Obiettivi da conseguire
- Attività (task) e sotto-attività (subtask)
- Deliverable
- Milestone

**Formule:**
```
durata = impegno / numero_persone
durata = impegno / produttività_standard
```
L'impegno si ricava dalla stima dei **function point (FP)** → convertiti in **LOC (Lines of Code)** → divisi per la produttività standard del programmatore.

**Due passi preliminari per definire la WBS:**
1. Identificazione dei deliverable
2. Identificazione dei componenti dei deliverable e delle attività per raggiungerli

**Le attività WBS devono essere:** significative, descrivibili in termini tangibili, misurabili, controllabili, gestibili (durata breve).

### Logiche di disaggregazione

| Logica | Descrizione |
|---|---|
| **Per parti** | Decomposizione dell'output nelle sue parti componenti (come distinta base) |
| **Per funzioni** | Decomposizione secondo le funzionalità da svolgere |
| **Per obiettivi** | Decomposizione secondo le prestazioni (es. test di tutte le prestazioni) |
| **Per fasi** | Decomposizione secondo la sequenza delle fasi (es. progettazione separata da test) |
| **Per rilasci progressivi** | Decomposizione identificando prototipazioni successive |

### Il Gantt
Strumento **puramente grafico** con barre orizzontali proporzionali alla durata delle attività. Asse Y = attività; asse X = tempo. Le milestone sono indicate con simboli (es. triangoli).

**Punti per ogni attività:**
- **ES** (Earliest Startpoint), **EE** (Earliest Endpoint = ES + D)
- **LS** (Latest Startpoint), **LE** (Latest Endpoint) → calcolati a ritroso
- **TA** (Total Amortization) = tempo di riserva = LS – ES

Le attività senza TA sono **critiche**.

**Vantaggi**: mostra informazioni complesse a colpo d'occhio; facile da leggere anche per non tecnici.

**Limiti**: *"Il diagramma di Gantt non spiega le relazioni di precedenza tra le attività."* (citazione diretta del libro). Con molte attività le frecce diventano illeggibili → non individua il cammino critico.

### Le tecniche reticolari
Grafi in cui le attività sono rappresentate con frecce e le durate riportate su di esse. Permettono di individuare il **cammino critico** (cammino più lungo tra inizio e fine del progetto):
- Attività sul cammino critico → **critiche**: ogni giorno di ritardo = un giorno di ritardo per tutto il progetto
- Attività fuori dal cammino critico → **non critiche**: hanno margini (slack/float)

**Due strumenti:**
- **CPM** (Critical Path Method): valuta la miglior allocazione delle risorse per ridurre il cammino critico; usato per **processi più conosciuti**
- **PERT** (Program Evaluation Review Technique): valuta le conseguenze dei ritardi; usato per **progetti più incerti e complessi**

### Il PERT – three point estimation
Usa **tre stime** del tempo per ogni attività:
- **To** = tempo ottimistico
- **Tm** = tempo modale (più probabile)
- **Tp** = tempo pessimistico

**Formula:**
```
Tempo previsto = (To + 4·Tm + Tp) / 6
```

Il PERT è un **grafo unidirezionale aciclico** che descrive il progetto nella sua interezza; evidenzia le precedenze e la durata di ogni attività; permette di calcolare il **cammino critico** su cui si applica il CPM.

**Strumenti software**: GanttProject (gratuito/open source); Microsoft Project (a pagamento).

### Schedulazione e bilanciamento dei vincoli
Tre parametri in gioco: **tempi, costi, risorse**. Qualunque azione su uno causa variazione degli altri due.

Un progetto può essere vincolato dal tempo (data consegna inderogabile) o dai costi (budget fisso).

Se non è possibile ottenere nuove risorse, due soluzioni:
1. **Taglio delle funzioni**: concordato con il committente; si rimandano funzionalità a un aggiornamento successivo
2. **Indebolimento delle specifiche**: operazione rischiosa spesso fatta "di nascosto"; si riducono le prestazioni al "minimo essenziale"

> **Legge di Mealy**: *"Se un progetto ritarda, aggiungere una nuova persona al gruppo di lavoro consuma più risorse di quante ne produca."*
> → L'aggiunta di risorse va fatta all'inizio di una nuova fase, non in corso d'opera.

---

## Lezione 6 – La Documentazione del Progetto e il Controllo della Qualità (p. 252)

### Documenti per fase

| Fase | Deliverable |
|---|---|
| **Avvio** | Project charter |
| **Pianificazione** | WBS, diagramma di Gantt |
| **Esecuzione** | Convalida dei deliverable |
| **Monitoraggio e controllo** | Project status, Registro delle issue |
| **Chiusura** | Output finale con indicatori di performance, Lesson learned |

### Project Charter (avvio)
Documento formale che stabilisce il patto generale di progetto e **autorizza ufficialmente l'avvio**, attribuendo al PM l'autorità di disporre delle risorse. Pubblicato dallo **sponsor**.

**5 sezioni principali:**
1. **Ambito**: attività, prodotti da realizzare, esclusioni, obiettivi, benefici attesi
2. **Organizzazione del progetto**: ruoli, stakeholder, cultura aziendale, struttura organizzativa, standard di settore
3. **Durata**: Gantt di massima con milestone e deliverable; eventuale PERT con cammino critico
4. **Budget**: piano dei costi con stima minima, media e massima
5. **Vincoli e rischi**: eventi aleatori negativi (rischi) o positivi (opportunità); valutazione pesata per voce di rischio (scala 1-5)

> In alcune metodologie chiamato **PID** (Project Initial Document).

### Project Status (monitoraggio)
Valuta lo stato del progetto mediante la **percentuale di completamento** delle attività. Include confronto pianificato vs. reale. Include trattazione sulle tecniche di controllo costi → metodologia dell'**earned value**.

Misure correttive in caso di ritardi: incremento ore lavorative, esternalizzazione attività, rinegoziazione scadenze.

### Registro delle issue (monitoraggio)
Per ogni issue: N° progressivo, descrizione, chi l'ha segnalata e quando, persona assegnata, soluzione proposta, effetto, stato. Può essere inserito nelle lesson learned.

### Documenti di chiusura
- Contratto e accettazione formale del cliente
- Documenti del progetto (piani, documentazione tecnica)
- Report sullo stato e problematiche
- Documentazione finanziaria
- **Lesson learned**: eredità del progetto, quanto si è appreso e come riutilizzarlo

> La documentazione di progetto rappresenta il **business case** e serve da caposaldo per il successo di tutti i progetti futuri.

### Pianificazione e controllo della qualità
I criteri di gestione della qualità sono definiti nel **piano di qualità (quality plan)** che riporta:
- Gli standard di qualità dei deliverable
- I ruoli e le responsabilità per la pianificazione e l'assicurazione della qualità

---

## Lezione 7 – Le Fasi nei Modelli di Sviluppo dei Progetti Informatici (p. 258)

### Ciclo di vita del software (SDLC) – Waterfall classico (7 fasi)
1. Raccolta requisiti → 2. Analisi → 3. Progettazione → 4. Implementazione → 5. Test → 6. Attivazione → 7. Manutenzione

### Modelli di sviluppo tradizionali

#### Build and Fix
Nessun processo formale. Si scrive, si prova, si corregge. Funziona solo per progetti piccolissimi, non scalabile.

#### Waterfall (p. 261)
Fasi sequenziali rigide: ognuna deve concludersi prima della successiva.

**Vantaggi**: semplice, documentato, prevedibile; adatto a requisiti stabili e team distribuiti.

**Svantaggi**: rigido; il cliente vede il prodotto solo alla fine; errori nei requisiti scoperti tardi costano moltissimo.

#### RAD – Rapid Application Development (p. 263)
Si crea rapidamente un prototipo da mostrare al cliente.
- **Throw-away**: il prototipo si butta, serve solo per chiarire i requisiti
- **Evolutivo**: il prototipo diventa gradualmente il prodotto finale

**Vantaggi**: cliente vede subito qualcosa; requisiti chiariti prima.
**Svantaggi**: rischio di consegnare un prototipo non rifinito.

#### Modello incrementale (p. 264)
Il sistema viene consegnato in incrementi successivi, ognuno aggiunge funzionalità.

**Vantaggi**: valore consegnato presto, rischi distribuiti.
**Svantaggi**: serve una buona architettura iniziale.

#### Modello a spirale – Boehm (p. 265)
Combina sviluppo incrementale con **gestione del rischio**. Ogni ciclo ha 4 quadranti:
1. Determinazione obiettivi e vincoli
2. Valutazione rischi e prototipazione
3. Sviluppo e test
4. Pianificazione del prossimo ciclo

**Vantaggi**: gestione esplicita dei rischi, flessibile.
**Svantaggi**: complesso, costoso.

#### Limiti dei modelli tradizionali (p. 266)
Falliscono quando i requisiti cambiano frequentemente, il dominio è nuovo, il cliente non sa cosa vuole, il mercato richiede rilasci rapidi.

### Sviluppo Agile (p. 267)
**Manifesto Agile** (2001) – 4 valori fondamentali:
1. **Individui e interazioni** > processi e strumenti
2. **Software funzionante** > documentazione estesa
3. **Collaborazione col cliente** > negoziazione contrattuale
4. **Rispondere al cambiamento** > seguire un piano

Definite **"leggere" (lightweight)** perché: minimizzano la documentazione, riducono i processi burocratici, usano team piccoli e auto-organizzati, si adattano al cambiamento.

#### XP – eXtreme Programming (p. 267)
- **Pair programming**: due programmatori sullo stesso codice
- **TDD**: si scrivono prima i test, poi il codice
- **Continuous Integration**: integrazione frequente del codice
- **Refactoring continuo**
- **Small releases**: rilasci piccoli e frequenti
- **Collective code ownership**: tutto il team è responsabile di tutto il codice

#### RUP – Rational Unified Process (p. 268)
4 fasi: **Inception** (avvio) → **Elaboration** (architettura/rischi) → **Construction** (sviluppo incrementale) → **Transition** (deployment/formazione). Basato su use case, usa UML. Ogni fase ha più iterazioni. Più adatto a grandi organizzazioni.

#### Altri modelli (p. 268)
- **Scrum**: sprint 2-4 settimane; ruoli (Product Owner, Scrum Master, Dev Team); cerimonie (Daily Standup, Sprint Review, Retrospective)
- **Kanban**: board To Do / In Progress / Done; nessun vincolo di sprint
- **DevOps**: integra sviluppo e operazioni; CI/CD; rilasci continui

### Confronto modelli

| Modello | Approccio | Punti di forza | Punti deboli |
|---|---|---|---|
| **Build & Fix** | Nessun processo | Veloce per micro-prototipi | Non scalabile, caotico |
| **Waterfall** | Sequenziale rigido | Semplice, documentato, prevedibile | Rigido; cliente vede il prodotto solo alla fine |
| **RAD** | Prototipazione rapida | Cliente vede subito qualcosa | Rischio di consegnare prototipo grezzo |
| **Incrementale** | Rilasci successivi | Valore consegnato presto | Serve buona architettura iniziale |
| **Spirale** | Iterativo + risk management | Gestione esplicita dei rischi | Complesso e costoso |
| **Agile/Scrum** | Iterativo, adattivo, leggero | Flessibile; cliente coinvolto; rilasci frequenti | Meno prevedibile su tempi/costi totali |

---

## Termini Chiave

| Termine | Significato |
|---|---|
| **SDLC** | Software Development Life Cycle |
| **WBS** | Work Breakdown Structure – scomposizione gerarchica del lavoro |
| **Work Package (WP)** | Unità elementare della WBS con risorse, tempi, responsabilità |
| **Milestone** | Evento di controllo, durata zero |
| **Deliverable** | Prodotto tangibile/documento consegnato a fine fase |
| **Gantt** | Diagramma a barre per pianificazione temporale |
| **PERT** | Tecnica reticolare con formula (To + 4Tm + Tp) / 6 |
| **CPM** | Critical Path Method – ottimizzazione allocazione risorse |
| **Cammino critico** | Cammino più lungo nel grafo → determina la durata minima del progetto |
| **TA** | Total Amortization – tempo di riserva (LS – ES) |
| **SRS** | Software Requirements Specification – "cosa deve fare il sistema" |
| **Project Charter** | Documento di avvio formale; autorizza il PM |
| **Issue log** | Registro dei problemi critici del progetto |
| **Lesson learned** | Eredità del progetto; base per progetti futuri |
| **Earned value** | Tecnica di controllo costi |
| **Stakeholder** | Tutti i soggetti che influenzano/sono influenzati dal progetto |
| **Software ad hoc** | Sviluppato da zero su richiesta di un cliente specifico |
| **COTS** | Commercial Off The Shelf – software pacchettizzato per il mercato |
| **Gara formale** | Unica modalità con cui la PA può assegnare un lavoro di sviluppo |
| **Capitolato** | Documento del committente con specifiche, aspettative, termini |
| **FURPS** | Functionality, Usability, Reliability, Performance, Supportability |
| **Legacy** | Sistema di valore ereditato dal passato su cui l'azienda fa affidamento |
| **Greenfield** | Sviluppo da zero senza sistemi preesistenti |
| **Re-engineering** | Riprogettazione di un sistema esistente obsoleto |
| **Interface engineering** | Aggiornamento della sola interfaccia mantenendo il legacy intatto |
| **Legge di Mealy** | Aggiungere persone a un progetto in ritardo consuma più risorse di quante ne produca |
| **TDD** | Test-Driven Development – prima i test, poi il codice |

---

## Ripasso Guidato – Domande e Risposte

### BASI DI PROJECT MANAGEMENT

**1. Che cosa significa approccio top-down nella gestione di un progetto?**
Dal libro: *"a partire dagli obiettivi del progetto li scompone in sotto-obiettivi individuando e formalizzando le fasi per raggiungerli e dettagliando le singole attività che devono essere svolte."* È il metodo usato nella WBS: si parte dal progetto intero e si disaggrega fino ai work package elementari.

**2. Che differenza c'è con l'approccio bottom-up?**
Dal libro: *"parte dalle attività, ne individua le risorse necessarie, valuta i tempi e i costi e le aggrega in un progetto."* Mentre il top-down scompone gli obiettivi, il bottom-up aggrega le stime dal basso verso l'alto.

**3. Che cosa sono le milestone e a cosa servono?**
Le milestone sono momenti in cui il PM e gli attori si riuniscono per analizzare lo stato di avanzamento e individuare azioni correttive. Hanno **durata zero** (sono eventi, non attività). Nel Gantt si indicano con simboli (es. triangoli). I deliverable vengono tendenzialmente rilasciati in corrispondenza delle milestone.

**4. Che cos'è un deliverable?**
Dal libro: *"Rappresenta un risultato intermedio o finale di progetto: le specifiche di un prodotto, di un servizio o di un output accessorio, ma anche una relazione o un documento di project management."* Esempi: piani di progetto, report di avanzamento, documentazione di progettazione, elenco issue, consuntivi.

**5. Chi è il committente e qual è il suo ruolo?**
Il committente (lato cliente) è il responsabile che individua il fornitore, firma il contratto, gestisce le risorse economiche e risponde del buon fine del progetto. Nel software pacchettizzato non esiste: è l'azienda stessa che investe dopo un'analisi di mercato.

---

### PROCESSO SOFTWARE

**1. Quali sono le macro-fasi del processo di sviluppo software? Descrivile.**
Il libro sintetizza in tre macro-fasi: **Progetto** (preprogetto + system design), **Sviluppo** (realizzazione con coding, test, avviamento), **Manutenzione** (dura tutta la vita del prodotto; classificata in correttiva, adattativa, perfettiva, preventiva).

**2. Che cosa si intende per preprogetto?**
La fase preliminare **comune a tutti i modelli di sviluppo**, che precede il progetto vero e proprio. È composta da: studio di fattibilità (raccolta requisiti, modelli, prima valutazione rischi/costi) e pianificazione del progetto (WBS, Gantt, PERT, milestone, deliverable).

**3. Che cos'è lo studio di fattibilità e quali aspetti analizza?**
Strumento che contribuisce a realizzare un sistema più efficiente ed efficace, diminuendo l'incertezza e i rischi. Analizza cinque aspetti: **tecnico** (la tecnologia esiste?), **organizzativo** (si integra con l'azienda?), **motivazionale** (gli utenti lo vogliono?), **economico** (analisi costi/benefici), **temporale** (realizzabile nei tempi accettabili?).

**4. Perché l'analisi dei requisiti è critica?**
Perché un errore in questa fase *"comporta necessariamente la presenza di molti errori nel sistema finale"* (citazione dal libro). Gli errori vengono scoperti solo nelle ultime fasi (collaudo, messa in opera), quando il costo di correzione è elevatissimo. Lo studio Standish Group documenta che i problemi legati ai requisiti rappresentano oltre il 50% delle cause principali di fallimento dei progetti.

---

### CRISI DEL SOFTWARE

**1. Che cos'è la crisi del software degli anni '80?**
Il fenomeno per cui l'evoluzione esponenziale dell'hardware e la riduzione dei suoi costi resero sproporzionati i costi di sviluppo e manutenzione del software. L'approccio artigianale portò a: 66% dei progetti falliti, 82% in ritardo, 48% senza le funzioni richieste, 55 miliardi di dollari di spreco annuo (solo USA).

**2. Quali sono le cause principali?**
Il libro individua tre cause: (1) **metodologie inefficaci** – carente formazione in una disciplina giovane; (2) **complessità** – il software deve interagire con sistemi sociali/organizzativi o elettrici/meccanici; (3) **natura del software** – non ha struttura regolare né requisiti stabili (cambiano per fattori esterni o interni).

---

### PIANIFICAZIONE E STRUMENTI

**1. Che cos'è la pianificazione di un progetto?**
La fase che ha come obiettivo la realizzazione dello schema di progetto con tutti gli eventi, le attività, le relazioni di precedenza e le durate. Comprende: WBS, stima risorse/costi, milestone, deliverable, Gantt, PERT, valutazione dei rischi. I due vincoli invalicabili sono la **durata temporale complessiva** e le **risorse globali disponibili**.

**2. Descrivi il diagramma di Gantt (struttura, elementi, vantaggi, limiti).**
Strumento puramente grafico. Asse Y = attività, asse X = tempo (giorni/settimane/mesi). Elementi: barre orizzontali proporzionali alla durata; simboli per le milestone; frecce per le precedenze; % di completamento; punti ES, EE, LS, LE, TA per ogni attività. Vantaggi: mostra informazioni complesse a colpo d'occhio; facile da leggere anche per non tecnici. Limiti: non spiega le relazioni di precedenza logiche; con molte attività le frecce diventano illeggibili; non individua il cammino critico.

**3. Il diagramma di Gantt cosa NON mostra chiaramente? Perché?**
Il libro afferma esplicitamente: *"Il diagramma di Gantt non spiega le relazioni di precedenza tra le attività."* Due attività in sequenza nel Gantt non implica necessariamente un vincolo logico (es. idraulico ed elettricista possono lavorare in parallelo ma sono messi in sequenza per indisponibilità). Per le precedenze effettive servono le frecce, ma su progetti complessi diventano illeggibili → si usano le **tecniche reticolari (PERT/CPM)**.

**4. A cosa serve il diagramma PERT?**
Il PERT è un grafo unidirezionale aciclico che: rappresenta le dipendenze logiche tra attività; calcola il **cammino critico**; usa tre stime del tempo con formula *(To + 4Tm + Tp) / 6*; calcola il float/TA delle attività non critiche. Viene usato per **progetti più incerti e complessi** rispetto al CPM.

**5. Che cos'è la WBS e perché è fondamentale?**
La WBS è la scomposizione gerarchica strutturale del lavoro in work package elementari, strutturata ad albero con codici gerarchici. Fondamentale perché: applica la regola del 100% (niente dimenticato, niente in eccesso); è la base per stimare tempi, costi e risorse; permette di assegnare responsabilità chiare; è il punto di partenza per Gantt e PERT.

---

### REQUISITI SOFTWARE

**1. Che cos'è un requisito software?**
Dal libro: *"Ogni informazione (ottenuta in qualsiasi modo) circa le funzionalità, i servizi, le modalità operative e di gestione del sistema da sviluppare."* Rappresenta una proprietà richiesta (obbligatoria) o auspicabile del prodotto.

**2. Classifica i requisiti per livello di dettaglio e per tipologia.**
**Per livello di dettaglio:** requisiti **utente** (linguaggio naturale del cliente, "aperti") e requisiti **di sistema** (linguaggio tecnico/formale, vincolanti, "chiusi").

**Per tipologia:** **funzionali** (funzionalità e servizi offerti; devono essere completi e coerenti), **non funzionali** (modalità operative, normative; difficili da verificare in modo binario → si misura il grado di soddisfacimento), **di dominio** (dipendenti dal settore operativo), **di qualità – FURPS** (Functionality, Usability, Reliability, Performance, Supportability).

**3. Differenza con esempi (dall'esempio del libro: carta di credito bancaria):**

| Tipo | Esempio carta di credito |
|---|---|
| **Funzionale** | Effettuare pagamento acquisti; prelevare contanti; visualizzare saldo ed estratto conto |
| **Non funzionale** | Tempo risposta < 1 min; sviluppato su architettura X86; disponibile a portatori di handicap; facilmente espandibile |
| **Di dominio** | Pagamenti entro limite massimo mensile; autenticazione tramite codice segreto memorizzato sulla carta |

**4. A quale domanda risponde il documento SRS?**
L'SRS risponde alla domanda: **"Cosa deve fare il sistema?"** – stabilisce le funzionalità senza interessarsi di *come* verranno realizzate. È la trasformazione dei requisiti in un documento formalizzato con specifiche tecniche e funzionali.

---

### MANUTENZIONE SOFTWARE

**1. Che cos'è la manutenzione del software?**
La fase che inizia con la consegna del prodotto e dura per tutta la vita del prodotto. Non è meno importante delle fasi precedenti. Statisticamente assorbe il 60-80% del costo totale di un sistema software.

**2. Quali sono le tipologie di manutenzione? (con percentuali del libro)**

| Tipo | % | Scopo |
|---|---|---|
| **Correttiva** | ~20% | Rimuovere gli errori inevitabilmente presenti nel software |
| **Adattativa** | ~20% | Aggiunte alle specifiche o cambiamenti emersi in corso d'opera |
| **Perfettiva** | ~50% | La più consistente: **migliorativa** (ottimizza funzionalità già presenti) + **evolutiva** (aggiunge nuovi requisiti funzionali secondari) |
| **Preventiva** | residuo | Revisione del codice per migliorarne la strutturazione e facilitare il debugging futuro |

**3. Quale tipo è il più frequente e complesso?**
La **manutenzione perfettiva** – stimata dal libro nel **50% degli interventi**. È la più consistente e complessa.

**4. Descrivi i tipi di manutenzione:**
- **Correttiva**: toglie gli errori inevitabilmente presenti in tutti i prodotti software. Es: correggere un bug di calcolo scoperto dai clienti dopo il rilascio.
- **Adattativa**: ritocchi per aggiunte alle specifiche o cambiamenti emersi. Es: adeguare il software a una nuova normativa; aggiornarlo per un nuovo OS.
- **Evolutiva**: aggiunge nuovi requisiti funzionali secondari. Es: il cliente chiede di aggiungere l'export in PDF al gestionale.

---

### MODELLI DI SVILUPPO

**1. Confronta i principali modelli di sviluppo software.**
(vedi tabella nella Lezione 7)

**2. Quali sono i punti di forza del modello Waterfall?**
Semplice, chiaro, facile da gestire; documentazione completa ad ogni fase; prevedibile; adatto a requisiti stabili e a team distribuiti; ottimo per progetti con requisiti legali o normativi.

**3. Caratteristiche delle metodologie agili. Perché si definiscono "leggere"?**
Si definiscono "leggere" perché minimizzano la documentazione formale (si produce solo ciò che è strettamente necessario), riducono i processi burocratici, usano team piccoli e auto-organizzati, si adattano al cambiamento invece di seguire rigidamente un piano. Lavorano in **iterazioni brevi** (sprint); fanno **rilasci frequenti** di software funzionante; coinvolgono il cliente continuamente.

**4. Qual è uno dei principali vantaggi delle metodologie agili?**
La **capacità di rispondere al cambiamento**: i requisiti possono cambiare tra uno sprint e l'altro senza mandare in crisi il progetto. Il cliente vede software funzionante dai primi sprint, può dare feedback reale (non su documenti astratti) e ridefinire le priorità. Questo riduce drasticamente il rischio di consegnare un sistema inutile – il problema classico del waterfall, dove il cliente vede il prodotto solo alla fine.
