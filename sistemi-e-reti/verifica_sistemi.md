# Riepilogo Completo - Verifica Sistemi e Reti
## DHCP, DNS e Application Layer

---

## 📡 DHCP (Dynamic Host Configuration Protocol)

### Introduzione al DHCP
Il DHCP è un protocollo di rete che **assegna automaticamente** i parametri di configurazione per ogni host che si connette a una rete. Questi parametri includono:
- **Indirizzo IP**
- **Gateway predefinito** (router)
- **Server DNS**

Il DHCP è particolarmente utile nelle reti dove gli host cambiano frequentemente (reti domestiche, wireless, aziendali). Senza DHCP, sarebbe necessario **assegnare manualmente** ogni indirizzo IP, cosa impraticabile in reti di grandi dimensioni.

Gli indirizzi IP assegnati dal DHCP hanno una **scadenza** (lease time) e possono essere rinnovati prima della scadenza grazie ai meccanismi di **renewal** e **rebinding**.

---

## 🔄 Le 4 Fasi del DHCP (DORA)

Il processo di assegnazione di un indirizzo IP tramite DHCP avviene attraverso **quattro fasi fondamentali**, spesso ricordate con l'acronimo **DORA**:

### 1️⃣ DHCP DISCOVER (Scoperta)
**Cosa succede:**
- Il client, appena connesso, **non ha ancora un indirizzo IP**
- Invia un messaggio di **broadcast** (255.255.255.255) sulla rete locale per cercare un server DHCP
- Si identifica solo tramite il proprio **indirizzo MAC**

**Tipo:** Broadcast

**Scopo:** "C'è un server DHCP? Ho bisogno di un indirizzo IP!"

---

### 2️⃣ DHCP OFFER (Offerta)
**Cosa succede:**
- I server DHCP presenti rispondono con un **DHCPOFFER** in broadcast
- L'offerta contiene: IP proposto, subnet mask, gateway, DNS, lease time e MAC del destinatario

**Tipo:** Broadcast

**Scopo:** "Ecco, posso offrirti questo indirizzo IP con queste configurazioni!"

---

### 3️⃣ DHCP REQUEST (Richiesta)
**Cosa succede:**
- Il client **sceglie una delle offerte** (di solito la prima)
- Invia un **DHCPREQUEST** in broadcast per accettare l'offerta scelta e informare gli altri server

**Tipo:** Broadcast

**Scopo:** "Accetto l'offerta del server X! Voglio quell'indirizzo IP!"

---

### 4️⃣ DHCP ACKNOWLEDGEMENT (Conferma)
**Cosa succede:**
- Il server scelto invia un **DHCPACK** che conferma ufficialmente l'assegnazione
- Contiene tutti i parametri definitivi: IP, subnet mask, gateway, DNS, lease time
- Il client configura la propria interfaccia di rete con l'IP ricevuto

**Tipo:** Broadcast o unicast

**Scopo:** "Conferma ufficiale: l'indirizzo IP è tuo per la durata del lease!"

---

## 🔄 Macchina a Stati del Client DHCP

Il client DHCP attraversa diversi **stati** durante il ciclo di vita della sua configurazione IP.

### Stati Principali

#### **INIT (Initialization)**
- Stato iniziale quando il client viene avviato o perde il suo IP
- Il client **non ha un indirizzo IP** configurato
- Da qui parte il processo DORA inviando DISCOVER

#### **SELECT (Selecting)**
- Il client ha ricevuto uno o più **OFFER** dai server DHCP
- Deve **scegliere quale offerta accettare** e invia il REQUEST

#### **REQUEST (Requesting)**
- Il client ha inviato il REQUEST e **attende la conferma** (ACK) dal server
- Se riceve ACK → passa a BOUND
- Se riceve NACK o timeout → torna a INIT

#### **BOUND (Legato)**
- Il client ha ricevuto l'ACK e l'indirizzo IP è **attivo e utilizzabile**
- Rimane in questo stato per la maggior parte del lease time
- Quando scatta il timer T1 (50% del lease) → passa a RENEW

#### **RENEW (Rinnovo)**
- Il client cerca di **rinnovare il lease** con lo stesso server DHCP
- Invia REQUEST **unicast** direttamente al server originale
- Avviene quando è trascorso circa il **50% del lease time** (timer T1)
- Se rinnovo riuscito → torna a BOUND
- Se timer T2 scade → passa a REBIND

