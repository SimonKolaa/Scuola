# Verifica Sistemi e Reti: Efficienza e Sicurezza nelle Reti Locali

## Concetti fondamentali di rete

### Dominio di Collisione

**Definizione breve**: Porzione di rete dove due frame possono collidere se trasmessi contemporaneamente.

**Spiegazione**:
- In una rete Ethernet, quando due dispositivi trasmettono contemporaneamente sullo stesso mezzo fisico, si verifica una **collisione**
- Il dominio di collisione è l'insieme di dispositivi che condividono lo stesso canale di comunicazione
- **Hub**: tutti i dispositivi collegati sono nello stesso dominio di collisione
- **Switch**: ogni porta crea un dominio di collisione separato
- Meno dispositivi nel dominio = meno collisioni = migliori prestazioni

**Segmentazione**:
- Si usa lo **switch** per dividere la rete in più domini di collisione
- Ogni porta dello switch = 1 dominio di collisione separato
- Ottimizza il traffico riducendo le collisioni

### Dominio di Broadcast

**Definizione breve**: Porzione di rete dove un messaggio broadcast raggiunge tutti i dispositivi.

**Spiegazione**:
- Area di rete dove un frame broadcast (indirizzo MAC FF:FF:FF:FF:FF:FF) viene ricevuto da tutti i dispositivi
- **Switch**: tutti i dispositivi collegati sono nello stesso dominio di broadcast
- **Router** o **VLAN**: dividono la rete in domini di broadcast separati
- Troppi broadcast riducono le prestazioni della rete

**Segmentazione**:
- Si usa **router** o **VLAN** per dividere i domini di broadcast
- Ogni VLAN = 1 dominio di broadcast separato
- Riduce il traffico broadcast inutile

### Broadcast Storm

**Definizione breve**: Situazione in cui i pacchetti broadcast si moltiplicano incontrollatamente causando il collasso della rete.

**Cause**:
- **Loop nella rete**: collegamenti ridondanti tra switch senza STP
- Frame broadcast che circolano all'infinito
- Gli switch inoltrano continuamente i broadcast su tutte le porte

**Conseguenze**:
- Saturazione della banda
- CPU degli switch al 100%
- Rete inutilizzabile
- Possibile crash dei dispositivi

**Soluzione**:
- **STP (Spanning Tree Protocol)**: blocca le porte ridondanti per eliminare i loop
- Configurazione corretta delle VLAN
- Monitoraggio del traffico di rete

**Come si sviluppa**:
1. Esiste un loop fisico tra switch (es. due collegamenti tra Switch A e Switch B)
2. Un frame broadcast entra nella rete
3. Lo switch lo inoltra su tutte le porte (incluso il secondo collegamento)
4. Il frame torna indietro attraverso il loop
5. Viene reinoltrato all'infinito
6. I frame si moltiplicano esponenzialmente
7. La rete collassa in pochi secondi

### Tabella MAC Address (Switch)

**Definizione**: Tabella che lo switch mantiene in memoria per sapere su quale porta inviare i frame.

**Contenuto**:
- Indirizzo MAC del dispositivo
- Porta dello switch a cui è collegato
- Timestamp (per aging/scadenza)

**Funzionamento**:
1. Lo switch riceve un frame
2. Legge l'indirizzo MAC sorgente e lo associa alla porta di entrata
3. Cerca l'indirizzo MAC destinazione nella tabella
4. Se lo trova, inoltra solo su quella porta
5. Se non lo trova, fa **flooding** (inoltra su tutte le porte tranne quella di origine)

**Aging**:
- Le entry hanno un timeout (default 300 secondi)
- Se un dispositivo non comunica, la entry viene rimossa
- Evita tabelle obsolete

### Riepilogo Domini

| Dispositivo | Dominio di Collisione | Dominio di Broadcast |
|-------------|----------------------|---------------------|
| Hub | 1 totale | 1 totale |
| Switch | 1 per porta | 1 totale |
| Router | 1 per porta | 1 per interfaccia |
| VLAN | 1 per porta | 1 per VLAN |

---

## STP - Spanning Tree Protocol

### Cos'è l'STP?
Il **Spanning Tree Protocol** serve per costruire un'alberatura gerarchica per gli switch, evitando loop nella rete.

