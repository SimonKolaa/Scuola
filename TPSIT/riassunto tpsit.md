# Riassunto Completo TPSIT - Interrogazione

---

## UDA 1 - SISTEMI DISTRIBUITI

### Definizioni Base

**Sistema Centralizzato**  
Dati e applicazioni risiedono su un unico nodo elaborativo (mainframe con terminali stupidi).

**Sistema Distribuito**  
Sistema in cui almeno una condizione è verificata:
- Elaborazione distribuita (applicazioni su più host collaboranti)
- Base di dati distribuita (dati su più host)

È un insieme di applicazioni logicamente indipendenti che collaborano attraverso un'infrastruttura comune.

**Sistema Parallelo vs Distribuito**  
- **Paralleli**: più processori eseguono lo stesso codice
- **Distribuiti**: più macchine indipendenti con programmi diversi

### Ruoli delle Applicazioni

| Ruolo | Descrizione |
|-------|-------------|
| **Client** | Utilizza servizi, IP dinamico, comunica solo con server |
| **Server** | Fornisce servizi, IP statico, sempre attivo e in ascolto |
| **Actor** | Assume sia ruolo client che server in base al contesto |

### Classificazione Sistemi Distribuiti

**Per destinazione d'uso:**
- **Calcolo**: cluster (computer omogenei) e grid (macchine eterogenee distribuite)
- **Informativi**: Web, sistemi legacy
- **Pervasivi**: sensori, domotica, wearable, PAN, reti wireless

**Per accoppiamento:**
- **Debole**: risorse poco interdipendenti (data center multinazionale)
- **Forte**: sistema fortemente integrato (banche, catene distribuzione)

### Benefici e Svantaggi

**Benefici:**
- Affidabilità (ridondanza)
- Trasparenza (sistema visto come unico)
- Scalabilità (espansione senza interruzioni)
- Tolleranza ai guasti
- Economicità
- Apertura (interoperabilità e portabilità)

**Svantaggi:**
- Maggiore complessità software
- Problemi sicurezza (dati in rete)
- Maggiore richiesta banda
- Necessità linguaggi e strumenti specifici

---

## UDA 1 - ARCHITETTURE HARDWARE

### Classificazione di Flynn

Framework per classificare architetture hardware basato su flusso istruzioni e dati.

| Tipo | Istruzioni | Dati | Descrizione |
|------|-----------|------|-------------|
| **SISD** | 1 | 1 | Computer tradizionale con singola CPU, esecuzione sequenziale |
| **SIMD** | 1 | Molti | Applicazioni grafiche, calcoli vettoriali e matriciali |
| **MISD** | Molti | 1 | Teoriche, non commercializzate, possibile uso in crittografia |
| **MIMD** | Molti | Molti | Memoria condivisa (multiprocessori) o privata (multicomputer) |

**MIMD - Due tipi:**
- **Memoria condivisa** (multiprocessori): comunicazione tramite variabili condivise, necessaria sincronizzazione
- **Memoria privata** (multicomputer): comunicazione tramite messaggi send/receive, include le LAN

### Cluster vs Grid

**Cluster**
- Nodi omogenei su stesso rack
- Rete ad alta velocità (>1Gbit/s)
- Stesso OS
- Architetture: gerarchica (Beowulf) o Single System Image (MOSIX)
- Corrisponde a MIMD a memoria privata

**Grid**
- Sistema decentralizzato
- Nodi eterogenei (hardware, software, rete diversi)
- Geograficamente distribuiti

### Sistemi Pervasivi

Nodi piccoli, mobili, wireless, parte di sistemi più grandi.

**Requisiti:**
- Adattamento contesto
- Composizione ad hoc
- Auto-configurazione
- Condivisione default

**Applicazioni:**
- Reti domestiche
- Domotica
- Wearable computing sanitario
- Reti sensori

---

## UDA 1 - ARCHITETTURE SOFTWARE

### Evoluzione

