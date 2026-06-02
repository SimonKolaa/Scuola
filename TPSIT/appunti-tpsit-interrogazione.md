# RIASSUNTO COMPLETO TPSIT - INTERROGAZIONE

---

## UDA 1 - SISTEMI DISTRIBUITI

### Definizioni Base

**Sistema Centralizzato**: dati e applicazioni risiedono su un unico nodo elaborativo (mainframe con terminali stupidi).

**Sistema Distribuito**: sistema in cui almeno una condizione è verificata: elaborazione distribuita (applicazioni su più host collaboranti) oppure base di dati distribuita (dati su più host). È un insieme di applicazioni logicamente indipendenti che collaborano attraverso un'infrastruttura comune.

**Sistema Parallelo vs Distribuito**: i sistemi paralleli hanno più processori che eseguono lo stesso codice, i sistemi distribuiti hanno più macchine indipendenti con programmi diversi.

### Ruoli delle Applicazioni

**Client**: utilizza servizi offerti da altre applicazioni, IP dinamico, comunica solo con server.

**Server**: fornisce servizi, IP statico, sempre attivo e in ascolto.

**Actor**: assume sia ruolo client che server in base al contesto.

### Classificazione Sistemi Distribuiti

**Per destinazione d'uso**:
- **Calcolo**: cluster (computer omogenei) e grid (macchine eterogenee distribuite)
- **Informativi**: Web, sistemi legacy
- **Pervasivi**: sensori, domotica, wearable, PAN, reti wireless

**Per accoppiamento**:
- **Debole**: risorse poco interdipendenti (data center multinazionale)
- **Forte**: sistema fortemente integrato (banche, catene distribuzione)

### Benefici e Svantaggi

**Benefici**: affidabilità (ridondanza), trasparenza (sistema visto come unico), scalabilità (espansione senza interruzioni), tolleranza ai guasti, economicità, apertura (interoperabilità e portabilità).

**Svantaggi**: maggiore complessità software, problemi sicurezza (dati in rete), maggiore richiesta banda, necessità linguaggi e strumenti specifici.

---

## UDA 1 - ARCHITETTURE HARDWARE

### Classificazione di Flynn

Framework per classificare architetture hardware basato su flusso istruzioni e dati.

**SISD**: 1 istruzione, 1 dato. Computer tradizionale con singola CPU, esecuzione sequenziale.

**SIMD**: 1 istruzione, più dati. Applicazioni grafiche, calcoli vettoriali e matriciali.

**MISD**: più istruzioni, 1 dato. Teoriche, non commercializzate, possibile uso in crittografia.

**MIMD**: più istruzioni, più dati. Due tipi:
- **Memoria condivisa (multiprocessori)**: comunicazione tramite variabili condivise, necessaria sincronizzazione
- **Memoria privata (multicomputer)**: comunicazione tramite messaggi send/receive, include le LAN

### Cluster vs Grid

**Cluster**: nodi omogenei su stesso rack, rete ad alta velocità (>1Gbit/s), stesso OS. Architetture: gerarchica (Beowulf) o Single System Image (MOSIX). Corrisponde a MIMD a memoria privata.

**Grid**: sistema decentralizzato, nodi eterogenei (hardware, software, rete diversi), geograficamente distribuiti.

### Sistemi Pervasivi

Nodi piccoli, mobili, wireless, parte di sistemi più grandi. Requisiti: adattamento contesto, composizione ad hoc, auto-configurazione, condivisione default. Applicazioni: reti domestiche, domotica, wearable computing sanitario, reti sensori.

---

## UDA 1 - ARCHITETTURE SOFTWARE

### Evoluzione

**1. Terminali Remoti**: mainframe + terminali stupidi (NON distribuito)

**2. Client-Server**: separazione tra richiedenti e fornitori servizi

**3. Web-Centric**: elaborazione su server, client solo interfaccia

**4. Cooperativa**: entità autonome con modello a componenti (OdP, CORBA)

**5. Completamente Distribuita**: entità paritetiche, servizi duplicati (RMI, DCOM)

**6. Microservizi**: componenti autonomi con API, database proprio per servizio

### Middleware

Software tra applicazioni e sistema operativo che garantisce interoperabilità su sistemi eterogenei. Basato su RPC o message passing.

---

