# Guida al Subnetting Semplice

## 📚 TEORIA DI BASE

### Cos'è il Subnetting?

Il **subnetting** è la tecnica che permette di dividere una rete IP in sottoreti più piccole per organizzare meglio i dispositivi e ottimizzare l'uso degli indirizzi IP.

### Struttura di un Indirizzo IP (Classe C)

Un indirizzo IP è composto da 4 byte (32 bit totali):

```
192.168.10.0
 |   |   |  |
 3 byte    1 byte
(24 bit)  (8 bit)
 RETE     HOST
```

- **Parte di RETE** (primi 3 byte): identifica la rete principale
- **Parte di HOST** (ultimo byte): identifica i dispositivi nella rete

### Subnet Mask

La **subnet mask** indica quali bit dell'indirizzo appartengono alla rete e quali agli host.

**Subnet mask di default per Classe C:**
```
255.255.255.0
= 11111111.11111111.11111111.00000000
```

I bit a 1 indicano la parte di RETE, i bit a 0 indicano la parte di HOST.

---

## 🔧 COME FARE SUBNETTING

### STEP 1: Decidere quante sottoreti servono

Formula: **2^n = numero di sottoreti**

Dove **n** = numero di bit che "prendo in prestito" dalla parte host.

**Esempi:**
- 1 bit → 2^1 = 2 sottoreti
- 2 bit → 2^2 = 4 sottoreti
- 3 bit → 2^3 = 8 sottoreti

### STEP 2: Calcolare quanti host per sottorete

Formula: **2^m - 2 = host utilizzabili**

Dove **m** = bit rimanenti per gli host.

Il "-2" è perché devi togliere:
1. L'indirizzo di rete (primo indirizzo)
2. L'indirizzo di broadcast (ultimo indirizzo)

**Esempi con 8 bit disponibili:**
- Uso 2 bit per subnet → rimangono 6 bit per host → 2^6 - 2 = 62 host
- Uso 3 bit per subnet → rimangono 5 bit per host → 2^5 - 2 = 30 host

### STEP 3: Calcolare la nuova subnet mask

Devi mettere a 1 i bit che usi per le sottoreti.

**Esempio con 2 bit per subnet:**
```
Default:  11111111.11111111.11111111.00000000 = 255.255.255.0
Nuova:    11111111.11111111.11111111.11000000 = 255.255.255.192
                                       ^^
                                       2 bit presi
```

**Conversione binario → decimale:**
```
11000000 = 128 + 64 = 192
```

### STEP 4: Trovare gli indirizzi di rete

Il "salto" tra una sottorete e l'altra si calcola con: **256 - ultimo_otteto_mask**

**Esempio con mask 255.255.255.192:**
- Salto = 256 - 192 = 64
- Le sottoreti partiranno da: 0, 64, 128, 192

---

## 📊 CONVERSIONI BINARIO ↔ DECIMALE

### DECIMALE → BINARIO

**Metodo:** Dividi per 2 e prendi i resti al contrario.

**Esempio: 49 in binario**
```
49 ÷ 2 = 24  resto 1 ← LSB (bit meno significativo)
24 ÷ 2 = 12  resto 0
12 ÷ 2 = 6   resto 0
6 ÷ 2 = 3    resto 0
3 ÷ 2 = 1    resto 1
1 ÷ 2 = 0    resto 1 ← MSB (bit più significativo)

Risultato: 110001
```

### BINARIO → DECIMALE

**Metodo:** Usa le potenze di 2.

**Posizioni dei bit:**
```
Bit:     7    6    5    4    3    2    1    0
Valore: 128  64   32   16   8    4    2    1
```

**Esempio: 11000111 in decimale**
```
1×128 + 1×64 + 0×32 + 0×16 + 0×8 + 1×4 + 1×2 + 1×1
= 128 + 64 + 4 + 2 + 1
= 199
```

---

## 🎯 ESERCIZIO GUIDATO

### TRACCIA

Hai la rete **192.168.20.0/24** e devi crearla in **4 sottoreti**.

Trova per ogni sottorete:
- Indirizzo di rete
- Primo host
- Ultimo host
- Broadcast
- Subnet mask

---

### SOLUZIONE PASSO-PASSO

#### PASSO 1: Quanti bit servono?

Per 4 sottoreti: **2^n = 4** → **n = 2 bit**