1. **Terminali Remoti**: mainframe + terminali stupidi (NON distribuito)
2. **Client-Server**: separazione tra richiedenti e fornitori servizi
3. **Web-Centric**: elaborazione su server, client solo interfaccia
4. **Cooperativa**: entità autonome con modello a componenti (OdP, CORBA)
5. **Completamente Distribuita**: entità paritetiche, servizi duplicati (RMI, DCOM)
6. **Microservizi**: componenti autonomi con API, database proprio per servizio

### Middleware

Software tra applicazioni e sistema operativo che garantisce interoperabilità su sistemi eterogenei.  
Basato su RPC o message passing.

---

## UDA 1 - CLIENT-SERVER E APPLICAZIONI WEB

### Tecnologie Web

| Tipo | Descrizione |
|------|-------------|
| **Client-side** | Elaborazione sul browser, codice visibile, non serve web server |
| **Server-side** | Elaborazione su web server, codice non visibile, serve URL |

**Linguaggi:** 
- Mark-up (documenti strutturati)
- Programmazione (sequenze istruzioni)

### Modello Client-Server

Insieme di server (gestiscono risorse) e client (richiedono accesso).  
*Nota: Si definiscono client/server i processi, non gli host.*

**Flusso:**
```
client invia richiesta → server riceve → server esegue (genera thread) → server risponde → client riceve
```

**Servizi tipici:** Telnet, HTTP, FTP, SMTP, IMAP

### Socket

Coppia `<IP:porta>` che identifica univocamente un processo.

**Nel server:**
- Socket di benvenuto (in ascolto)
- Socket dinamici (thread per ogni client, gestione concorrenza)

### Comunicazione

| Tipo | Descrizione |
|------|-------------|
| **Unicast** | Uno-a-uno, server risponde singolarmente (es. pagina web) |
| **Multicast** | Uno-a-molti, server trasmette contemporaneamente a gruppo (es. streaming) |

### Livelli e Strati

**Livelli (Tier) - Organizzazione fisica:**
- Front-end: interfaccia utente
- Middle tier: logica applicativa
- Back-end: gestione database

**Strati (Layer) - Organizzazione logica:**
- **Presentation Layer**: acquisizione/presentazione dati
- **Business Logic Layer**: logica elaborazione, relazioni tra entità
- **Resource Management Layer**: gestione dati persistenti

### Architetture Multi-Tier

| Tier | Descrizione |
|------|-------------|
| **1-Tier** | Mainframe con terminali (NON client-server) |
| **2-Tier** | Thin-client o thick-client. **Limite**: poco scalabile |
| **3-Tier** | Front + middle + back separati con middleware. **Vantaggi**: scalabilità, sicurezza. **Svantaggi**: tempi comunicazione, complessità |
| **N-Tier** | Numero variabile livelli per applicazioni complesse |

---

## UDA 1 - APPLICAZIONI DI RETE

### Protocolli Livello Applicazione

| Protocollo | Utilizzo |
|-----------|----------|
| **HTTP** | Navigazione web |
| **FTP** | Trasferimento file |
| **SMTP** | Invio email |
| **POP3** | Ricezione email |
| **DNS** | Risoluzione nomi |
| **SNMP** | Gestione rete |

### Definizione

Applicazione distribuita dove processi scambiano informazioni.

**Componenti:**
- User agent (interfaccia)
- Protocollo (regola comunicazione)

### Architetture

**Client-Server**  
Server IP statico, client IP dinamico, client comunica solo con server.  
*Esempio: WWW*

**Peer-to-Peer:**
- **Decentralizzato**: ogni peer è servent, passaparola, nessun server
- **Centralizzato**: server ha indici, peer hanno file
- **Ibrido**: super-peer eletti con funzione indicizzazione

### Applicazioni Web

**Monolitica**  
Singola entità, sviluppo veloce ma poco scalabile, manutenzione difficile.

**Microservizi**  
Componenti indipendenti, ognuno con funzione e database proprio, comunicazione tramite API, linguaggi diversi possibili.
- *Caratteristiche*: scalabilità indipendente, agilità sviluppo, isolamento difetti, dati decentralizzati

**Mobile**  
Progettate per dispositivi mobili, interfaccia touch/GPS, native o ibride.

