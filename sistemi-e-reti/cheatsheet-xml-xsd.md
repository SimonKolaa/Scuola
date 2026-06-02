# 📋 CHEATSHEET XML/XSD - VERIFICA CARTA E PENNA

## ⚡ STRUTTURE BASE

### XML minimo
```xml
<?xml version="1.0"?>
<root>
  <elemento>valore</elemento>
</root>
```

### XSD minimo
```xml
<?xml version="1.0"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <xs:element name="root" type="xs:string"/>
</xs:schema>
```

---

## 🎯 TIPI DI DATI COMUNI

| Tipo | Uso | Esempio |
|------|-----|---------|
| `xs:string` | Testo | "Mario" |
| `xs:integer` | Intero | 42 |
| `xs:decimal` | Decimale | 3.14 |
| `xs:date` | Data | 2024-01-15 |
| `xs:time` | Ora | 14:30:00 |

---

## 📦 ELEMENTO SEMPLICE

**XML:**
```xml
<nome>Mario</nome>
```

**XSD:**
```xml
<xs:element name="nome" type="xs:string"/>
```

---

## 📦 ELEMENTO COMPLESSO

**XML:**
```xml
<persona>
  <nome>Mario</nome>
  <cognome>Rossi</cognome>
</persona>
```

**XSD:**
```xml
<xs:element name="persona">
  <xs:complexType>
    <xs:sequence>
      <xs:element name="nome" type="xs:string"/>
      <xs:element name="cognome" type="xs:string"/>
    </xs:sequence>
  </xs:complexType>
</xs:element>
```

**TRUCCO:** Elementi dentro → `complexType` + `sequence`

---

## 🏷️ ATTRIBUTI

**XML:**
```xml
<libro genere="fantasy">
  <titolo>Harry Potter</titolo>
</libro>
```

**XSD:**
```xml
<xs:element name="libro">
  <xs:complexType>
    <xs:sequence>
      <xs:element name="titolo" type="xs:string"/>
    </xs:sequence>
    <xs:attribute name="genere" type="xs:string"/>
  </xs:complexType>
</xs:element>
```

**TRUCCO:** Attributo SEMPRE DOPO la sequence!

---

## 🔢 RESTRIZIONI NUMERICHE

**Età tra 0 e 120:**
```xml
<xs:element name="eta">
  <xs:simpleType>
    <xs:restriction base="xs:integer">
      <xs:minInclusive value="0"/>
      <xs:maxInclusive value="120"/>
    </xs:restriction>
  </xs:simpleType>
</xs:element>
```

- `minInclusive/maxInclusive` → include (≥ ≤)
- `minExclusive/maxExclusive` → esclude (> <)

---

## 📏 RESTRIZIONI STRINGHE

**Lunghezza esatta (CAP = 5 cifre):**
```xml
<xs:element name="CAP">
  <xs:simpleType>
    <xs:restriction base="xs:string">
      <xs:length value="5"/>
    </xs:restriction>
  </xs:simpleType>
</xs:element>
```

**Lunghezza min/max:**
```xml
<xs:minLength value="8"/>
<xs:maxLength value="20"/>
```

---

## 🎨 ENUMERAZIONI

**XSD:**
```xml
<xs:element name="colore">
  <xs:simpleType>
    <xs:restriction base="xs:string">
      <xs:enumeration value="rosso"/>
      <xs:enumeration value="verde"/>
      <xs:enumeration value="blu"/>
    </xs:restriction>
  </xs:simpleType>
</xs:element>
```

**XML valido:** `<colore>rosso</colore>` (solo valori elencati!)

---

## 🔄 ELEMENTI RIPETUTI

**XML:**
```xml
<libri>
  <libro>Libro 1</libro>
  <libro>Libro 2</libro>
</libri>
```

**XSD:**
```xml
<xs:element name="libri">
  <xs:complexType>
    <xs:sequence>
      <xs:element name="libro" type="xs:string" 
                  minOccurs="0" maxOccurs="unbounded"/>
    </xs:sequence>
  </xs:complexType>
</xs:element>
```

- `minOccurs="0"` → opzionale
- `maxOccurs="unbounded"` → illimitato
- Default = 1 (se omessi)

---