### Come funziona?
- Gli switch si comunicano tra loro e rilevano la presenza di collegamenti multipli
- Decidono quali collegamenti bloccare e quali mantenere attivi
- Se un collegamento attivo smette di funzionare, sbloccano automaticamente quello precedentemente bloccato
- Il blocco avviene a livello software

### BPDU - Bridge Protocol Data Unit
Messaggi che gli switch si scambiano per costruire l'alberatura gerarchica dello STP.

### Processo di costruzione
1. **Elezione del Root Switch**: lo switch più vicino al router
2. **Elezione dei Designated Switch**: gli switch più vicini al root (possono essere più di uno)
3. **Obiettivo finale**: determinare quali collegamenti sono attivi e quali bloccati

### Stati delle porte
- **Learning**: lo switch sta calcolando cosa fare con le porte
- **Listening**: attende informazioni sullo stato delle connessioni
- **Forwarding**: porta attiva (trasmette dati)
- **Blocking**: bloccata automaticamente dallo switch
- **Disabled**: disabilitata manualmente dall'amministratore

### Ruoli delle porte in STP
- **Root Port**: porta che offre il percorso migliore verso il root bridge
- **Designated Port**: porta attiva che inoltra il traffico verso il segmento
- **Blocked Port**: porta bloccata per evitare loop
- **Backup Port**: porta alternativa sulla stessa rete (usata in RSTP)

---

## RSTP - Rapid Spanning Tree Protocol

### Definizione breve
**RSTP** è l'evoluzione di STP (IEEE 802.1w) che riduce i tempi di convergenza della rete da 30-50 secondi a pochi secondi.

### Differenze con STP
- **Convergenza più rapida**: pochi secondi invece di 30-50 secondi
- **Meno stati delle porte**: solo 3 stati invece di 5
- **Migliore gestione dei link ridondanti**

### Stati delle porte in RSTP
- **Discarding**: equivalente a Blocking, Listening e Disabled in STP
- **Learning**: uguale a STP
- **Forwarding**: uguale a STP

### Porte di Backup in RSTP
- **Alternate Port**: backup della root port, pronta ad attivarsi se la root port fallisce
- **Backup Port**: backup di una designated port sullo stesso segmento

### Vantaggi
- Convergenza quasi istantanea in caso di guasto
- Migliore utilizzo della ridondanza
- Standard moderno per reti enterprise

---

## VLAN - Virtual LAN

### Definizione breve
Le **VLAN** (Virtual Local Area Network) sono reti locali virtuali che permettono di segmentare logicamente una rete fisica in più reti separate, isolando il traffico broadcast.

### Definizione completa
Le **VLAN** permettono di creare sottoreti logiche nella rete locale che esistono solo a livello di configurazione degli switch, mantenendo la stessa topologia fisica ma cambiando quella logica.

### Vantaggi
- Segmentazione della rete in domini di broadcast separati
- Maggiore sicurezza
- Migliore gestione del traffico
- Implementazione di funzioni del livello Network (sicurezza, QoS)
- Riduzione del traffico broadcast
- Flessibilità nella gestione della rete

### Modalità di creazione
- **Per gruppi di porte**: modalità più comune
- **Per utenti**: tramite indirizzo MAC dell'host
- **Per protocolli**: usando indirizzi logici (es. IP)

---

## IEEE 802.1Q - VLAN Tagging

### Definizione breve
**IEEE 802.1Q** è lo standard che definisce come vengono taggati i frame Ethernet per identificare a quale VLAN appartengono.

### Come funziona
- Aggiunge un **tag di 4 byte** nell'header del frame Ethernet
- Il tag viene inserito tra l'indirizzo MAC sorgente e il campo Type/Length
- Permette agli switch di identificare a quale VLAN appartiene un frame

### Struttura del tag 802.1Q (4 byte)

#### TPID - Tag Protocol Identifier (2 byte)
- **Valore fisso**: 0x8100
- Identifica il frame come tagged 802.1Q
- Permette agli switch di riconoscere che è presente un tag VLAN

#### TCI - Tag Control Information (2 byte)
Composto da tre campi:

1. **PCP - Priority Code Point (3 bit)**
   - Indica la priorità del frame (QoS)
   - Valori da 0 a 7

2. **DEI - Drop Eligible Indicator (1 bit)**
   - Indica se il frame può essere scartato in caso di congestione