---

## UDA 1 - DEVOPS, SRE E CI/CD

### DevOps

Metodologia di collaborazione tra Development e Operations per consegna software continua, affidabile e veloce.  
*Non esistono regole codificate, solo linee guida.*

**Fasi:**  
Plan → Develop → Build → Test → Release → Deploy → Operate → Report → Feedback

**Vantaggi:**
- Identificazione anticipata problemi
- Risoluzione rapida
- Qualità migliorata
- Riduzione supporto post-vendita

### SRE (Site Reliability Engineering)

Implementazione pratica dei principi DevOps (DevOps è filosofia, SRE è implementazione).

**Focus:** affidabilità sistemi, efficienza, scalabilità

**Funzioni:**
- Ponte tra dev/ops
- Automazione
- Monitoraggio
- Gestione incidenti
- Sicurezza

### CI/CD Pipeline

Insieme di pratiche per rilascio continuo e sicuro degli aggiornamenti.  
*Rientra nell'Agile: ogni rilascio con piccoli cambiamenti, codice versionato frequentemente.*

**Continuous Integration (CI)**  
Integrazione frequente modifiche con test automatici.
- *Modalità*: rilascio periodico giornaliero o giorni specifici
- *Vantaggi*: facile identificare difetti, meno conflitti

**Continuous Delivery**  
Automazione rilascio su repository.

**Continuous Deployment**  
Rilascio automatico in produzione (fase finale pipeline).

**Gestione funzionalità:**
- Flag (attiva/disattiva funzioni)
- Branching (branch specifici per funzionalità)

**Packaging e test:**
- Automazione generazione pacchetto
- Framework per test (regressione, analisi statica, performance, API, sicurezza)

*Principio: CI/CD si ripete ad ogni modifica codice.*

---

## UDA 1 - CONTROLLO VERSIONI E GIT

### VCS (Version Control System)

Sistema che gestisce modifiche ai file da più persone.

**Garantisce:**
- Reversibilità (tornare a qualsiasi punto)
- Concorrenza (più persone modificano stesso progetto)
- Annotazione (aggiungere note)

### Terminologia

| Termine | Descrizione |
|---------|-------------|
| **Working Directory** | Cartella locale con file progetto |
| **Staging Area** | File "finiti" pronti per salvataggio, area di transito |
| **Repository** | Archivio che traccia cronologia e modifiche, locale o su server |
| **Add** | Registra file da versionare, li sposta in staging area |
| **Commit** | Salvataggio versione, "fotografia" progetto con modifiche staging area |
| **Branch** | Diramazione percorso sviluppo per sviluppi paralleli |
| **Merge** | Riunisce versioni differenti in nuova versione |
| **Checkout** | Recupera commit precedente, riporta progetto a versione specifica |
| **Push/Pull** | Push pubblica commit da locale a remoto; pull scarica modifiche da remoto a locale |
| **Fork** | Copia completa e indipendente di repository in altra locazione |

### CVCS vs DVCS

| Tipo | Descrizione |
|------|-------------|
| **CVCS (Centralizzato)** | Singola copia completa su server, sviluppatori salvano su server centrale |
| **DVCS (Distribuito)** | Ogni sviluppatore ha copia locale completa, salva localmente, sincronizza con remoto |

---

## GIT - LABORATORIO

### Caratteristiche

Sistema distribuito di controllo versione. Ogni sviluppatore ha copia locale completa, modifica indipendentemente.

**Quattro caratteristiche vincenti:**
- Cambio contesto senza conflitti
- Linee codice basate su ruoli
- Flusso lavoro basato su funzionalità
- Sperimentazione usa e getta

**Funzionamento:**
- Crea repository (file system)
- Ogni commit genera cartella con solo file modificati (risparmio spazio)
- Struttura a grafo con istantanee
- Ogni commit contiene: autore, data, ora, descrizione

### Architettura

**Tre alberi:**
```
Working Directory → Index/Staging Area → HEAD
(file progetto)    (transito file add)   (ultimo commit)
```

### Comandi Principali