## UDA 1 - CLIENT-SERVER E APPLICAZIONI WEB

### Tecnologie Web

**Client-side**: elaborazione sul browser, codice visibile, non serve web server.

**Server-side**: elaborazione su web server, codice non visibile, serve URL.

**Linguaggi**: mark-up (documenti strutturati) e programmazione (sequenze istruzioni).

### Modello Client-Server

Insieme di server (gestiscono risorse) e client (richiedono accesso). Si definiscono client/server i processi, non gli host.

**Flusso**: client invia richiesta → server riceve → server esegue (genera thread) → server risponde → client riceve.

**Servizi tipici**: Telnet, HTTP, FTP, SMTP, IMAP.

### Socket

Coppia `<IP:porta>` che identifica univocamente un processo. Nel server: socket di benvenuto (in ascolto) + socket dinamici (thread per ogni client, gestione concorrenza).

### Comunicazione

**Unicast**: uno-a-uno, server risponde singolarmente (es. pagina web).

**Multicast**: uno-a-molti, server trasmette contemporaneamente a gruppo (es. streaming).

### Livelli e Strati

**Livelli (Tier)** - organizzazione fisica:
- Front-end: interfaccia utente
- Middle tier: logica applicativa
- Back-end: gestione database

**Strati (Layer)** - organizzazione logica:
- Presentation Layer: acquisizione/presentazione dati
- Business Logic Layer: logica elaborazione, relazioni tra entità
- Resource Management Layer: gestione dati persistenti

### Architetture Multi-Tier

**1-Tier**: mainframe con terminali (NON client-server).

**2-Tier**: thin-client (server logica+dati, client presentazione) o thick-client (server dati, client logica+presentazione). Limite: poco scalabile.

**3-Tier**: front+middle+back separati con middleware. Vantaggi: scalabilità, sicurezza. Svantaggi: tempi comunicazione, complessità.

**N-Tier**: numero variabile livelli per applicazioni complesse.

---

## UDA 1 - APPLICAZIONI DI RETE

### Protocolli Livello Applicazione

**HTTP**: navigazione web | **FTP**: trasferimento file | **SMTP**: invio email | **POP3**: ricezione email | **DNS**: risoluzione nomi | **SNMP**: gestione rete

### Definizione

Applicazione distribuita dove processi scambiano informazioni. Componenti: user agent (interfaccia) e protocollo (regola comunicazione).

### Architetture

**Client-Server**: server IP statico, client IP dinamico, client comunica solo con server. Esempio: WWW.

**Peer-to-Peer**:
- **Decentralizzato**: ogni peer è servent, passaparola, nessun server
- **Centralizzato**: server ha indici, peer hanno file
- **Ibrido**: super-peer eletti con funzione indicizzazione

### Applicazioni Web

**Monolitica**: singola entità, sviluppo veloce ma poco scalabile, manutenzione difficile.

**Microservizi**: componenti indipendenti, ognuno con funzione e database proprio, comunicazione tramite API, linguaggi diversi possibili. Caratteristiche: scalabilità indipendente, agilità sviluppo, isolamento difetti, dati decentralizzati.

**Mobile**: progettate per dispositivi mobili, interfaccia touch/GPS, native o ibride.

---

## UDA 1 - DEVOPS, SRE E CI/CD

### DevOps

Metodologia di collaborazione tra Development e Operations per consegna software continua, affidabile e veloce. Non esistono regole codificate, solo linee guida.

**Fasi**: Plan → Develop → Build → Test → Release → Deploy → Operate → Report → Feedback

**Vantaggi**: identificazione anticipata problemi, risoluzione rapida, qualità migliorata, riduzione supporto post-vendita.

### SRE (Site Reliability Engineering)

Implementazione pratica dei principi DevOps (DevOps è filosofia, SRE è implementazione). Focus: affidabilità sistemi, efficienza, scalabilità. Funzioni: ponte tra dev/ops, automazione, monitoraggio, gestione incidenti, sicurezza.

### CI/CD Pipeline

Insieme di pratiche per rilascio continuo e sicuro degli aggiornamenti. Rientra nell'Agile: ogni rilascio con piccoli cambiamenti, codice versionato frequentemente.

**Continuous Integration (CI)**: integrazione frequente modifiche con test automatici. Modalità: rilascio periodico giornaliero o giorni specifici. Vantaggi: facile identificare difetti, meno conflitti.