## ⚠️ ERRORI COMUNI

### ❌ XML
```xml
<!-- SBAGLIATO -->
<Persona></persona>  <!-- case sensitive! -->
<tag attributo=valore>  <!-- mancano apici! -->
<tag><altro>  <!-- tag non chiuso! -->
```

### ✅ XML
```xml
<!-- GIUSTO -->
<persona></persona>
<tag attributo="valore">
<tag><altro></altro></tag>
```

### ❌ XSD
```xml
<!-- SBAGLIATO - attributo PRIMA! -->
<xs:complexType>
  <xs:attribute name="id"/>
  <xs:sequence>...</xs:sequence>
</xs:complexType>
```

### ✅ XSD
```xml
<!-- GIUSTO - attributo DOPO! -->
<xs:complexType>
  <xs:sequence>...</xs:sequence>
  <xs:attribute name="id" type="xs:string"/>
</xs:complexType>
```

---

## 🎓 STRATEGIA VERIFICA

### XML → XSD:
1. Scrivi intestazione XSD
2. Elemento radice → se ha figli = `complexType`
3. Apri `sequence`
4. Elenca elementi con tipi appropriati
5. Chiudi `sequence`
6. Attributi DOPO sequence
7. Chiudi tutto

### XSD → XML:
1. Scrivi intestazione XML
2. Crea elemento radice
3. Segui `sequence` nell'ordine
4. Rispetta restrizioni (min/max, enum)
5. Aggiungi attributi se presenti
6. Chiudi tutto

---

## 💡 TIPS CARTA E PENNA

- ✅ Indentazione: 2 spazi, basta leggibile
- ✅ Se sbagli: ~~cancella~~ e riscrivi
- ✅ Lascia 5-10 min finali per rileggere
- ✅ Non perdere tempo su dettagli minori

**CHECKLIST FINALE:**
- [ ] Ogni tag aperto è chiuso?
- [ ] Attributi tra apici?
- [ ] Sequence prima degli attributi?
- [ ] Case sensitive rispettato?
- [ ] Tipi corretti (xs:string, xs:integer...)?

---

## 🚀 ESEMPIO COMPLETO

### XML:
```xml
<?xml version="1.0"?>
<rubrica>
  <persona sesso="M">
    <nome>Mario</nome>
    <cognome>Rossi</cognome>
    <telefono>0288888888</telefono>
    <email>mario@rossi.it</email>
  </persona>
</rubrica>
```

### XSD:
```xml
<?xml version="1.0"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <xs:element name="rubrica">
    <xs:complexType>
      <xs:sequence>
        <xs:element name="persona" minOccurs="0" maxOccurs="unbounded">
          <xs:complexType>
            <xs:sequence>
              <xs:element name="nome" type="xs:string"/>
              <xs:element name="cognome" type="xs:string"/>
              <xs:element name="telefono" type="xs:string"/>
              <xs:element name="email" type="xs:string"/>
            </xs:sequence>
            <xs:attribute name="sesso" type="xs:string"/>
          </xs:complexType>
        </xs:element>
      </xs:sequence>
    </xs:complexType>
  </xs:element>
</xs:schema>
```

---

## 📚 POSSIBILI CONSEGNE

### TIPO 1: XML → XSD (Base)
> Dato il seguente documento XML che rappresenta un messaggio, scrivere lo schema XSD.

```xml
<?xml version="1.0"?>
<messaggio>
  <mittente>Mario</mittente>
  <destinatario>Maria</destinatario>
  <testo>Ciao!</testo>
</messaggio>
```

---

### TIPO 2: XML → XSD (Con attributi)
> Scrivere lo schema XSD per il seguente libro con attributo genere.

```xml
<?xml version="1.0"?>
<libro genere="fantasy">
  <autore>Tolkien</autore>
  <titolo>Il Signore degli Anelli</titolo>
  <anno>1954</anno>
</libro>
```

---

### TIPO 3: XML → XSD (Elementi ripetuti)
> Creare lo schema XSD. Permettere da 0 a infiniti libri.

```xml
<?xml version="1.0"?>
<biblioteca>
  <libro>
    <titolo>Libro 1</titolo>
    <autore>Autore 1</autore>
  </libro>
  <libro>
    <titolo>Libro 2</titolo>
    <autore>Autore 2</autore>
  </libro>
</biblioteca>
```

