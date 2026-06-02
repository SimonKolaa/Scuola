# Report Ciclo di Vita del Software: Personal Portfolio
**Autore:** Simon Kola - http://simonkolaaa.github.io/

## 1. Descrizione del Progetto: Recap
Il progetto consiste nello sviluppo di un Portfolio Professionale dinamico, concepito sotto forma di Single Page Application (SPA). A differenza di un sito statico, l'applicazione integra i dati in tempo reale interrogando le API REST di GitHub (da account multipli) e offre un'esperienza utente interattiva, comprensiva di un sistema bilingue (IT/EN) gestito dinamicamente. Lo scopo è dimostrare le mie competenze come Software Engineer in fase Junior siccome frequento ancora la scuola, automatizzando al contempo l'aggiornamento dei progetti esposti e di quelli futuri.

---

## 2. Fasi del Ciclo di Vita del Software

* **Pianificazione del sistema:** La fase iniziale si è concentrata sulla scelta dello stack tecnologico (React.js, React-Bootstrap) per garantire reattività e facilità di gestione dello stato. Si è deciso di puntare su un'architettura modulare per facilitare la futura scalabilità.
* **Analisi dei requisiti:** Sono stati definiti i requisiti funzionali principali: il sistema doveva aggregare i repository da profili GitHub multipli (`simonkolaaa` e `SimonKolaa`), presentare un layout responsive e consentire lo switch della lingua senza ricaricare la pagina.
* **Progettazione:** È stata definita l'architettura dei componenti (About, Projects, Skills, Contact). Per la gestione dei dati, si è progettato un file centralizzato (`config.js`).
* **Codifica:**  Fork del main-repository, sviluppo in locale dei componenti, focalizzandosi sulla riusabilità. Implementazioni front-end per consumare le API pubbliche di GitHub.
* **Test e debug:** Verifica della corretta visualizzazione degli skeleton (prove) durante il caricamento dei dati.
* **Installazione e collaudo:** Il deploy è stato completamente automatizzato tramite **GitHub Actions**. Ogni push sul branch principale fa scattare una pipeline su Actions che compila e pubblica il progetto su GitHub Pages.
* **Manutenzione:** L'architettura scelta riduce drasticamente i costi di manutenzione: i nuovi progetti si aggiornano automaticamente tramite API, mentre i testi e le sezioni sono modificabili dal singolo file `config.js`.

---

## 3. Modello di Sviluppo

**Modello adottato:** Modello **Ibrido** (Combinazione di Waterfall, RAD, Incrementale/Agile e Build & Fix).

**Motivazione:**
Trattandosi di un progetto personale sviluppato interamente da me, ho ritenuto che limitarsi a un singolo modello teorico fosse restrittivo e non flessibile. Ho quindi adottato un approccio ibrido, applicando modelli diversi a seconda della fase e del task da affrontare:

* **Waterfall (A cascata):** Utilizzato per l'impostazione iniziale dell'architettura e per la configurazione dell'infrastruttura (in particolare la pipeline con GitHub Actions). In questi contesti "core", era fondamentale seguire una sequenza logica e rigorosa (pianificazione strutturale -> implementazione -> deploy) per evitare di dover rifare il lavoro da zero.
* **RAD / Prototipazione:** Adottato per la fase di design dell'interfaccia. Ho utilizzato React-Bootstrap per creare rapidamente un prototipo visivo (uno "scheletro" della UI) senza logica sottostante. Questo mi ha permesso di validare subito l'aspetto estetico, il layout responsivo e l'esperienza utente prima di investire tempo nello sviluppo delle funzionalità complesse.
* **Incrementale / Agile:** Utilizzato per lo sviluppo logico delle funzionalità. Il progetto è cresciuto rilasciando piccoli incrementi software: prima l'integrazione di base con le API per un solo account, poi il refactoring per il multi-account, e infine l'introduzione della Context API per il sistema bilingue. Questo approccio mi ha garantito di avere un portfolio sempre "deployabile" e pronto all'uso, aggiungendo valore un pezzo alla volta.
* **Build & Fix:** Utilizzato a livello "micro", in particolare durante il perfezionamento grafico (CSS e responsiveness sui vari device) e la gestione di comportamenti imprevisti delle API. In questi scenari specifici, l'approccio diretto "scrivi il codice, guarda il risultato a schermo, correggi l'errore" si è rivelato il più veloce.

