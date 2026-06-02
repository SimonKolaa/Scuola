## Lesson Learned (Lezioni Apprese)

Al termine della fase di pianificazione e delle prime simulazioni di sviluppo del progetto **Portfolio Personale simonkolaaa.github.io**, è stato effettuato un debriefing per analizzare criticamente il processo. Di seguito le principali riflessioni:

### Errori di pianificazione
* **Assenza di un ambiente di Staging:** Si è pianificato di testare il codice direttamente in produzione (su GitHub Pages). Questo puo essere un errore organizzativo: ogni modifica va live immediatamente, rischiando di mostrare un sito "rotto" agli utenti (es. recruiter) durante i deploy intermedi.
* **Mancanza di un processo di "Change Control":** Durante le simulazioni (Focus Group e Interviste), sono state accolte troppe idee nuove (es. chatbot, form di contatto, supporto bilingue) senza bloccare o filtrare formalmente le richieste. Questo puo scatenare il fenomeno dello *scope creep* (allargamento incontrollato dei requisiti).

### Stime sottovalutate
* **Sviluppo UI e Cross-browser Testing:** L'implementazione della griglia CSS e delle animazioni è stata stimata in modo troppo ottimistico. Non si è tenuto conto del tempo fisiologico necessario per testare e correggere i bug visivi su browser differenti (in particolare Safari su iOS).
* **Creazione dei Contenuti (Copywriting):** Si è erroneamente pensato che la scrittura della bio, del CV e degli articoli del blog fosse rapida. In realtà, produrre testi professionali, bilingue e orientati all'utente ha richiesto molto più tempo del codice stesso.

###  Rischi non considerati inizialmente
* **Rate-Limiting delle API:** Non è stato calcolato che le chiamate pubbliche e non autenticate alle API di GitHub avrebbero potuto superare il limite orario (60 richieste/ora), causando il blocco del caricamento dei repository sulla pagina o delle chiamate ad Arus.
* **Blocchi lato Client:** L'utilizzo diffuso di estensioni AdBlocker o impostazioni di privacy severe da parte degli utenti finali rischia di bloccare script di terze parti essenziali (come il modulo di contatti serverless).

### Cosa migliorerei in un progetto futuro
1. **Introdurre Buffer di Contingenza:** Aggiungere sistematicamente un 15-20% di tempo extra "cuscinetto" sulle stime di sviluppo tecnico per assorbire bug imprevisti o problemi di compatibilità.
2. **Congelamento dei Requisiti (Requirements Freeze):** Creare un Documento dei Requisiti o un Project Charter e bloccarlo prima di scrivere codice. Ogni nuova feature desiderata va inserita in un backlog per versioni future (v2.0), senza impattare la prima release.
3. **Proof of Concept (PoC) Obbligatorio:** Prima di adottare librerie esterne o basare il sito su API di terze parti, dedicare 1-2 giorni a creare un prototipo isolato per testare i limiti tecnici (come il rate-limiting).
4. **Deploy su Ambienti Separati:** Implementare una pipeline CI/CD che preveda un ambiente di test separato dalla produzione (es. deploy automatico delle Pull Request su Vercel o su un branch di *preview*), per testare il sito senza compromettere l'URL pubblico.