#### **REBIND (Riassociazione)**
- Il renewal con il server originale è **fallito**
- Il client cerca di rinnovare con **qualsiasi server DHCP** disponibile
- Invia REQUEST in **broadcast** sulla rete
- Avviene quando è trascorso circa l'**87,5% del lease time** (timer T2)
- Se trova un server → torna a BOUND
- Se lease scade completamente → torna a INIT

---

## ⏱️ Timer del DHCP

Il DHCP utilizza tre timer fondamentali per gestire il ciclo di vita dell'indirizzo IP:

### **Lease Time (Tempo di Concessione)**
- È la **durata totale** per cui l'indirizzo IP è assegnato al client
- Può variare da pochi minuti a diversi giorni, a seconda della configurazione del server
- Quando il lease scade completamente senza essere rinnovato, il client **perde l'indirizzo IP** e deve ricominciare da INIT
- Esempio: lease time = 24 ore

### **Renewal Timer (T1)**
- Scatta quando è trascorso circa il **50% del lease time**
- Quando scatta, il client passa allo stato **RENEW**
- Il client prova a rinnovare il lease contattando **direttamente il server DHCP originale** (comunicazione unicast)
- Esempio: se lease = 24 ore, T1 scatta dopo 12 ore

### **Rebinding Timer (T2)**
- Scatta quando è trascorso circa l'**87,5% del lease time**
- Se il renewal è fallito e T2 scatta, il client passa allo stato **REBIND**
- Il client prova a contattare **qualsiasi server DHCP** disponibile sulla rete (comunicazione broadcast)
- Esempio: se lease = 24 ore, T2 scatta dopo circa 21 ore

### Schema temporale
```
0%              50%                87.5%              100%
|----------------|-------------------|------------------|
    BOUND            RENEW              REBIND          INIT
               (timer T1)         (timer T2)      (lease scaduto)
```

Se tutti i tentativi falliscono e il lease scade al 100%, il client torna allo stato **INIT** e deve ricominciare il processo DORA dall'inizio.

---

## 🌐 DNS (Domain Name System)

### Cos'è il DNS?
Il **Domain Name System** è un sistema distribuito e gerarchico che **traduce i nomi di dominio leggibili** (come www.google.com) **negli indirizzi IP numerici** (come 142.250.184.132) che i computer usano per comunicare.

Definito negli **RFC 1034 e 1035**, il DNS è basato su un **modello Client/Server** ed è:
- **Distribuito:** i dati sono su migliaia di server nel mondo
- **Gerarchico:** organizzato in una struttura ad albero

Senza il DNS dovremmo ricordare indirizzi IP per ogni sito, rendendo Internet inutilizzabile.

---

## 🏗️ Componenti Principali del DNS

### 1. Domain Name Space (Spazio dei Nomi)
Struttura ad albero con livelli gerarchici:

- **Radice (Root - ".")**: vertice dell'albero, gestito dai Root Server
- **TLD (Top-Level Domain)**: .com, .org, .it, .edu
- **Domini registrati**: google.com, wikipedia.org
- **Sottodomini/Host**: www.google.com, mail.unibo.it

**Esempio gerarchia:**
```
. (radice) → .org → wikipedia.org → en.wikipedia.org
```

---

### 2. Name Server (Server DNS)
I Name Server gestiscono **zone** del Domain Name Space.

**Tipi:**
- **Root Name Server:** gestiscono i TLD, circa 13 gruppi (A-M) distribuiti globalmente
- **Authoritative Name Server:** hanno dati ufficiali di una zona specifica
- **Non-Authoritative:** hanno solo riferimenti o dati in cache

**Server Primario e Secondario:**
- Primario: dati originali della zona
- Secondario: copia dal primario per ridondanza

---

### 3. Resolver (Client DNS)
Il Resolver è il **client DNS** che fa richieste ai Name Server.

- Integrato nel sistema operativo
- Invia query DNS quando un'applicazione richiede la risoluzione di un nome
- Su Unix/Linux usa: `gethostbyname()` (nome → IP) e `gethostbyaddr()` (IP → nome)

---

## 🔍 Come Funziona la Risoluzione DNS

### Tipi di Query DNS

