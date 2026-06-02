# APPUNTI SISTEMI E RETI - ESSENZIALE

## 1️⃣ LIVELLO TRASPORTO - BASI

**PORTE**
- Numeri 16 bit (0-65535) che identificano i processi
- Esempio: web server porta 80

**SOCKET**
- Socket = IP + Porta
- Esempio: 192.168.1.10:80

**MULTIPLEXING/DEMULTIPLEXING**
- **Multiplexing (TX)**: transport riceve dati e aggiunge header
- **Demultiplexing (RX)**: transport legge header e consegna alla socket giusta
- Permette a più applicazioni di condividere la connessione

**SERVIZI DEL LIVELLO TRASPORTO**
- Gestione connessioni (stabilire, mantenere, terminare)
- Segmentazione e riassemblaggio
- Controllo di flusso e congestione
- Multiplexing/demultiplexing

---

## 2️⃣ TCP vs UDP

| | TCP | UDP |
|---|---|---|
| **Tipo** | Connection-oriented | Connectionless |
| **Affidabilità** | ✅ Garantita | ❌ Best effort |
| **Ordine** | ✅ Garantito | ❌ No |
| **Velocità** | Più lento | Più veloce |
| **Header** | 20 byte | 8 byte |
| **Controllo flusso** | Sì | No |
| **Controllo congestione** | Sì | No |
| **Uso CPU/RAM** | Alto | Basso |
| **Applicazioni** | HTTP, FTP, SMTP | Streaming, VoIP, Gaming |

**Esempio:** TCP = raccomandata (sicura ma lenta), UDP = cartolina (veloce ma può perdersi)

---

## 3️⃣ TCP - CARATTERISTICHE

**COSA È TCP**
- Connection-oriented (serve handshake)
- Affidabile (garantisce consegna ordinata)
- Full-duplex (trasmissione/ricezione simultanea)
- Point-to-point (un mittente ↔ un destinatario)
- Data stream (flusso continuo di byte)

**STRUTTURA SEGMENTO TCP**
- Source/Destination Port
- Sequence Number (identifica byte inviati)
- Acknowledgment Number (conferma byte ricevuti)
- FLAGS (SYN, ACK, FIN, RST, PUSH, URG)
- Window Size (controllo di flusso)
- Checksum (verifica integrità)

**FLAG TCP**

| FLAG | VALORE | SIGNIFICATO |
|------|--------|-------------|
| **SYN** | 1 | Apertura connessione / "Voglio connettermi" |
| **ACK** | 1 | Conferma ricezione / "Ho ricevuto" |
| **FIN** | 1 | Chiusura connessione / "Ho finito" |
| **RST** | 1 | Reset/rifiuto / "Chiudo subito" |
| **PUSH** | 1 | Invio immediato senza buffer |
| **URG** | 1 | Dati urgenti |

---

## 4️⃣ THREE-WAY HANDSHAKE

**SCHEMA**
```
CLIENT                          SERVER
   |                               |
   |----[1] SYN=1, SEQ=X--------->|
   |                               |
   |<---[2] SYN=1, ACK=1,---------|
   |        SEQ=Y, ACK.N=X+1       |
   |                               |
   |----[3] ACK=1, ACK.N=Y+1----->|
   |                               |
   └──── CONNESSIONE ATTIVA ───────┘
```

**PASSO 1** - Client → Server
- SYN=1, SEQ=X (numero casuale)
- Primitiva: `connect()`
- "Voglio connettermi, parto dal byte X"

**PASSO 2** - Server → Client
- SYN=1, ACK=1, SEQ=Y, ACK.N=X+1
- Primitiva: `send()`
- "Accetto! Parto da Y, ho ricevuto X"
- Stabilisce direzione inversa (full-duplex)

**PASSO 3** - Client → Server
- ACK=1, ACK.N=Y+1
- Primitiva: `send()`
- "Ok, ho ricevuto Y"
- ✅ CONNESSIONE ATTIVA

**RIFIUTO CONNESSIONE**
- Se non c'è processo in ascolto → server invia RST=1

**PARAMETRI SCAMBIATI**

1. **MSS (Maximum Segment Size)**
   - Dimensione massima segmenti TCP
   - Formula: **MSS = min(MTU, MRU) - 20 byte**
   - MTU Ethernet = 1500 byte
   - Default = 536 byte
   - Si sceglie il minore tra i due host

2. **Window Size**
   - Dimensione buffer di ricezione
   - Indica quanti byte può accettare destinatario

3. **Sequence Number Iniziale**
   - Numero casuale per sicurezza (protegge da sequence guessing)
   - Serve per tracciare, riordinare, rilevare duplicati

**ESEMPIO**
- Client: SYN=1, SEQ=1000, MSS=1460, WS=65535
- Server: SYN=1, ACK=1, SEQ=5000, ACK.N=1001, MSS=1460, WS=8192
- Client: ACK=1, ACK.N=5001
- Risultato: MSS=1460, client invia max 8192 byte, server max 65535 byte