**Continuous Delivery**: automazione rilascio su repository.

**Continuous Deployment**: rilascio automatico in produzione (fase finale pipeline).

**Gestione funzionalità**: flag (attiva/disattiva funzioni) o branching (branch specifici per funzionalità).

**Packaging e test**: automazione generazione pacchetto, framework per test (regressione, analisi statica, performance, API, sicurezza).

**Principio**: CI/CD si ripete ad ogni modifica codice.

---

## UDA 1 - CONTROLLO VERSIONI E GIT

### VCS (Version Control System)

Sistema che gestisce modifiche ai file da più persone. Garantisce: reversibilità (tornare a qualsiasi punto), concorrenza (più persone modificano stesso progetto), annotazione (aggiungere note).

### Terminologia

**Working Directory**: cartella locale con file progetto.

**Staging Area**: file "finiti" pronti per salvataggio, area di transito.

**Repository**: archivio che traccia cronologia e modifiche, locale o su server.

**Add**: registra file da versionare, li sposta in staging area.

**Commit**: salvataggio versione, "fotografia" progetto con modifiche staging area.

**Branch**: diramazione percorso sviluppo per sviluppi paralleli.

**Merge**: riunisce versioni differenti in nuova versione.

**Checkout**: recupera commit precedente, riporta progetto a versione specifica.

**Push/Pull**: push pubblica commit da locale a remoto, pull scarica modifiche da remoto a locale.

**Fork**: copia completa e indipendente di repository in altra locazione.

### CVCS vs DVCS

**CVCS (Centralizzato)**: singola copia completa su server, sviluppatori salvano su server centrale.

**DVCS (Distribuito)**: ogni sviluppatore ha copia locale completa, salva localmente, sincronizza con remoto.

---

## GIT - CONCETTI PRINCIPALI

### Caratteristiche

Sistema distribuito di controllo versione. Ogni sviluppatore ha copia locale completa, modifica indipendentemente.

**Quattro caratteristiche vincenti**: cambio contesto senza conflitti, linee codice basate su ruoli, flusso lavoro basato su funzionalità, sperimentazione usa e getta.

**Funzionamento**: crea repository (file system), ogni commit genera cartella con solo file modificati (risparmio spazio), struttura a grafo con istantanee. Ogni commit: autore, data, ora, descrizione.

### Architettura

**Tre alberi**: Working Directory (file progetto) → Index/Staging Area (transito file add) → HEAD (ultimo commit)

### Operazioni Principali

**Setup**: init (crea repository), config (identità autore)

**Gestione**: add (staging), commit (salva con SHA-1), log (cronologia)

**Ripristino**: reset (torna indietro, cancella cronologia), revert (annulla preservando cronologia), checkout (recupera commit preservando successivi)

**Branch**: visualizza, crea, passa, merge (fonde)

**Altro**: rm (elimina da repository), diff (mostra modifiche)

### Collaborazione

**GitHub**: piattaforma hosting repository remoti. Aggiunge livello: working → staging → repo locale → repo remoto.

**Operazioni remote**: clone (copia remoto in locale), remote add (specifica remoto), push (upload locale→remoto), pull (download remoto→locale), fetch (verifica allineamento)

**Conflitti**: se collaboratore ha modificato file in lavorazione, serve merge che genera nuovo commit e richiede push.

**Modello**: copy/modify/merge - ogni sviluppatore ha tre copie (working copy, repository locale, repository remoto)

---

## UDA 2 - XML (eXtensible Markup Language)

### Cos'è XML

**Definizione**: XML è un **metalinguaggio di markup** (NON linguaggio di programmazione!) che permette di definire altri linguaggi attraverso tag personalizzati.

**Scopo principale**: **Scambio di dati** tra sistemi diversi, specialmente via Internet.

**Caratteristiche fondamentali**:
- File di testo → compatibile con qualsiasi sistema HW/SW
- Estensione: `.xml`
- Standard W3C
- **Descrive la natura dei dati**, non la loro visualizzazione (HTML visualizza)
- Organizzazione **gerarchica ad albero**
- Separazione dati da rappresentazione grafica
- Regole unica di sintassi

### Differenza XML vs HTML

**XML**: descrive e trasporta dati, tag personalizzati, focus su contenuto/struttura