3. **VID - VLAN ID (12 bit)**
   - Identifica la VLAN di appartenenza
   - Valori da 0 a 4095
   - **VLAN 0**: usata per priorità ma non per identificazione
   - **VLAN 1**: VLAN di default (management)
   - **VLAN 2-1001**: VLAN normali
   - **VLAN 1002-1005**: riservate per Token Ring e FDDI
   - **VLAN 1006-4094**: VLAN estese
   - **VLAN 4095**: riservata

### Perché serve il protocollo nelle VLAN?
Il protocollo (IEEE 802.1Q) serve per:
- **Identificare** a quale VLAN appartiene un frame quando viaggia tra switch
- **Mantenere la separazione** del traffico anche su collegamenti condivisi (trunk)
- **Permettere la comunicazione** tra switch diversi mantenendo le VLAN
- **Garantire** che il traffico di una VLAN non venga inviato a porte di altre VLAN

---

## Porte Trunk e Access

### Porte Access
**Definizione breve**: Porta che appartiene a una singola VLAN e rimuove/aggiunge il tag VLAN.

**Caratteristiche**:
- Connettono dispositivi end-user (PC, stampanti, telefoni IP)
- Appartengono a **una sola VLAN**
- **Rimuovono** il tag 802.1Q dai frame in uscita
- **Aggiungono** il tag 802.1Q ai frame in entrata
- I dispositivi collegati non vedono i tag VLAN

**Esempio**: PC collegato alla porta Fa0/1 configurata come access sulla VLAN 10

### Porte Trunk
**Definizione breve**: Porta che trasporta traffico di multiple VLAN mantenendo i tag 802.1Q.

**Caratteristiche**:
- Connettono **switch tra loro** o switch con router
- Trasportano traffico di **multiple VLAN contemporaneamente**
- **Mantengono** i tag 802.1Q sui frame
- Permettono la comunicazione inter-switch preservando le VLAN

**Native VLAN**:
- VLAN il cui traffico viaggia **senza tag** sul trunk
- Di default è la VLAN 1
- Usata per compatibilità con dispositivi che non supportano 802.1Q
- **Importante**: deve essere la stessa su entrambi i lati del trunk

**Esempio**: Collegamento tra Switch1 e Switch2 che trasporta VLAN 10, 20, 30

### Differenza fondamentale
| Caratteristica | Access | Trunk |
|----------------|--------|-------|
| VLAN supportate | Una sola | Multiple |
| Tag 802.1Q | Rimosso | Mantenuto |
| Connessione tipica | End device | Switch-to-switch |
| Frame inviati | Untagged | Tagged (tranne native) |

---

## VTP - VLAN Trunking Protocol

### Definizione breve
**VTP** è un protocollo proprietario Cisco che sincronizza automaticamente le configurazioni VLAN tra gli switch di una rete.

### Come funziona VTP

#### Scopo
- **Centralizzare** la gestione delle VLAN
- **Propagare** automaticamente le modifiche VLAN a tutti gli switch
- **Ridurre** gli errori di configurazione manuale
- **Semplificare** l'amministrazione in reti con molti switch

#### Componenti

**VTP Domain**:
- Nome che identifica un gruppo di switch che condividono le stesse VLAN
- Gli switch devono essere nello stesso dominio per scambiarsi informazioni VTP

**VTP Password** (opzionale):
- Autenticazione per le comunicazioni VTP
- Protezione contro modifiche non autorizzate

**Configuration Revision Number**:
- Numero incrementale che indica la "versione" della configurazione VLAN
- Ogni modifica incrementa questo numero
- Lo switch con il numero più alto sovrascrive gli altri

#### Modalità VTP

**1. Server Mode**
- Può **creare, modificare, eliminare** VLAN
- **Propaga** le modifiche agli altri switch
- **Sincronizza** le VLAN con gli altri switch
- Salva la configurazione VLAN in NVRAM
- Modalità di default

**2. Client Mode**
- **Non può** modificare le VLAN
- **Riceve** e applica gli aggiornamenti dai server
- **Propaga** gli aggiornamenti ad altri switch
- **Non salva** la configurazione VLAN in NVRAM (solo in RAM)