---

### TIPO 4: XSD → XML (Base)
> Scrivere un documento XML valido.

```xml
<?xml version="1.0"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <xs:element name="studente">
    <xs:complexType>
      <xs:sequence>
        <xs:element name="nome" type="xs:string"/>
        <xs:element name="matricola" type="xs:string"/>
      </xs:sequence>
    </xs:complexType>
  </xs:element>
</xs:schema>
```

---

### TIPO 5: XSD → XML (Con restrizioni)
> Scrivere XML valido rispettando le restrizioni.

```xml
<xs:element name="prodotto">
  <xs:complexType>
    <xs:sequence>
      <xs:element name="quantita">
        <xs:simpleType>
          <xs:restriction base="xs:integer">
            <xs:minInclusive value="1"/>
            <xs:maxInclusive value="100"/>
          </xs:restriction>
        </xs:simpleType>
      </xs:element>
      <xs:element name="prezzo">
        <xs:simpleType>
          <xs:restriction base="xs:decimal">
            <xs:minExclusive value="0"/>
          </xs:restriction>
        </xs:simpleType>
      </xs:element>
    </xs:sequence>
  </xs:complexType>
</xs:element>
```

---

### TIPO 6: XML → XSD (Con restrizioni da inferire)
> Scrivere XSD con restrizioni:
> - quantità: intero tra 5 e 100 (inclusi)
> - prezzo: decimale > 0 (escluso) e ≤ 999

```xml
<?xml version="1.0"?>
<prodotto>
  <quantita>10</quantita>
  <prezzo>25.99</prezzo>
</prodotto>
```

---

### TIPO 7: XSD → XML (Enumerazioni)
> Creare XML valido. `mezzo` può essere solo: auto, treno, aereo.

```xml
<xs:element name="viaggio">
  <xs:complexType>
    <xs:sequence>
      <xs:element name="mezzo">
        <xs:simpleType>
          <xs:restriction base="xs:string">
            <xs:enumeration value="auto"/>
            <xs:enumeration value="treno"/>
            <xs:enumeration value="aereo"/>
          </xs:restriction>
        </xs:simpleType>
      </xs:element>
      <xs:element name="partenza" type="xs:string"/>
    </xs:sequence>
  </xs:complexType>
</xs:element>
```

---

### TIPO 8: XML → XSD (Nidificazione)
> Definire XSD per questa rubrica con indirizzo nidificato.

```xml
<?xml version="1.0"?>
<rubrica>
  <persona>
    <nome>Mario</nome>
    <indirizzo>
      <via>Via Roma</via>
      <numero>1</numero>
      <CAP>57100</CAP>
    </indirizzo>
  </persona>
</rubrica>
```

---

### TIPO 9: Validazione
> Indicare se questo XML è valido rispetto allo schema. Se no, perché?

**Schema:**
```xml
<xs:element name="CAP">
  <xs:simpleType>
    <xs:restriction base="xs:string">
      <xs:length value="5"/>
    </xs:restriction>
  </xs:simpleType>
</xs:element>
```

**XML A:** `<CAP>57100</CAP>` → ✅ VALIDO

**XML B:** `<CAP>5710</CAP>` → ❌ NON VALIDO (4 cifre invece di 5)

---

## 🎯 TRUCCHI RAPIDI

### Vedi nell'XML → Scrivi nell'XSD:
- `<el>testo</el>` → `type="xs:string"`
- `<el><figlio>...</figlio></el>` → `complexType` + `sequence`
- `<el attr="val">` → `<xs:attribute.../>`
- Più elementi uguali → `minOccurs/maxOccurs`

### Vedi nell'XSD → Scrivi nell'XML:
- `type="xs:integer"` → numero intero
- `minOccurs="0"` → opzionale
- `maxOccurs="unbounded"` → ripetibile
- `enumeration` → usa SOLO quei valori

---

## 🏆 IN BOCCA AL LUPO!

✅ Leggi bene la consegna  
✅ Fai schema mentale prima  
✅ Rileggi tutto alla fine  
✅ Non farti prendere dal panico  

**CE LA FAI! 💪🚀**