**HTML**: visualizza dati, tag predefiniti, focus su presentazione

### Utilizzo dell'XML

**Data Islands**: dati XML memorizzati dentro pagine HTML, usando HTML solo per layout/presentazione. Se dati cambiano non serve cambiare HTML.

**Scambio dati**: risolve incompatibilità tra sistemi diversi convertendo in formato XML.

**Condivisione**: essendo testo puro, indipendente da software e hardware.

**Memorizzazione**: può salvare dati in file o database.

---

## STRUTTURA DOCUMENTO XML

### Componenti

**PROLOGO** (opzionale): XML declaration + riferimenti a documenti esterni (XSD, DTD, CSS)

**Elementi declaration**:
- `version`: versione XML (1.0 più usata, 1.1 meno supportata)
- `encoding`: codifica caratteri (UTF-8, ISO-8859-1)
- `standalone`: se conforme a sintassi esterna ("yes" o "no")

**CORPO** (obbligatorio): dati veri e propri, deve avere **unico elemento radice (root)**, tag personalizzati gerarchici

---

## REGOLE SINTATTICHE XML

### Documento "Ben Formato"

Rispetta regole sintattiche:

1. XML declaration corretta (se presente)
2. Un unico elemento radice
3. Corretta nidificazione: tag aperti per ultimi chiusi per primi, no sovrapposizione
4. Ogni tag ha chiusura oppure forma abbreviata per vuoti
5. Tag apertura/chiusura coincidono: case sensitive
6. Attributi tra apici (singoli o doppi)
7. Commenti consentiti

### Regole Nomi Tag

**Consentito**: iniziare con lettera/underscore, contenere lettere/cifre/trattini/underscore/punti

**NON consentito**: iniziare con numeri, iniziare con "xml" (riservato), contenere spazi

---

## ELEMENTI E ATTRIBUTI

### Quando Usare Elementi

Per rappresentare: dati principali/entità, strutture espandibili, informazioni gerarchiche, contenuti con dettagli

### Quando Usare Attributi

Per rappresentare: metadati (dati sui dati), proprietà semplici/atomiche, identificatori univoci, informazioni non espandibili

**Regola pratica**: seguire logica modello ER database relazionali

---

## DOCUMENTO VALIDO vs BEN FORMATO

### Ben Formato
Rispetta solo regole sintattiche XML, parser può leggerlo senza errori, NON garantisce struttura corretta dati

### Valido
Ben formato + rispetta regole semantiche (XSD/DTD), struttura dati verificata, tipi controllati, ordine rispettato, elementi obbligatori presenti

**Relazione**: tutti documenti validi sono ben formati, NON tutti ben formati sono validi

**Regole sintattiche**: XML declaration, elemento radice unico, nidificazione corretta, tag chiusi, nomi validi, attributi tra apici

**Regole semantiche**: definite da XSD o DTD

---

## XSD - XML Schema Definition

### Cos'è XSD

Definisce struttura e regole semantiche documento XML.

**Caratteristiche**: scritto in XML, definisce elementi semplici/complessi, specifica tipi dati, impone restrizioni, supporta namespace

### Cosa Definisce

Elementi e relazione gerarchica, attributi, numero/ordinamento elementi, elementi vuoti, tipi di dati, valori predefiniti/costanti, restrizioni (range, pattern, lunghezza)

### Elementi Semplici

Contengono solo testo, NO attributi, NO altri elementi.

**Tipi comuni**: xs:string (stringhe), xs:integer (interi), xs:decimal (decimali), xs:date (date aaaa-mm-gg), xs:time (orari hh:mm:ss), xs:boolean (booleani)

### Valori Predefiniti e Costanti

**default**: valore assunto se elemento vuoto

**fixed**: valore costante obbligatorio

### Restrizioni

**Range numerico**: minInclusive, maxInclusive, minExclusive, maxExclusive

**Decimali**: fractionDigits (numero cifre decimali)

**Pattern**: espressioni regolari (regex) per validare formato

**Lunghezza**: length (lunghezza esatta), minLength, maxLength

---

## ELEMENTI COMPLESSI XSD

### Tipi

**Contiene altri elementi**: usa sequence per definire ordine

**Elemento con attributi**: usa simpleContent + extension

**Elementi annidati con restrizioni**: combina complexType + simpleType + restriction