**Setup:**
```bash
git init                                    # Crea repository
git config --global user.email/name         # Identità autore
```

**Gestione:**
```bash
git add <file>                              # Staging
git commit -m "msg"                         # Salva con SHA-1
git log                                     # Cronologia
git log --oneline --decorate                # Log compresso
```

**Ripristino:**
```bash
git reset <ID>                              # Torna indietro, cancella cronologia
git revert <ID>                             # Annulla preservando cronologia
git checkout <ID>                           # Recupera commit preservando successivi
```

**Branch:**
```bash
git branch -v                               # Visualizza
git branch <nome>                           # Crea
git checkout <branch>                       # Passa a branch
git checkout -b <nome>                      # Crea e passa
git merge <branch>                          # Fonde
```

**Altro:**
```bash
git rm <file>                               # Elimina da repository
git rm --cached <file>                      # Rimuove da staging
git diff                                    # Mostra modifiche
```

### Collaborazione GitHub

**GitHub:** Piattaforma hosting repository remoti.

**Livelli:** working → staging → repo locale → repo remoto

**Setup:**
- Creare account
- Creare repository remoto (ottiene URL)

**Comandi:**
```bash
git clone <url>                             # Copia remoto in locale
git remote add origin <url>                 # Specifica remoto
git remote -v                               # Visualizza remoto
git branch --set-upstream-to=origin/<remoto> <locale>  # Configura branch
git push                                    # Upload locale→remoto
git pull                                    # Download remoto→locale
git fetch                                   # Verifica allineamento (eseguire sempre a inizio sessione!)
```

**Conflitti:**  
Se collaboratore ha modificato file in lavorazione, serve merge che genera nuovo commit e richiede push.

**Modello:** copy/modify/merge - ogni sviluppatore ha tre copie
- Working copy
- Repository locale
- Repository remoto

---

## UDA 2 - FORMATI SCAMBIO DATI

### XML (eXtensible Markup Language)

#### Generalità

**Cos'è XML:**  
Non è un linguaggio di markup né l'evoluzione di HTML. È un **metalinguaggio di markup** (meta = oltre), cioè un linguaggio che permette di definire altri linguaggi di markup.

**Caratteristiche:**
- Non ha tag predefiniti
- Non serve per programmare né per definire pagine web
- È costituito da regole sintattiche standard per modellare la struttura di documenti e dati
- È diventato uno standard per lo scambio dati commerciali via Internet
- Specifiche ufficiali definite dal W3C

**Differenze con HTML:**
- HTML si occupa di visualizzare i dati
- XML si occupa di descrivere la natura dei dati
- XML ha lo scopo di rappresentare contenuti testuali organizzati in modo gerarchico

**Vantaggi:**
- Documento di testo compatibile con qualsiasi sistema HW/SW
- Può essere letto e modificato con qualsiasi editor
- I file XML possono essere trasmessi tra aziende e utenti diversi senza vincoli
- Separazione dati dalla rappresentazione grafica
- Insieme unico di regole sintattiche
- Tag con nomi significativi (leggibilità basata sul nome, non sulla posizione)

#### Utilizzo dell'XML

**Memorizzazione dati strutturati nelle pagine HTML:**
- XML permette di definire "data islands" (isole dei dati)
- HTML usato solo per layout e presentazione
- Se i dati cambiano, non serve cambiare l'HTML

**Scambio dati:**  
Risolve problemi di incompatibilità tra sistemi diversi convertendo i dati in formato XML

**Condivisione dati:**  
Essendo puro testo, fornisce un modo di condividere dati slegato da software e hardware

**Memorizzazione:**  
Può essere utilizzato per memorizzare dati in file o database

#### Sintassi XML

**Struttura documento XML:**

**Prologo (opzionale):**
- XML declaration: `<?xml version="1.0" encoding="UTF-8" standalone="yes"?>`
- Riferimenti opzionali a documenti esterni (Processing Instruction o Doctype declaration)

**Corpo:** documento XML vero e proprio