Prendo in prestito 2 bit dalla parte host.

#### PASSO 2: Quanti host per sottorete?

Bit disponibili per host: 8 - 2 = **6 bit**

Host utilizzabili: **2^6 - 2 = 64 - 2 = 62 host**

#### PASSO 3: Calcolare la subnet mask

```
Default:  11111111.11111111.11111111.00000000
Nuova:    11111111.11111111.11111111.11000000
                                       ^^
                                       2 bit per subnet
```

**Conversione ultimo otteto:**
```
11000000 = 128 + 64 = 192
```

**Subnet mask:** 255.255.255.192 o **/26** (24 bit di rete + 2 bit subnet)

#### PASSO 4: Calcolare il salto tra sottoreti

Salto = 256 - 192 = **64**

Le sottoreti partiranno da: **0, 64, 128, 192**

---

### 🎯 RISULTATI FINALI

#### **SOTTORETE 1**
```
Indirizzo di rete:     192.168.20.0
Primo host:            192.168.20.1
Ultimo host:           192.168.20.62
Broadcast:             192.168.20.63
Subnet mask:           255.255.255.192 (/26)
Range:                 192.168.20.0 - 192.168.20.63
```

#### **SOTTORETE 2**
```
Indirizzo di rete:     192.168.20.64
Primo host:            192.168.20.65
Ultimo host:           192.168.20.126
Broadcast:             192.168.20.127
Subnet mask:           255.255.255.192 (/26)
Range:                 192.168.20.64 - 192.168.20.127
```

#### **SOTTORETE 3**
```
Indirizzo di rete:     192.168.20.128
Primo host:            192.168.20.129
Ultimo host:           192.168.20.190
Broadcast:             192.168.20.191
Subnet mask:           255.255.255.192 (/26)
Range:                 192.168.20.128 - 192.168.20.191
```

#### **SOTTORETE 4**
```
Indirizzo di rete:     192.168.20.192
Primo host:            192.168.20.193
Ultimo host:           192.168.20.254
Broadcast:             192.168.20.255
Subnet mask:           255.255.255.192 (/26)
Range:                 192.168.20.192 - 192.168.20.255
```

---

## 📝 SCHEMA RAPIDO PER OGNI SOTTORETE

Una volta che hai l'**indirizzo di rete** (es. 192.168.20.64):

```
Network Address:       N (192.168.20.64)
Primo Host:            N + 1 (192.168.20.65)
Ultimo Host:           N + 62 (192.168.20.126)
Broadcast:             N + 63 (192.168.20.127)
Prossima Sottorete:    N + 64 (192.168.20.128)
```

Dove il numero da sommare dipende dal salto calcolato (256 - ultimo otteto mask).

---

## 🔑 FORMULE CHIAVE DA RICORDARE

| Cosa | Formula |
|------|---------|
| Numero sottoreti | 2^n (n = bit per subnet) |
| Host utilizzabili | 2^m - 2 (m = bit per host) |
| Salto tra subnet | 256 - ultimo_otteto_mask |
| Primo host | Network + 1 |
| Ultimo host | Broadcast - 1 |
| Broadcast | Network + (salto - 1) |

---

## 💡 TRUCCHI VELOCI

### Valori comuni delle subnet mask:
```
/24 = 255.255.255.0    → 0 bit subnet, 8 bit host → 1 rete, 254 host
/25 = 255.255.255.128  → 1 bit subnet, 7 bit host → 2 reti, 126 host
/26 = 255.255.255.192  → 2 bit subnet, 6 bit host → 4 reti, 62 host
/27 = 255.255.255.224  → 3 bit subnet, 5 bit host → 8 reti, 30 host
/28 = 255.255.255.240  → 4 bit subnet, 4 bit host → 16 reti, 14 host
/29 = 255.255.255.248  → 5 bit subnet, 3 bit host → 32 reti, 6 host
/30 = 255.255.255.252  → 6 bit subnet, 2 bit host → 64 reti, 2 host
```

### Salti comuni:
```
Mask .0   → Salto 256
Mask .128 → Salto 128
Mask .192 → Salto 64
Mask .224 → Salto 32
Mask .240 → Salto 16
Mask .248 → Salto 8
Mask .252 → Salto 4
```

---

**Buono studio! 📚💪**