**Mixed content**: testo + elementi (attributo mixed="true")

---

## NAMESPACE

### Scopo

Evitare conflitti tra elementi con stesso nome ma significato diverso

### Definizione

Sintassi: `xmlns:prefisso="URI"`

Elementi distinti grazie a prefissi namespace diversi

---

## ATTRIBUTI GLOBALI XML

### Definiti W3C

Prefissati con `xml:`, utilizzabili su qualsiasi elemento

**xml:lang**: specifica lingua contenuto (codice ISO 639-1)

**xml:id**: identificatore univoco elemento

---

## PARSING E CDATA

### Parsing XML

**Parser**: strumento che legge, interpreta, converte XML in albero sintattico (DOM - Document Object Model) manipolabile

### CDATA

**Scopo**: impedire al parser di interpretare contenuto come markup

**Sintassi**: `<![CDATA[ ... ]]>`

**Uso**: inserire codice HTML/XML/JavaScript/caratteri speciali senza analisi

---

## UDA 2 - JSON (JavaScript Object Notation)

### COS'È JSON

**JSON** = **JavaScript Object Notation**

**Definizione**: formato di interscambio di dati di tipo **testuale** basato sulla sintassi degli **oggetti literal** del linguaggio JavaScript.

**Origine**: deriva da un **sottoinsieme del linguaggio di programmazione JavaScript** (Standard ECMA-262 3ª edizione, dicembre 1999).