#### **Query Ricorsiva**
- Il client chiede al server di trovare la **risposta completa**
- Il server DNS contatta altri server se necessario
- Il client riceve una risposta definitiva (IP o errore)
- Usata dai resolver degli utenti finali

#### **Query Iterativa**
- Il server DNS risponde con ciò che sa o **indica dove cercare**
- Il client deve fare ulteriori query ad altri server
- Usata tra Name Server

**Schema tipico:**
- Resolver → DNS Server: query **ricorsiva**
- Name Server → altri Name Server: query **iterative**

---

## 📋 Esempio Pratico di Risoluzione: www.company.com

**1. Query al Default DNS Server**
- Il resolver invia la richiesta al DNS Server (es. 8.8.8.8 Google DNS)

**2. Query al Root Server**
- Se non ha la risposta in cache, il DNS Server interroga un Root Server
- Root risponde: "Per .com, chiedi al server TLD .com"

**3. Query al TLD .com**
- DNS Server chiede al TLD .com: "Dove trovo company.com?"
- TLD risponde: "Chiedi al Name Server autorevole di company.com"

**4. Query al Name Server Autorevole**
- DNS Server chiede al server autorevole: "Qual è l'IP di www.company.com?"
- Server autorevole risponde con l'IP definitivo (es. 203.0.113.45)

**5. Risposta al Client**
- Il DNS Server invia l'IP al resolver → browser può contattare il server web

**6. Caching**
- La risposta viene memorizzata in cache per il tempo indicato dal TTL

---

## 📦 Resource Record (RR) - Record di Risorsa

I Resource Record sono le **unità fondamentali** del DNS. Ogni RR contiene:

| Campo | Significato |
|-------|-------------|
| **Name** | Nome del dominio (es. www.example.com) |
| **Type** | Tipo di record (A, PTR, TXT, SOA, MX, ecc.) |
| **Class** | Contesto, quasi sempre **IN** (Internet) |
| **TTL** | Durata in secondi per cui il record può stare in cache |
| **RData** | Valore: IP, nome, testo, ecc. |

---

### Tipi Principali di Resource Record:

#### **A (Address)**
Associa un nome a un **indirizzo IPv4**

```
www.example.com.  IN  A  93.184.216.34
```

#### **AAAA**
Come A, ma per **indirizzi IPv6**

#### **PTR (Pointer)**
Risoluzione inversa: da **IP a nome**. Usa il dominio **in-addr.arpa**

```
34.216.184.93.in-addr.arpa.  IN  PTR  www.example.com.
```

#### **CNAME (Canonical Name)**
Crea un **alias** per un altro dominio

```
www.example.com.  IN  CNAME  server1.example.com.
```

#### **MX (Mail Exchange)**
Indica i **server di posta** con priorità (numero più basso = priorità più alta)

```
example.com.  IN  MX  10  mail1.example.com.
example.com.  IN  MX  20  mail2.example.com.
```

#### **TXT (Text)**
Testi associati al dominio (verifiche, SPF, DKIM)

```
example.com.  IN  TXT  "v=spf1 include:_spf.google.com ~all"
```

#### **NS (Name Server)**
Indica i Name Server autorevoli per una zona

```
example.com.  IN  NS  ns1.example.com.
```

#### **SOA (Start of Authority)**
Definisce l'autorità della zona (server primario, admin, serial, timer). Deve essere unico per zona.

---

## 🔄 Risoluzione Inversa nel DNS

La risoluzione inversa parte da un **IP** per ottenere il **nome di dominio**.

**Come funziona:**
- Usa record di tipo **PTR**
- Dominio speciale: **in-addr.arpa**
- L'IP viene **invertito**

**Perché invertire?**
- DNS: gerarchia da destra a sinistra (www.google.com → .com generico, google specifico)
- IP: da sinistra a destra (192.168.1.100 → 192 generico, 100 specifico)
- Invertendo l'IP si mantiene coerenza con la gerarchia DNS

**Esempio:**
- IP: 198.45.30.165
- Invertito: 165.30.45.198.in-addr.arpa
- Query PTR restituisce: pingu.di.school.it

---

## 📜 Formato dei Pacchetti DNS

Il DNS usa pacchetti per **query** e **reply**.

### Struttura Pacchetto:

**1. Header (12 byte)**
- **ID:** associa richiesta e risposta
- **Flag:** QR (query/risposta), AA (autorevole), RD (ricorsione richiesta), RA (ricorsione disponibile), Rcode (codice errore: 0=OK, 3=nome inesistente)
- **Contatori:** QDcount (query), ANcount (risposte), NScount (autorità), ARcount (info aggiuntive)

**2. Sezioni Variabili**
- **Query:** domanda (nome, tipo, classe)
- **Answer:** risposte alla query
- **Authority:** Name Server autorevoli
- **Additional:** info supplementari (es. IP dei NS)

---

## ⚙️ Regole Tecniche DNS e Porte

**Lunghezza nomi:**
- FQDN massimo: 255 caratteri
- Ogni label (tra i punti): massimo 63 caratteri

**Case-insensitive:**
- www.google.com = WWW.GOOGLE.COM

**Sottodomini:**
- blog.example.com richiede permesso di example.com, non di .com

**Punto finale:**
- www.ietf.org = www.ietf.org. (il punto indica la radice, è sottinteso)

**Porte e Protocolli:**
- **Porta 53**
- **UDP:** query normali (più veloce)
- **TCP:** zone transfer o risposte >512 byte

**Caching e TTL:**
- I server mantengono risposte in cache
- **TTL** indica durata validità (es. 300s = 5 min, 86400s = 24h)
- Risposta **autorevole**: dal server ufficiale
- Risposta **non autorevole**: dalla cache

---

# 📬 Application Layer - Protocolli

Il **livello Application** è il più vicino all'utente nel modello TCP/IP. Fornisce servizi direttamente alle applicazioni software.

## 🎯 Perché Tanti Protocolli Diversi?

Ogni protocollo nasce per **esigenze specifiche** di comunicazione:

| Protocollo | Scopo | Requisiti principali |
|------------|-------|---------------------|
| DNS | Risoluzione nomi → IP | Velocità, affidabilità |
| HTTP/HTTPS | Navigazione web | Flessibilità, sicurezza (HTTPS) |
| SMTP | Invio email | Push, affidabilità |
| POP3/IMAP | Ricezione email | Sincronizzazione (IMAP) |
| FTP | Trasferimento file | Velocità, due canali |
| SSH/Telnet | Accesso remoto | Sicurezza (SSH) |
| VoIP (SIP, RTP) | Chiamate vocali | Bassa latenza, tempo reale |

Il livello Application deve adattarsi a servizi diversi con requisiti specifici di **velocità, affidabilità, sicurezza e formato dati**.

---

## 🌐 HTTP e HTTPS

### HTTP (Hypertext Transfer Protocol)

**Scopo:** Trasferire documenti ipertestuali (pagine web) tra client e server

**Caratteristiche:**
- **Porta 80** (well known port)
- **Livello Application** del modello TCP/IP
- Usa **TCP** per garantire affidabilità (ordine, controllo errori)
- Protocollo **stateless** (ogni richiesta è indipendente)

**Perché TCP e non UDP?**
- Le pagine web sono documenti complessi
- La perdita di un pacchetto comprometterebbe l'intera risorsa
- TCP garantisce consegna completa e ordinata

---

### Struttura dei Messaggi HTTP

#### **REQUEST (Richiesta dal Client)**
```
GET /index.html HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0
Accept: text/html
```

**Componenti:**
- **Request Line:** metodo + risorsa + versione (GET /index.html HTTP/1.1)
- **Header:** informazioni aggiuntive (Host, User-Agent, Accept, Cookie, ecc.)
- **Body:** contiene dati, usato principalmente con POST/PUT

**Metodi principali:**
- **GET:** richiede una risorsa
- **POST:** invia dati al server
- **PUT:** aggiorna una risorsa
- **DELETE:** elimina una risorsa

#### **RESPONSE (Risposta dal Server)**
```
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 1234

<html>...</html>
```

**Componenti:**
- **Status Line:** versione + codice stato + messaggio (HTTP/1.1 200 OK)
- **Header:** info sul server, tipo contenuto, cookie
- **Body:** risorsa richiesta (HTML, immagine, JSON, ecc.)

---

### Codici di Stato HTTP

I codici di stato sono **numeri a tre cifre** che indicano l'esito della richiesta.

#### **2xx - Successo**
- **200 OK:** Richiesta soddisfatta, risorsa trovata e restituita