**PRIMITIVE TCP**
- `connect()` → Connection Request (SYN) → client richiede
- `accept()` → server accetta richieste
- `send()` → invia dati/risposte

---

## 5️⃣ AFFIDABILITÀ TCP

**COME TCP GARANTISCE AFFIDABILITÀ**

1. **Numeri di Sequenza**
   - Ogni byte ha un numero
   - Ricostruiscono messaggio originale
   - Riordinano segmenti ricevuti

2. **ACK (Acknowledgment)**
   - Destinatario conferma ricezione corretta
   - ACK.N = "ho ricevuto fino al byte N-1"

3. **Checksum**
   - Rileva errori nei dati
   - Segmento danneggiato → scartato

4. **Timeout e Ritrasmissione**
   - ACK non arriva → timeout → ritrasmissione
   - 3 ACK duplicati → ritrasmissione immediata (NACK implicito)

**RITRASMISSIONE**
- **Timeout scade**: nessun ACK ricevuto → rimanda
- **3 ACK uguali**: destinatario riceve fuori ordine → rimanda segmento perso

**Esempio:** Mittente manda [1][2][3], si perde [2]
- Destinatario: riceve 1, poi 3 → manda ACK(1), ACK(1), ACK(1)
- Mittente: riceve 3 ACK(1) → capisce che 2 si è perso → ritrasmette [2]

---

## 6️⃣ CONTROLLO DI FLUSSO - SLIDING WINDOW

**COS'È**
- Meccanismo a finestra scorrevole
- Dichiara numero massimo di byte inviabili prima di un ACK
- Lunghezza decisa dal buffer disponibile

**COME FUNZIONA**

1. Mittente invia segmenti dentro la finestra di trasmissione
2. Destinatario riceve, memorizza nel buffer, invia ACK
3. Mittente riceve ACK → finestra scorre avanti
4. Può trasmettere segmenti successivi

**Esempio:** Window = 3 segmenti
```
Mittente: [1][2][3] → invia
Destinatario: riceve, invia ACK(1,2,3)
Finestra scorre: ora può inviare [4][5][6]
```

**GESTIONE ERRORI**

**Segmento perso o ACK perso:**
- Mittente non riceve ACK → timeout
- Ritrasmette segmento
- Sliding window si **blocca** finché non riceve ACK

**NACK Implicito (ACK duplicato):**
- Destinatario riceve segmento fuori ordine
- Invia di nuovo ultimo ACK corretto
- Mittente riceve 3 ACK uguali → ritrasmette senza aspettare timeout

**VANTAGGI**
- Destinatario ordina correttamente i dati nel buffer
- Trasmissione ordinata e affidabile
- Efficiente: non aspetta ACK per ogni singolo byte

---

## 7️⃣ GESTIONE CONGESTIONE

**PROBLEMA**
- Troppi dati in transito → router non riescono a gestirli
- Pacchetti scartati quando coda router piena

**COME TCP RILEVA CONGESTIONE**
- **Timeout**: ACK non arriva → possibile congestione
- **3 ACK duplicati**: perdita pacchetti
- TCP assume congestione (controllo end-to-end, non nella rete)

**VARIABILI**

**Finestra di Congestione (cwnd)**
- Numero massimo byte non riscontrati nella rete
- Controllata dagli algoritmi di congestione

**Finestra di Ricezione (rwnd)**
- Advertised Window del destinatario
- Quanti byte può ricevere

**maxWindow = min(cwnd, rwnd)**
- Il mittente invia al massimo il valore minore

**Threshold (soglia)**
- Inizialmente 64 KB
- Separa slow start da congestion avoidance

**ALGORITMI (RFC 5681)**

**1. SLOW START**
- All'inizio connessione
- cwnd = valore iniziale piccolo
- Per ogni ACK → cwnd raddoppia
- **Crescita esponenziale**
- Continua fino a threshold

**2. CONGESTION AVOIDANCE**
- Dopo threshold
- Per ogni ACK → cwnd aumenta linearmente (+1 MSS)
- **Crescita lineare**
- Evita di sovraccaricare la rete

**3. GESTIONE TIMEOUT**
- Si verifica timeout (congestione grave)
- **threshold = cwnd / 2**
- **cwnd = valore iniziale**
- Riparte con Slow Start

**SCHEMA CRESCITA**
```
  cwnd
    ^
    |     /'''''''''''' Congestion Avoidance (lineare)
    |    /
    |   / Slow Start (esponenziale)
    |  /
    | /________ threshold (64KB)
    |/
    +------------------------> tempo
         ↑ timeout → riparte
```

**Esempio:**
- Inizio: cwnd = 1 MSS
- Slow Start: 1 → 2 → 4 → 8 → 16 → 32 → 64 (threshold)
- Congestion Avoidance: 65 → 66 → 67 → 68...
- Timeout a 70: threshold = 35, cwnd = 1
- Riparte Slow Start: 1 → 2 → 4 → 8 → 16 → 32 → 35 (threshold)
- Congestion Avoidance: 36 → 37 → 38...

---

## 8️⃣ UDP - USER DATAGRAM PROTOCOL