**Caratteristiche**:
- Formato di testo **completamente indipendente dal linguaggio di programmazione**
- Usa convenzioni conosciute dai programmatori di linguaggi della famiglia C (C, C++, C#, Java, JavaScript, Perl, Python, ecc.)
- Queste proprietà rendono JSON un **linguaggio ideale per lo scambio di dati**

---

## VANTAGGI JSON vs XML

**JSON è più utilizzato di XML** per i seguenti motivi:

1. **File di dimensioni inferiori** rispetto ai corrispondenti file XML
2. **Struttura più semplice e comprensibile** da parte di un umano
3. **Migliore integrazione con JavaScript**: il parsing JSON è nativo in JavaScript
4. **Supporto in molti linguaggi di programmazione** e database NoSQL
5. **Facilmente serializzabile e deserializzabile**
6. Più **semplice da scrivere** rispetto a XML

---

## STRUTTURA JSON

JSON è costruito su **due strutture**:

### 1. OBJECT (Oggetto)

- Insieme **non ordinato** di coppie **(nome, valore)**
- Delimitato da **parentesi graffe** `{ }`
- I **nomi** devono essere **stringhe diverse** tra loro
- Ogni coppia nome/valore è separata da **virgola** `,`

### 2. ARRAY

- **Lista ordinata di valori**
- Delimitato da **parentesi quadre** `[ ]`
- I valori sono separati da **virgola** `,`

**Nota**: queste sono strutture dati universali, supportate da praticamente tutti i linguaggi di programmazione moderni.

---

## TIPI DI DATI JSON

JSON supporta i seguenti tipi di dati:

### 1. NUMBER (Numero)
- Qualunque formato numerico
- Interi o decimali
- Positivi o negativi

### 2. BOOLEAN (Booleano)
- Valori: `true` o `false`

### 3. STRING (Stringa)
- Può essere racchiusa tra:
  - Apici `'stringa'`
  - Doppi apici `"stringa"`
  - Backtick `` `stringa` ``

### 4. OBJECT (Oggetto)
- Insieme non ordinato di coppie nome/valore
- I nomi devono essere **stringhe diverse** tra loro

### 5. ARRAY
- Lista ordinata di valori

### 6. WHITESPACE
- Spazi bianchi consentiti **prima o dopo** qualsiasi token

### 7. NULL
- Valore speciale per inizializzazione vuota
- Rappresenta assenza di valore

---

## CREAZIONE OGGETTI JSON IN JAVASCRIPT

Esistono **tre modi** per creare un oggetto JSON in JavaScript:

### 1. Oggetto vuoto
Crea un oggetto senza proprietà

### 2. Nuovo oggetto (costruttore)
Usa il costruttore Object per creare un nuovo oggetto

### 3. Oggetto con valori (literal)
Definizione diretta con coppie chiave/valore

---

## SERIALIZZAZIONE E DESERIALIZZAZIONE

### SERIALIZZAZIONE

**Definizione**: processo di conversione di un **oggetto JavaScript** in una **stringa JSON**.

**Funzione JavaScript**: `JSON.stringify(oggetto)`

**Scopo**: preparare i dati per la **trasmissione** (es. invio via rete, salvataggio su file).

---

### DESERIALIZZAZIONE

**Definizione**: processo di conversione di una **stringa JSON** in un **oggetto JavaScript**.

**Funzione JavaScript**: `JSON.parse(stringa[, reviver])`

**Parametri**:
- `stringa`: la stringa JSON da convertire
- `reviver` (opzionale): funzione che può trasformare i valori durante il parsing

**Errori**: se la stringa JSON non è valida, genera un **SyntaxError**.

---

## FUNZIONE JSON.parse()

**Sintassi**: `JSON.parse(stringa[, reviver])`

**Funzionamento**:
- Analizza una stringa JSON
- Costruisce il valore JavaScript o l'oggetto descritto dalla stringa
- Può accettare una funzione **reviver** opzionale per trasformare i valori

**Parametro reviver**:
- Funzione opzionale che viene chiamata per ogni coppia chiave/valore
- Permette di **modificare i valori** durante il parsing
- Riceve come parametri `(chiave, valore)`
- Può restituire un valore trasformato o il valore originale

---

## FUNZIONE JSON.stringify()

**Sintassi**: `JSON.stringify(oggetto)`

**Funzionamento**:
- Converte un oggetto JavaScript in una stringa JSON
- Utile per **serializzare** i dati prima dell'invio

**Scopo principale**: preparare dati per la trasmissione via rete o per il salvataggio.

---

## IMPORTANTE: NON USARE eval()

⚠️ **ATTENZIONE**: **NON** utilizzare la funzione `eval()` per il parsing JSON!

**Motivi**:
1. **Vulnerabilità di sicurezza**: `eval()` esegue **qualsiasi codice JavaScript** contenuto nella stringa
2. **Rischio code injection**: un attaccante può inserire codice malevolo
3. **Performance**: `eval()` è molto più **lenta** di `JSON.parse()`

**Regola**: usare **SEMPRE** `JSON.parse()` per il parsing JSON, **MAI** `eval()`.

---

## DIFFERENZE JSON vs XML

| Caratteristica | JSON | XML |
|----------------|------|-----|
| **Verbosità** | Compatto | Verboso (tag apertura/chiusura) |
| **Leggibilità umana** | Alta | Media |
| **Dimensione file** | Minore | Maggiore |
| **Parsing JavaScript** | Nativo (`JSON.parse()`) | Richiede librerie DOM |
| **Supporto tipi dati** | Nativo (number, boolean, null) | Solo testo (serve XSD) |
| **Struttura** | Oggetti e array | Gerarchica con tag |
| **Commenti** | NON supportati | Supportati `<!-- -->` |
| **Uso principale** | API web, scambio dati leggero | Documenti complessi, configurazioni |
| **Semplicità scrittura** | Più semplice | Più complesso |

---

## MARKDOWN (cenni)

### Definizione

Linguaggio marcatura leggero creato 2004 (John Gruber, Aaron Swartz)

**Obiettivo**: conciliare formattazione testo con leggibilità dispositivi/persone

**Caratteristiche**: sintassi semplice/intuitiva, leggibile forma sorgente, conversione automatica HTML, estensione `.md`

### Tre Principi

**Immediatezza**: facile scrivere

**Compatibilità**: funziona qualsiasi piattaforma

**Longevità**: file testo puro sempre leggibile

### Sintassi Essenziale

**Formattazione**: asterischi/underscore per corsivo/grassetto/barrato

**Intestazioni**: cancelletti (6 livelli) oppure uguale/trattino sotto testo

**Elenchi**: puntati (trattino/asterisco/più), numerati (numero+punto), checkbox (parentesi quadre)

**Link**: parentesi quadre testo + parentesi tonde URL

**Immagini**: punto esclamativo + link

**Codice**: backtick inline, tre backtick blocco

**Tabelle**: barre verticali separano celle, trattini seconda riga per intestazione

**Citazioni**: maggiore (>) per blockquote

**Note piè pagina**: numero tra quadre con cappelletto

**Caratteri speciali**: backslash per escape

### Uso

GitHub (README, documentazione), documentazione tecnica (MkDocs, GitBook), note personali (Obsidian, Notion), blog (Jekyll, Hugo)

---

## YAML (cenni)

### Definizione

"YAML Ain't Markup Language" (ricorsivo), formato serializzazione dati human-readable, più leggibile JSON/XML

**Caratteristiche**: sintassi minimalista basata indentazione (spazi, NO tab), estensione `.yaml` o `.yml`, supporta tipi complessi, usato file configurazione

### Sintassi Base

**Coppie chiave-valore**: chiave seguita da due punti e valore

**Oggetti annidati**: indentazione (2 spazi standard)

**Liste**: trattino + spazio

**Lista oggetti**: combinazione indentazione + trattino

**Tipi dati**: stringhe, numeri, decimali, booleani, null, date

**Stringhe multilinea**: pipe (|) preserva a capo, maggiore (>) compatta

### Uso YAML

**Configurazione**: Docker, Kubernetes, CI/CD pipelines, Ansible

**Vantaggi**: più leggibile JSON/XML per configurazioni complesse, riduce parentesi/virgolette

**vs JSON**: YAML human-friendly, JSON machine-friendly, YAML supporta commenti, JSON più veloce parsing

---

## SCHEMA RIEPILOGATIVO

**SISTEMI**: Centralizzato (1 nodo) | Distribuito (più host) | Parallelo (stesso codice)

**RUOLI**: Client (IP dinamico) | Server (IP statico) | Actor (entrambi)

**CLASSIFICAZIONE SD**: Calcolo (cluster/grid) | Informativi (web) | Pervasivi (sensori/domotica)

**FLYNN**: SISD (1-1) | SIMD (1-molti, grafica) | MISD (molti-1, teorico) | MIMD (molti-molti: condivisa/privata)

**CLUSTER vs GRID**: Cluster (omogenei, vicini, >1Gbit/s) | Grid (eterogenei, distribuiti)

**ARCHITETTURE SW**: Terminali → Client-Server → Web-Centric → Cooperativa (CORBA) → Distribuita (RMI) → Microservizi

**TIER**: 1 (mainframe) | 2 (thin/thick, poco scalabile) | 3 (front+middle+back, middleware) | N (molti livelli)

**LIVELLI**: Front-end (interfaccia) | Middle (logica) | Back-end (database)

**SOCKET**: `<IP:porta>` identifica processo univocamente

**COMUNICAZIONE**: Unicast (1-a-1) | Multicast (1-a-molti)

**P2P**: Decentralizzato (no server) | Centralizzato (server indici) | Ibrido (super-peer)

**APPLICAZIONI**: Monolitica (tutto insieme) | Microservizi (componenti indipendenti API)

**DEVOPS**: Metodologia Dev+Ops | SRE (implementazione) | CI (integrazione frequente) | CD (rilascio automatico)

**PROTOCOLLI**: HTTP (web) | FTP (file) | SMTP (invio mail) | POP3 (ricevi mail) | DNS (nomi) | SNMP (gestione)

**VCS**: Reversibilità + Concorrenza + Annotazione | CVCS (centralizzato) | DVCS (distribuito)

**GIT**: Working Dir → Staging (add) → HEAD (commit) | Branch (rami) | Merge (unione) | Push/Pull (sincronizzazione)

**XML**: Metalinguaggio | Tag personalizzati | Gerarchico | XSD validazione | Verboso | Attributi/namespace | Ben formato (sintassi) vs Valido (sintassi+semantica)

**JSON**: Formato scambio | Deriva da sottoinsieme JavaScript | Oggetti (non ordinati) + Array (ordinati) | Tipi: Number, Boolean, String, Object, Array, null, Whitespace | Deserializzazione: JSON.parse(stringa, reviver) | Serializzazione: JSON.stringify(oggetto) | MAI eval() | Vantaggi vs XML: file più piccoli, struttura semplice, parsing nativo JS, facilmente serializzabile

**MARKDOWN**: Linguaggio leggero | Sintassi intuitiva | Conversione HTML | `.md` | Documentazione/note

**YAML**: Serializzazione human-readable | Indentazione | `.yaml`/`.yml` | Configurazioni | Più leggibile JSON/XML