#### **3xx - Redirezione**
- **301 Moved Permanently:** Risorsa spostata permanentemente a nuovo URL
- **302 Found:** Risorsa spostata temporaneamente

#### **4xx - Errore Client**
- **400 Bad Request:** Richiesta malformata
- **401 Unauthorized:** Autenticazione richiesta ma non fornita/invalida
- **403 Forbidden:** Server rifiuta l'autorizzazione (accesso negato)
- **404 Not Found:** Risorsa non trovata (errore più comune)

#### **5xx - Errore Server**
- **500 Internal Server Error:** Errore generico sul server
- **503 Service Unavailable:** Server temporaneamente non disponibile (manutenzione/sovraccarico)

---

### HTTPS (HTTP Secure)

**Scopo:** Come HTTP ma con **crittografia e autenticazione**

**Caratteristiche:**
- **Porta 443** (well known port)
- Usa **TLS (Transport Layer Security)** per creare un canale cifrato
- Protegge da: intercettazioni, manomissioni, falsificazioni
- **Essenziale** per dati sensibili (credenziali, pagamenti, dati personali)

**Come funziona TLS:**
1. **Handshake:** client e server negoziano chiavi crittografiche
2. **Cifratura:** tutti i dati vengono cifrati
3. **Certificato digitale:** verifica l'identità del server

**Indicatori HTTPS nel browser:**
- Icona lucchetto nella barra indirizzi
- URL inizia con https://

---

## 📁 FTP (File Transfer Protocol)

**Scopo:** Trasferimento di file tra client e server

**Caratteristiche:**
- Nato negli anni '80 (RFC 959)
- Usa **TCP** per affidabilità
- **Due canali separati:**
  - **Porta 21:** canale di comando (controllo)
  - **Porta 20:** canale dati (trasferimento file)
- Comunicazione **unidirezionale** (o client→server o server→client, non contemporanea)

**Vantaggi:**
- Supporto tra sistemi operativi diversi (Linux, Windows, macOS)
- Integrazione in ogni linguaggio di programmazione
- Comunicazione con server, NAS, router

**Client FTP con interfaccia grafica:**
- **FileZilla** (limite 4 MB/s)
- **WinSCP** (solo Windows)

---

### FTP: Active Mode vs Passive Mode

#### **ACTIVE MODE (Modalità Attiva)**

**Funzionamento:**
1. Client si connette alla porta 21 del server (comandi)
2. Client apre porta locale N (>1023) per dati
3. Client invia comando PORT N al server
4. Server si connette dal suo porto 20 alla porta N del client

**Problema:**
- Il **server inizia connessione verso il client**
- Se il client ha un firewall, viene rilevato come **tentativo di intrusione** e bloccato

```
Client (porta N) ←── Server (porta 20)  ❌ Firewall blocca
```

#### **PASSIVE MODE (Modalità Passiva)**

**Funzionamento:**
1. Client apre due porte N e N+1 (>1023)
2. Client si connette alla porta 21 del server e invia comando PASV
3. Server apre porta casuale P (>1023) e la comunica al client
4. **Client inizia connessione** dalla sua porta N+1 alla porta P del server

**Vantaggio:**
- Il **client inizia tutte le connessioni** (dall'interno verso l'esterno)
- **Nessun problema con firewall**

```
Client (porta N+1) ──→ Server (porta P)  ✅ Firewall permette
```

**Impostazione in WinSCP:**
- Modalità predefinita: **Passive**
- Modificabile nelle impostazioni di connessione

---

### Accesso FTP

**Due modalità:**

1. **Accesso con credenziali:**
   - Username e password richiesti
   - Accesso a cartelle private/protette

2. **Accesso anonimo:**
   - Username: "anonymous"
   - Password: non richiesta o email
   - Usato per scambio dati pubblici

---

### Vulnerabilità FTP e Soluzioni

**Problemi di sicurezza:**
- ❌ **Password in chiaro:** viaggiano senza cifratura, facilmente intercettabili
- ❌ **Dati non cifrati:** file trasferiti senza protezione
- ❌ **Spreco di porte:** due connessioni per ogni sessione

**Soluzione: FTPS (FTP over TLS)**
- Aggiunge **crittografia TLS** al protocollo FTP
- Due varianti:
  - **EXPLICIT (porta 21):** client chiede connessione cifrata
  - **IMPLICIT (porta 990):** connessione cifrata automatica