**Regole sintattiche fondamentali:**
- Il contenuto deve corrispondere a una gerarchia di tag non sovrapposti
- I tag che si aprono per ultimi devono chiudersi per primi
- Ogni tag deve avere una chiusura (o forma abbreviata `<tag/>` per tag vuoti)
- È possibile inserire commenti: `<!-- commento -->`
- Deve sempre esserci un tag radice (root) che racchiude tutti gli altri
- XML è case sensitive (maiuscole ≠ minuscole)

**Tipi di documento:**
- **Ben formato**: rispetta le regole sintattiche
- **Valido**: rispetta le regole sintattiche E semantiche (definite in XSD o DTD)

**Regole per nomi elementi:**
- Devono iniziare con lettera o trattino basso
- Non possono iniziare con "xml" (o XML, Xml, ecc.)
- Possono contenere lettere, cifre, trattini, trattini bassi e punti
- Non possono contenere spazi
- Gli attributi sono sempre racchiusi tra singoli o doppi apici

#### XSD (XML Schema Definition)

**Cos'è:**  
Linguaggio che definisce la struttura di un documento XML. Successore del DTD (Document Type Definition), scritto anch'esso in XML.

**Elemento radice:**  
```xml
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
```

**Cosa definisce uno schema XSD:**
- Gli elementi di un documento XML e la loro relazione gerarchica
- Gli eventuali attributi negli elementi
- Il numero e l'ordinamento degli elementi
- Gli eventuali elementi vuoti
- Il tipo di dati contenuto negli elementi e negli attributi
- I valori predefiniti o costanti del contenuto

**Dichiarazione nel prologo XML:**
```xml
xmlns:xsi="http://www.w3.org/XMLSchema-instance"
xsi:noNamespaceSchemaLocation="nomefile.xsd"
```

**Elementi semplici:**
- Possono contenere solo testo (stringhe, numeri, date, orari)
- Non possono includere attributi o altri elementi
- Sintassi: `<xs:element name="..." type="..."/>`
- Tipi comuni: `xs:string`, `xs:decimal`, `xs:integer`, `xs:date`, `xs:time`
- Possono avere valori predefiniti (default) o costanti (fixed)
- Possono avere restrizioni (restriction): `minExclusive`, `maxInclusive`, `length`, `pattern` (espressioni regolari), `fractionDigits`

**Elementi complessi:**
- Elemento vuoto con attributi
- Elemento che contiene altri elementi (`xs:sequence`)
- Elemento con solo testo ma con attributi (`xs:simpleContent` + `xs:extension`)
- Elemento che contiene sia testo che altri elementi (`mixed="true"`)

#### Attributi vs Elementi

**Usare elementi quando:**
- Si rappresentano entità o strutture gerarchiche
- Il concetto necessita di ulteriori dettagli
- Si vuole espandibilità futura

**Usare attributi quando:**
- Si rappresentano proprietà o metadati
- Sono informazioni aggiuntive (come identificatori)
- Logica simile al modello ER nei database relazionali

#### Namespace