**3. Transparent Mode**
- Può **creare, modificare, eliminare** VLAN **localmente**
- **Non partecipa** alla sincronizzazione VTP
- **Inoltra** i messaggi VTP ma non li applica
- Salva la configurazione VLAN in NVRAM
- Le VLAN create sono solo locali

**4. Off Mode** (VTP v3)
- VTP completamente disabilitato
- Non inoltra messaggi VTP

#### Processo di sincronizzazione

1. **Modifica VLAN** su uno switch in modalità Server
2. Il **revision number** viene incrementato
3. Lo switch Server invia un **VTP Summary Advertisement**
4. Gli switch Client ricevono il messaggio
5. Se il revision number è **più alto** del loro, richiedono i dettagli
6. Lo switch Server invia i **VTP Subset Advertisements** con tutti i dettagli
7. Gli switch Client **applicano le modifiche**
8. Tutti gli switch si **sincronizzano** con la nuova configurazione

#### Messaggi VTP

**Summary Advertisement**:
- Inviato ogni 5 minuti o dopo una modifica
- Contiene: domain name, revision number, timestamp

**Subset Advertisement**:
- Inviato dopo una modifica VLAN
- Contiene i dettagli delle VLAN (ID, nome, tipo)

**Advertisement Request**:
- Richiesto da uno switch che ha revision number più basso
- Chiede l'invio dei subset advertisement

#### VTP Pruning
- **Ottimizzazione** del traffico trunk
- Impedisce l'invio di frame broadcast/multicast su trunk dove non ci sono porte attive per quella VLAN
- Riduce il traffico non necessario

### Vantaggi VTP
- Configurazione centralizzata
- Consistenza tra switch
- Riduzione errori manuali
- Facilità di gestione reti grandi

### Svantaggi e rischi VTP
- **Rischio di sovrascrittura**: uno switch con revision number alto può cancellare tutte le VLAN
- Dipendenza da un protocollo proprietario Cisco
- Complessità nella risoluzione problemi

### Best practice
- Usare VTP Transparent in ambienti di produzione
- Impostare password VTP
- Documentare il dominio VTP
- Reset del revision number prima di aggiungere nuovi switch

---

## FIREWALL

### Definizione breve
**Firewall** è un dispositivo di sicurezza che monitora e controlla il traffico di rete in entrata e in uscita, bloccando o permettendo pacchetti secondo regole di sicurezza predefinite.

### Definizione completa
Dispositivo (hardware o software) che **blocca/filtra i pacchetti entranti e uscenti** dalla rete o dal computer secondo regole prestabilite (policy).

### Tre categorie principali

#### 1. Application Level Firewall
- Opera a livello applicativo
- Indaga fino ai livelli più alti dello stack
- Riesce a leggere il contenuto dei messaggi

#### 2. Packet Filter Firewall
- Opera a livello Network (livello 3)
- Blocca in base agli indirizzi IP

#### 3. Stateful Packet Inspection Firewall
- Opera a livello Transport (livello 4)
- Via di mezzo tra i due precedenti
- Blocca in base alle porte

---

## ACL - Access Control List

### Definizione breve
**ACL** sono liste di regole che determinano quali pacchetti di rete vengono permessi o bloccati, basandosi su criteri come IP sorgente, IP destinazione, protocollo e porte.

### Definizione completa
**Liste di controllo degli accessi**: regole (policy) che definiamo per controllare il traffico di rete.

### Funzionamento
- Utilizzo di **whitelist** (permessi) e **blacklist** (blocchi)
- Esempi di regole: bloccare/permettere specifici IP, porte, protocolli

### Regola importante
**L'ordine delle regole è fondamentale**: appena viene trovata una regola valida, il controllo si ferma.
- Le regole più stringenti vanno inserite in cima alla lista
- Le regole più generiche vanno alla fine

### Tipi di ACL
- **ACL Standard**: filtrano solo in base all'indirizzo IP sorgente
- **ACL Estese**: filtrano in base a IP sorgente, IP destinazione, protocollo e porte

---

## PROXY SERVER

### Definizione breve
**Proxy Server** è un intermediario che si frappone tra client e server, inoltrando richieste e risposte per fornire funzionalità come caching, filtro contenuti e anonimato.

### Definizione completa
Programma (o hardware dedicato) che **si interpone tra client e server**, fungendo da intermediario.

### Funzionalità principali