**Esempio configurazione FTPS (WinSCP):**
```
Protocol: FTP
Encryption: TLS/SSL Explicit
Port: 21
Host: test.rebex.net
Username: demo
Password: password
```

---

## 📧 SMTP, POP3 e IMAP - Protocolli Email

### Sistema Email: Componenti

**Componenti principali:**
- **Mail Client (MUA):** programma dell'utente (Outlook, Thunderbird, Gmail web)
- **Mail Server:** gestisce caselle di posta, riceve e inoltra messaggi
- **Protocolli:**
  - **SMTP:** invio email
  - **POP3/IMAP:** ricezione email

**Indirizzo email:** nomeutente@dominio
- I server usano **DNS (record MX)** per trovare il server di destinazione

---

### SMTP (Simple Mail Transfer Protocol)

**Scopo:** Gestisce l'**invio** delle email dal mittente al destinatario

**RFC:** 821 (1982), 5321 (2008)

**Componenti del sistema:**
- **MUA (Mail User Agent):** client dell'utente
- **MSA (Mail Submission Agent):** riceve da MUA e prepara invio
- **MTA (Mail Transfer Agent):** inoltra messaggi tra server
- **MDA (Mail Delivery Agent):** consegna nella mailbox destinatario

**Fasi di invio:**
1. **Invio:** MUA → MSA → MTA mittente
2. **Transito:** MTA mittente ↔ MTA destinatario (porta 25, possibili relay)
3. **Ricezione:** MDA salva in mailbox → destinatario legge via POP3/IMAP

**Modalità di funzionamento:**
- SMTP funziona in **push** (spinge i messaggi)
- Comunica solo tra server per l'inoltro

---

### Sicurezza e Porte SMTP

**Problemi:**
- SMTP base **non ha autenticazione né crittografia**
- Vulnerabile a spoofing e spam

**Soluzione: TLS**
- Protegge i dati in transito

**Porte SMTP:**
- **25:** traffico tra server (relay MTA-MTA)
- **465:** SMTP su TLS **implicito** (connessione cifrata automatica)
- **587:** SMTP con **STARTTLS** (porta raccomandata, inizia cifrata su richiesta)

**Formato Email (RFC 5322):**
- **Header:** From, To, Subject, Date, Message-ID
- **Body:** testo del messaggio in ASCII 7-bit (per ridurre occupazione)
- **MIME:** estensione per allegati e contenuti multimediali

---

### POP3 (Post Office Protocol)

**Scopo:** **Scaricare** email dal server al dispositivo locale

**RFC:** 1939

**Caratteristiche:**
- Email **scaricate** sul computer e **cancellate** dal server (comportamento standard)
- Possibile configurare per lasciare copia sul server
- **Blocco mailbox** durante l'accesso (no accessi simultanei)
- Autenticazione: username e password **non cifrati** (a meno di TLS)

**Porte:**
- **110:** connessione standard (non cifrata)
- **995:** connessione sicura con TLS

**Vantaggi:**
- Lettura **offline**
- Email salvate localmente

**Svantaggi:**
- ❌ No sincronizzazione tra dispositivi
- ❌ Email cancellate dal server (accessibili solo da un dispositivo)
- ❌ No gestione cartelle sul server

**Quando usare POP3:**
- Vuoi leggere email su un solo dispositivo
- Vuoi conservare tutto in locale
- Non serve sincronizzazione

---

### IMAP4 (Internet Message Access Protocol)

**Scopo:** Leggere email **direttamente dal server** con sincronizzazione completa

**RFC:** 3501

**Caratteristiche:**
- Email **rimangono sul server** (client riceve copia)
- **Sincronizzazione in tempo reale** tra tutti i dispositivi
- Supporta modalità **online e offline**
- Accessi **simultanei** consentiti da più dispositivi/utenti
- Gestione **cartelle direttamente sul server**

**Porte:**
- **143:** connessione standard (non cifrata)
- **993:** connessione sicura con TLS

**Funzioni avanzate:**
- Download **parziale** dei messaggi (solo testo, solo header)
- Ideale per email con **allegati grandi** (scarichi solo ciò che serve)
- Traccia **stato messaggi** (letto, risposto, cancellato)
- Supporta struttura **MIME** (Multipurpose Internet Mail Extensions)