**Definizione:**  
Contenitori logici per evitare problemi di omonimia (come in C#, Java, Python)

**Sintassi:**  
`NamespacePrefix:xmlns="NamespaceURI"`

**Esempio:**
```xml
<lb:libro xmlns:lb="mioSito.com/libri">
  <lb:titolo>Libro di informatica</lb:titolo>
</lb:libro>
```

#### Attributi Globali

Attributi predefiniti con `xml:` che sono globali e utilizzabili in qualsiasi elemento:
- **xml:lang**: indica la lingua del testo (codice ISO 639-1)
- **xml:id**: assegna un identificatore univoco all'elemento

#### Parsing di XML

**Parser:**  
Strumento che legge, interpreta e converte XML in albero sintattico manipolabile

**CDATA (Character DATA):**
- Per evitare che il contenuto sia analizzato dal parser
- Permette di inserire qualsiasi sequenza di caratteri
- Utile per inserire codice o XML/HTML senza interpretazione
- Sintassi: `<![CDATA[ contenuto ]]>`

**DOM (Document Object Model):**
- Struttura dati gerarchica risultante dal parsing HTML
- Oggetto che rappresenta documento e tutti i suoi elementi come nodi
- Interfaccia di programmazione per JavaScript

---

### JSON (JavaScript Object Notation)

#### Generalità

**Cos'è JSON:**  
Formato standard, aperto, per immagazzinare e scambiare informazioni tra applicazioni

**Origine:**  
Basato su sottoinsieme del linguaggio JavaScript (Standard ECMA-262, 1999), specificamente sulla sintassi degli object literal

**Caratteristiche:**
- JSON non è JavaScript eseguibile, usa solo literal statici
- Ogni documento JSON valido è sintassi JavaScript valida
- Non ogni JavaScript valido è sintatticamente valido in JSON

**Vantaggi rispetto a XML:**
- Dimensione documento molto inferiore
- Struttura più semplice
- Facilmente integrabile nelle applicazioni Web
- Supportato nativamente in molti linguaggi e database
- Utilizzato in database NoSQL

#### Formato JSON

**Due sole strutture fondamentali:**
- Insieme di coppie (nome, valore) → dizionari/mappe/oggetti
- Lista ordinata di valori → array/sequenze

**Uso nel web:**
- Formato maggiormente utilizzato per messaggi di risposta dei servizi web
- Ottimale per JavaScript client-side

**Oggetto letterale:**
- Definito con coppie proprietà/valori separate da virgola
- Racchiuso tra parentesi graffe `{}`
- Esempio: `var JSON = { proprieta1: 'valore', proprieta2: 'valore' };`

#### Tipi di dati supportati

| Tipo | Descrizione |
|------|-------------|
| **Number** | Di qualunque formato (interi, decimali) |
| **Boolean** | true o false |
| **String** | Delimitate da apici, doppi apici o backtick `` ` `` |
| **Object** | Insieme NON ordinato di valori tra parentesi graffe. I nomi devono essere stringhe diverse (funzione di chiave) |
| **Array** | Insieme ordinato di valori tra parentesi quadre |
| **null** | Per inizializzazione a vuoto delle variabili |
| **Whitespace** | Consentito liberamente prima e dopo i token (ma non all'interno) |

**Esempio Object:**
```json
{ "id": "01669", "linguaggio": "JAVA", "prezzo": 15.50 }
```

**Esempio Array:**
```json
{ "books": [ {"linguaggio":"Java"}, {"linguaggio":"Python"} ] }
```

#### Creazione oggetti JSON

**Tre modalità in JavaScript:**
```javascript
var oggetto1 = {};                                      // Creare oggetto vuoto
var oggetto2 = new Object();                            // Creare nuovo oggetto
var oggetto3 = { "titolo":"TPSIT vol.3", "prezzo":23.50 };  // Creare con valori
```

**Oggetti nidificati:**  
Possibile creare gerarchie di oggetti dentro oggetti

#### Parsing di JSON

**Metodo eval() (DEPRECATO):**
- Interpreta qualsiasi stringa come codice JavaScript
- **PERICOLOSO**: può eseguire qualsiasi istruzione (code injection)
- Lento
- Sintassi: `var mioOggettoJSON = eval('(' + mioTestoJSON + ')');`

**Metodi JSON (RACCOMANDATI):**

**JSON.parse() - Deserializzazione:**
- Converte testo JSON in oggetto JavaScript
- Sintassi: `JSON.parse(stringa[, reviver])`
- Genera SyntaxError se stringa non valida
- Parametro opzionale reviver: funzione per trasformare valori durante parsing

**JSON.stringify() - Serializzazione:**
- Converte oggetto JavaScript in stringa JSON
- Processo inverso di parse()

*Nota importante: JSON ammette solo valori semplici e atomici, non può contenere funzioni*

---

### MARKDOWN

#### Generalità

**Cos'è Markdown:**  
Linguaggio di markup leggero per formattazione testo

**Caratteristiche:**
- Facile da leggere e scrivere
- Sintassi semplice e intuitiva
- Convertibile in HTML e altri formati
- Ampiamente usato per documentazione, README, wiki

#### Sintassi Base

| Elemento | Sintassi |
|----------|----------|
| **Intestazioni** | `# H1`, `## H2`, `### H3` (fino a 6 livelli) |
| **Grassetto** | `**testo**` o `__testo__` |
| **Corsivo** | `*testo*` o `_testo_` |
| **Liste non ordinate** | `- elemento` o `* elemento` |
| **Liste ordinate** | `1. elemento`, `2. elemento` |
| **Link** | `[testo](url)` |
| **Immagini** | `![alt text](url)` |
| **Codice inline** | `` `codice` `` |
| **Blocco di codice** | ` ```linguaggio` ... ` ``` ` |
| **Citazioni** | `> testo citazione` |

---

### YAML (YAML Ain't Markup Language)

#### Generalità

**Cos'è YAML:**  
Linguaggio di serializzazione dati human-readable

**Caratteristiche:**
- Sintassi minimalista basata su indentazione
- Usato per file di configurazione
- Supporta strutture dati complesse
- Superset di JSON (ogni JSON valido è YAML valido)

#### Sintassi Base

| Concetto | Descrizione |
|----------|-------------|
| **Indentazione** | Usa spazi (NON tab) per definire struttura |
| **Coppie chiave-valore** | `chiave: valore` |
| **Liste** | Prefisso `-` seguito da spazio |
| **Oggetti nidificati** | Tramite indentazione |
| **Tipi supportati** | Stringhe, numeri, booleani, null, date |
| **Commenti** | `# commento` |

**Esempio:**
```yaml
persona:
  nome: Mario
  cognome: Rossi
  età: 30
  hobbies:
    - lettura
    - sport
```

---

## SCHEMA RIEPILOGATIVO RAPIDO

| Argomento | Sintesi |
|-----------|---------|
| **SISTEMI** | Centralizzato (1 nodo) \| Distribuito (più host) \| Parallelo (stesso codice) |
| **RUOLI** | Client (IP dinamico) \| Server (IP statico) \| Actor (entrambi) |
| **CLASSIFICAZIONE SD** | Calcolo (cluster/grid) \| Informativi (web) \| Pervasivi (sensori/domotica) |
| **FLYNN** | SISD (1-1) \| SIMD (1-molti, grafica) \| MISD (molti-1, teorico) \| MIMD (molti-molti) |
| **CLUSTER vs GRID** | Cluster (omogenei, vicini, >1Gbit/s) \| Grid (eterogenei, distribuiti) |
| **ARCHITETTURE SW** | Terminali → Client-Server → Web-Centric → Cooperativa → Distribuita → Microservizi |
| **TIER** | 1 (mainframe) \| 2 (poco scalabile) \| 3 (middleware) \| N (complesse) |
| **LIVELLI** | Front-end (interfaccia) \| Middle (logica) \| Back-end (database) |
| **SOCKET** | `<IP:porta>` identifica processo univocamente |
| **COMUNICAZIONE** | Unicast (1-a-1) \| Multicast (1-a-molti) |
| **P2P** | Decentralizzato (no server) \| Centralizzato (server indici) \| Ibrido (super-peer) |
| **APPLICAZIONI** | Monolitica (tutto insieme) \| Microservizi (componenti indipendenti) |
| **DEVOPS** | Metodologia Dev+Ops \| SRE (implementazione) \| CI (frequente) \| CD (automatico) |
| **PROTOCOLLI** | HTTP (web) \| FTP (file) \| SMTP (invio) \| POP3 (ricevi) \| DNS (nomi) \| SNMP (gestione) |
| **VCS** | Reversibilità + Concorrenza + Annotazione \| CVCS (centralizzato) \| DVCS (distribuito) |
| **GIT** | Working Dir → Staging (add) → HEAD (commit) \| Branch \| Merge \| Push/Pull |
| **XML** | Metalinguaggio, gerarchico, tag personalizzati, XSD per validazione, verboso |
| **JSON** | Lightweight, coppie chiave-valore, array, parse()/stringify(), web-oriented |
| **YAML** | Human-readable, indentazione, configurazioni, superset JSON |
| **Markdown** | Markup leggero, documentazione, facile sintassi |