#### 1. Connettività
Garantisce l'accesso a Internet per i client della rete locale

#### 2. Caching
- Salva le risposte già richieste
- Se la richiesta è già in cache, risponde direttamente senza contattare il server
- Riduce la congestione della rete

#### 3. Privacy
- Offre il proprio IP per mascherare quello del client
- Aumenta l'anonimato

#### 4. Logging/Monitoraggio
- Registra le richieste ai siti web
- Utile per controllo e statistiche

### Topologie di rete con proxy

#### Single Proxy Topology
Un singolo proxy per tutta la rete

#### Multiple Proxy Vertically Topology
- Ogni sottorete ha il proprio proxy secondario
- Tutti i proxy secondari passano attraverso un proxy primario
- Struttura gerarchica

#### Multiple Proxy Horizontally Topology
- I proxy secondari comunicano tra loro
- Bilanciamento del carico di lavoro
- Svantaggio: maggior traffico sulla rete

---

## NAT - Network Address Translation

### Definizione breve
**NAT** è una tecnica che traduce indirizzi IP privati in indirizzi IP pubblici, permettendo a dispositivi con IP privati di comunicare su Internet usando pochi IP pubblici.

### Problema da risolvere
Gli indirizzi IPv4 privati non possono essere utilizzati direttamente su Internet, e gli indirizzi pubblici disponibili sono limitati.

### Soluzione NAT
Permette a una rete locale con indirizzi IP privati di accedere a Internet usando uno o più IP pubblici forniti dall'ISP.

### Come funziona
- Il router mantiene una **tabella di traduzione**
- Associa socket interni (IP privato + porta) con socket esterni (IP pubblico + porta)
- **Socket** = protocollo + indirizzo IP + porta di comunicazione

### Tipi di NAT

#### NAT Statico
- Rapporto 1:1 tra IP privato e IP pubblico
- Ogni client ha un IP pubblico dedicato
- Costoso

#### NAT Dinamico
- Il router dispone di un pool di indirizzi IP pubblici
- Assegna dinamicamente gli IP disponibili ai client
- Più economico dello statico ma comunque costoso

---

## PAT - Port Address Translation

### Definizione breve
**PAT** è un'estensione di NAT che usa anche le porte per permettere a migliaia di dispositivi di condividere un singolo indirizzo IP pubblico.

### Problema da risolvere
Con il NAT semplice, quando due client fanno la stessa richiesta allo stesso server, il router non sa a quale client restituire la risposta.

### Soluzione PAT
Permette al router di utilizzare **un singolo indirizzo IP pubblico** per gestire oltre **64.000 connessioni private contemporaneamente**.

### Come funziona
- Il router modifica anche le **porte** oltre agli IP
- Quando due client fanno la stessa richiesta, usa porte diverse
- Rapporto 1:N tra IP pubblico e IP privati
- Mantiene una tabella con: IP privato, porta privata, IP pubblico, porta pubblica

### Vantaggi
- Massima efficienza nell'uso degli IP pubblici
- Soluzione più economica
- Standard per reti domestiche e aziendali

---

## DMZ - DeMilitarized Zone

### Definizione breve
**DMZ** è una sottorete isolata che espone servizi esterni mantenendo protetta la rete interna, fungendo da zona cuscinetto tra Internet e la LAN aziendale.

### Definizione completa
**Area all'interno della rete locale** dove il traffico è volutamente controllato e limitato, sia dalla WAN che dalla LAN.

### Scopo
- Sezionare la rete
- Isolare risorse importanti
- Proteggere la rete interna

### Utilizzi tipici
- **Server pubblici**: web server, mail server, FTP server
- **Posta elettronica**
- **Application Server** accessibili dall'esterno
- **Stanza server** con dati sensibili

### Tipi di DMZ

#### 1. DMZ "Vicolo cieco"
- Un firewall con tre interfacce: WAN, LAN, DMZ
- La DMZ è collegata direttamente al firewall
- Configurazione più semplice

#### 2. DMZ "Zona cuscinetto"
- Due firewall separati: External Firewall e Internal Firewall
- La DMZ si trova tra i due firewall
- Maggiore sicurezza: anche se la DMZ viene compromessa, la LAN interna resta protetta