Questa flessibilità mi ha permesso di ottimizzare i tempi di sviluppo, mantenendo il focus dove serviva (architettura) e la velocità dove era possibile (UI e bug fixing).

---

## 4. Rischi e Problemi

Di seguito i 3 rischi principali individuati e mitigati durante lo sviluppo, collegati alle relative fasi:

1.  **Rischio di blocco API (Rate Limiting) - Fase di Test/Codifica:**
    * *Problema:* Utilizzando le API pubbliche di GitHub o le API di alcune AI (Gemini), c'è un limite stretto di chiamate. Durante lo sviluppo e il testing continuo, ricaricare spesso la pagina avrebbe potuto bloccare l'IP, impedendo di testare l'interfaccia.
    * *Gestione:* Utilizzo intelligente di dati mockati durante la codifica o implementazione di chiamate ottimizzate.
2.  **Rischio di architettura complessa - Fase di Progettazione:**
    * *Problema:* Il passaggio dei dati per il sistema bilingue a tutti i componenti interni rischiava di rendere il codice illeggibile o l'implementazione di un chat-bot rischiava di noon essere fuzionante (già successo :( )).
    * *Gestione:* Anticipando il problema nella progettazione, è stata introdotta la Context API, che ha centralizzato lo stato isolando il rischio.
3.  **Rischio di integrazione (Rottura della Build) - Fase di Installazione/Collaudo:**
    * *Problema:* Effettuare modifiche dirette al codice in produzione avrebbe potuto causare down del portfolio, offrendo una cattiva immagine agli utenti.
    * *Gestione:* Implementazione di GitHub Actions. La pipeline verifica l'integrità del codice prima del deploy.

---

## 5. Valutazione Critica

* **Cosa ha funzionato bene?** L'automazione tramite GitHub Actions è stata un successo: ha annullato il tempo perso per i deploy manuali. Inoltre, l'utilizzo degli *skeleton loading* durante l'attesa delle API ha migliorato notevolmente l'UX.
* **Cosa avrebbe potuto causare problemi?**
    Una mancata progettazione iniziale del file `config.js`. Se i testi (es. bio, contatti, hard skills) fossero stati *hardcoded* (scritti fissi) dentro ogni singolo componente React, aggiungere la seconda lingua avrebbe richiesto di riscrivere mezza applicazione.
* **Quale modello userei oggi per questo progetto? Perché?**
    Confermerei l'approccio **Ibrido**, ma lo formalizzerei maggiormente utilizzando un framework come **Flask** adattato per un singolo sviluppatore. Utilizzerei una board Kanban (GitHub Projects) fin dal giorno zero per definire dei piccoli "sprint" settimanali, trasformando ogni idea in una *User Story* ben definita.

---

## 6. Gestione Lato GitHub Projects (Board)

*(In questa sezione sono allegati gli screenshot della gestione Projects del progetto)*

* **Screenshot 1: La Board generale** (Visualizzazione delle colonne Todo, In Progress, Done)
    > ![Testo alternativo]("C:\Users\Utente\Desktop\projects-1.png")

* **Screenshot 2: Esempio di Issue dettagliata** (Esempio di una task come "Implement Context API for bilingual system" con assegnazione e label)
    > ![Testo alternativo]("C:\Users\Utente\Desktop\projects-2.png")

**Nota per la presentazione:** Durante l'esposizione, si effettuerà una navigazione live della piattaforma all'indirizzo del repository: `https://github.com/simonkolaaa/simonkolaaa.github.io/projects`