**CARATTERISTICHE**
- **Connectionless**: no handshake
- **Non affidabile**: no garanzie consegna/ordine
- **Best Effort**: come IP
- **No controllo** flusso/congestione
- **Multiplexing/Demultiplexing**: usa porte
- **Checksum**: opzionale (obbligatorio IPv6)

**STRUTTURA DATAGRAMMA**
Header 8 byte:
1. Source Port (16 bit)
2. Destination Port (16 bit)
3. Length (16 bit): 8-65535 byte totali
4. Checksum (16 bit): controllo integrità header, dati, pseudo-header IP

Dimensione massima effettiva: **65507 byte** (65535 - 8 UDP - 20 IP)

**UDP-LITE**
- Length sostituito con Checksum Coverage Length
- Indica quanti byte controllare (da 8 a tutto)
- Permette di usare parti non corrotte
- Utile per VoIP, streaming audio/video

**VANTAGGI**
- No ritardo connessione (no handshaking)
- Nessuno stato connessione → gestione efficiente molti client
- Overhead minimo (8 byte vs 20 TCP)
- Controllo totale da parte dell'applicazione
- Alta velocità → ideale real-time
- Supporto broadcast/multicast

**SVANTAGGI**
- Possibile perdita o disordine pacchetti
- Nessun controllo congestione → rischio saturare rete
- Applicazione deve gestire affidabilità ed errori
- Dimensione massima limitata

**CASI D'USO**
- Streaming multimediale: VoIP, videoconferenze, streaming live
- Gaming online: comunicazioni rapide, tolleranti perdite
- Broadcast/Multicast: IPTV, trasmissioni gruppo
- DNS: query veloci
- DHCP: configurazione rete

---

## 9️⃣ BUFFERIZZAZIONE TCP

**BUFFER DI TRASMISSIONE/RICEZIONE**
- Processo scrive dati in buffer
- TCP aggiunge header e invia
- Per ricevere: processo definisce buffer, affida gestione a TCP

**ACCESSO SINCRONO PORTE**
- Sistemi operativi gestiscono porte in modo sincrono
- Processo si blocca temporaneamente durante accesso

**SCARTO DATI**
Dati scartati se:
- Processo destinatario non pronto
- Porta non esiste
- Buffer di ricezione pieno

**INFORMAZIONI DI CONTROLLO**
- Source/Destination address
- Next packet sequence number
- Current buffer size
- Next write/read position
- Timeout/flag

**ECCEZIONI BUFFERIZZAZIONE**

**PUSH = 1**
- Invio immediato senza bufferizzazione
- TCP non aspetta di accumulare dati

**URG = 1**
- Trasmissione urgente
- Applicazione interrompe attività per gestire subito
- Dati urgenti processati prima

---

## 🎯 NUMERI DA RICORDARE

- Porte: **16 bit** (0-65535)
- Header TCP: **20 byte**
- Header UDP: **8 byte**
- MTU Ethernet: **1500 byte**
- MSS tipico: **1460 byte** (1500 - 40)
- MSS default: **536 byte** (576 - 20 - 20)
- Threshold iniziale: **64 KB**
- UDP max effettivo: **65507 byte**

**FORMULE**
- **MSS = min(MTU, MRU) - 20**
- **maxWindow = min(cwnd, rwnd)**
- **Timeout → threshold = cwnd/2, cwnd = inizio**

---

## 📝 SCHEMI DA SAPER DISEGNARE

**1. THREE-WAY HANDSHAKE**
```
CLIENT                    SERVER
  |-----SYN=1,SEQ=X------->|
  |<--SYN=1,ACK=1,SEQ=Y----|
  |   ACK.N=X+1            |
  |-----ACK=1,ACK.N=Y+1--->|
  └──CONNESSIONE ATTIVA────┘
```

**2. SLIDING WINDOW**
```
Mittente: [1][2][3] → invia (window=3)
Destinatario: riceve, ACK(1,2,3)
Finestra scorre: [4][5][6] → invia
```

**3. CONGESTIONE**
```
  cwnd
    ^     /''''''''  Congestion Avoidance
    |    /
    |   /  Slow Start
    |  /
    | /_____ threshold
    |/
    +----------> tempo
```

---

## 💡 ESEMPI PRATICI

**Handshake = telefonata**
1. "Pronto?" (SYN)
2. "Sì pronto, mi senti?" (SYN+ACK)
3. "Sì ti sento!" (ACK)

**Sliding Window = nastro trasportatore**
- 5 scatole alla volta
- Prima arriva → sesta parte
- Una cade → nastro si blocca

**Congestione = autostrada**
- Poche auto → acceleri (slow start)
- Traffico aumenta → rallenti (congestion avoidance)
- Incidente → riparti piano (timeout)

**TCP vs UDP = posta**
- TCP = raccomandata (sicura, lenta)
- UDP = cartolina (veloce, può perdersi)

**MSS = valigia aereo**
- Aereo A: max 20kg, Aereo B: max 15kg
- Scegli 15kg (il minore)