### Regole tipiche
- Traffico WAN → DMZ: permesso solo su porte specifiche (es. 80, 443 per web)
- Traffico DMZ → LAN: molto limitato o bloccato
- Traffico LAN → DMZ: permesso per amministrazione

---

## Riepilogo: Sicurezza a livelli

1. **STP**: Previene loop a livello fisico/data link
2. **VLAN**: Segmenta logicamente la rete
3. **Firewall**: Filtra il traffico tra zone di sicurezza diverse
4. **ACL**: Definisce regole specifiche di accesso
5. **Proxy**: Intermedia e controlla il traffico applicativo
6. **NAT/PAT**: Nasconde la struttura della rete interna
7. **DMZ**: Isola i servizi pubblici dalla rete interna

Ogni tecnologia contribuisce a creare una **difesa in profondità** (defense in depth), aumentando complessivamente la sicurezza della rete.

---

## Note per la verifica

### Concetti chiave da ricordare

**Domini di rete**
- **Dominio di collisione**: area dove i frame possono collidere - switch crea domini separati (1 per porta)
- **Dominio di broadcast**: area raggiunta da broadcast - router/VLAN creano domini separati
- **Broadcast storm**: loop che moltiplica all'infinito i broadcast - risolto con STP
- **Tabella MAC**: switch memorizza MAC address + porta per inoltrare correttamente

**STP e RSTP**
- BPDU, Root Switch, Designated Switch
- Stati STP: Learning, Listening, Forwarding, Blocking, Disabled
- Stati RSTP: Discarding, Learning, Forwarding
- Porte: Root Port, Designated Port, Alternate Port (RSTP), Backup Port (RSTP)
- RSTP converge in pochi secondi vs 30-50 secondi di STP

**VLAN**
- Segmentazione logica (stessa topologia fisica, diversa topologia logica)
- Layer 3 switching
- IEEE 802.1Q: standard per VLAN tagging
- TPID (0x8100) + VID (12 bit, 0-4095)
- Native VLAN: traffico senza tag sul trunk (default VLAN 1)

**Porte Trunk vs Access**
- Access: 1 VLAN, rimuove tag, per end device
- Trunk: multiple VLAN, mantiene tag, per switch-to-switch

**VTP**
- Modalità: Server, Client, Transparent, Off
- Configuration Revision Number: chi ha il numero più alto vince
- VTP Domain e Password
- VTP Pruning: ottimizza traffico trunk

**Firewall**
- Tre tipi: Application Level, Packet Filter, Stateful Packet Inspection
- Operano a livelli diversi dello stack TCP/IP

**ACL**
- Ordine delle regole è fondamentale
- Standard vs Estese

**Proxy**
- Caching, Privacy, Logging, Connettività
- Topologie: Single, Vertical, Horizontal

**NAT/PAT**
- NAT: traduzione IP (1:1 o dinamico)
- PAT: traduzione porta (1:N, fino a 64k connessioni)
- Socket = protocollo + IP + porta

**DMZ**
- Vicolo cieco (1 firewall) vs Zona cuscinetto (2 firewall)
- Isola servizi pubblici dalla rete interna

### Tabella riepilogativa IEEE 802.1Q

| Campo | Dimensione | Descrizione | Valori |
|-------|-----------|-------------|---------|
| TPID | 2 byte | Tag Protocol ID | 0x8100 |
| PCP | 3 bit | Priority Code Point | 0-7 |
| DEI | 1 bit | Drop Eligible Indicator | 0-1 |
| VID | 12 bit | VLAN ID | 0-4095 |

### Differenze chiave

| Aspetto | STP | RSTP |
|---------|-----|------|
| Standard | IEEE 802.1D | IEEE 802.1w |
| Convergenza | 30-50 sec | 1-6 sec |
| Stati porte | 5 | 3 |
| Backup ports | No | Sì |

| Tipo porta | VLAN | Tag | Connessione |
|------------|------|-----|-------------|
| Access | 1 | Rimosso | End device |
| Trunk | Multiple | Mantenuto | Switch-to-switch |

| VTP Mode | Crea VLAN | Propaga | Applica | Salva NVRAM |
|----------|-----------|---------|---------|-------------|
| Server | Sì | Sì | Sì | Sì |
| Client | No | Sì | Sì | No |
| Transparent | Sì (locale) | Sì | No | Sì |
| Off | No | No | No | No |