**Vantaggi:**
- ✅ Sincronizzazione completa
- ✅ Accesso da più dispositivi sempre aggiornati
- ✅ Gestione cartelle e organizzazione
- ✅ Risparmio spazio locale (allegati grandi restano sul server)

**Quando usare IMAP:**
- Usi email su più dispositivi (PC, telefono, tablet)
- Vuoi tutto sincronizzato
- Lavori con email pesanti

---

### Confronto POP3 vs IMAP4

| Caratteristica | POP3 | IMAP4 |
|----------------|------|-------|
| **Email sul server** | ❌ Cancellate (standard) | ✅ Rimangono |
| **Sincronizzazione** | ❌ No | ✅ Tempo reale |
| **Multi-dispositivo** | ❌ Difficile | ✅ Perfetto |
| **Accessi simultanei** | ❌ Blocco mailbox | ✅ Consentiti |
| **Gestione cartelle** | ❌ No | ✅ Sul server |
| **Download parziale** | ❌ No | ✅ Sì (MIME) |
| **Lettura offline** | ✅ Locale | ✅ Dopo sync |
| **Uso banda** | Basso | Medio-alto |
| **Spazio locale** | Alto (tutto scaricato) | Basso (solo cache) |

---

## 🔄 Interazione con i Livelli TCP/IP

Il modello TCP/IP è un'architettura a strati dove ogni livello collabora per la trasmissione dei dati.

**Livelli (dall'alto al basso):**

**1. Application Layer**
- HTTP/HTTPS, DNS, SMTP, POP3, IMAP, FTP
- Definisce significato e struttura dei messaggi
- Fornisce servizi alle applicazioni

**2. Transport Layer**
- **TCP:** affidabilità, ordine, controllo errori (HTTP, SMTP, FTP, DNS zone transfer)
- **UDP:** velocità, no controllo (DNS query, streaming, VoIP)
- Garantisce comunicazione end-to-end

**3. Internet Layer**
- **IP (Internet Protocol):** instradamento pacchetti attraverso la rete
- Trova il percorso verso la destinazione

**4. Network Access Layer**
- **Ethernet, Wi-Fi:** trasmissione fisica dei frame
- Gestisce la comunicazione sul mezzo fisico

**Esempio pratico (richiesta HTTP):**
```
1. Browser (Application) → richiesta HTTP "GET /index.html"
2. TCP (Transport) → suddivide in segmenti, garanzie di consegna
3. IP (Internet) → incapsula in pacchetti, instrada verso server
4. Ethernet (Network Access) → trasmette frame sul cavo/Wi-Fi
```

Ogni livello aggiunge le proprie informazioni (header) per garantire che il messaggio arrivi correttamente al destinatario.

---

## 🛠️ Strumenti di Analisi

**Browser Web:**
- Chrome, Firefox, Safari
- Principali utilizzatori di HTTP/HTTPS

**Strumenti da linea di comando:**
- **curl:** invia richieste HTTP/HTTPS manualmente
- **nslookup/dig:** interroga server DNS
- **ping:** verifica connettività
- **traceroute:** traccia percorso pacchetti

**Analisi di rete:**
- **Wireshark:** analizza pacchetti di rete in dettaglio
- Permette di vedere header, payload, sequenze TCP
- Utile per debug e studio dei protocolli

---

## 🎓 Conclusioni Application Layer

**Punti chiave:**
- Il livello Application è il **più vicino all'utente**
- Ogni protocollo è **specializzato** per un servizio specifico
- La **diversità di protocolli** riflette la varietà di esigenze applicative
- Nessun protocollo unico potrebbe coprire tutte le necessità
- Questa **specializzazione rende la rete robusta e versatile**

**Esempi di specializzazione:**
- **HTTP:** flessibile per qualsiasi contenuto web
- **SMTP:** ottimizzato per push di messaggi
- **IMAP:** progettato per sincronizzazione multi-dispositivo
- **FTP:** due canali per efficienza nel trasferimento file
- **DNS:** veloce, distribuito, essenziale per tutti gli altri protocolli

La semplicità e adattabilità di questi protocolli sono state cruciali per l'evoluzione del World Wide Web e di Internet come lo conosciamo oggi.