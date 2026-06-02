# Anthropic vs Pentagono - cosa sta succedendo

*marzo 2026 - Simon Kola*

---

## cos'è successo in breve

il pentagono (dipartimento della difesa USA) ha etichettato anthropic come "supply chain risk", che è una roba che di solito si usa per aziende di paesi nemici tipo cina o russia, non per un'azienda americana. questa cosa blocca tutti i contractor del ministero della difesa dall'usare i prodotti di anthropic (tipo claude).

trump ha anche postato su truth social dicendo a tutte le agenzie federali di smettere immediatamente di usare anthropic. letteralmente ha scritto qualcosa tipo "WE will decide the fate of our Country — NOT some out-of-control, Radical Left AI company"

anthropic ha risposto portandoli in tribunale il 9 marzo 2026, con due cause separate: una in california e una a washington

fonti:
- [TechCrunch - articolo principale sulla causa](https://techcrunch.com/2026/03/09/anthropic-sues-defense-department-over-supply-chain-risk-designation/)
- [CNN Business](https://www.cnn.com/2026/03/09/tech/anthropic-sues-pentagon)
- [NPR](https://www.npr.org/2026/03/09/nx-s1-5742548/anthropic-pentagon-lawsuit-amodai-hegseth)
- [discussione su r/technology](https://www.reddit.com/r/technology/comments/1j7k2xp/anthropic_sues_the_trump_administration_after_it/)
- [discussione su r/MachineLearning](https://www.reddit.com/r/MachineLearning/comments/1j7nmqp/anthropic_sues_pentagon_over_supply_chain_risk/)

---

## il contesto 

worldy ha fatto una puntata del podcast newsy su questa storia e secondo me è il miglior punto di partenza per capire il quadro generale.

la premessa che fanno è importante: **non è una storia di buoni e cattivi**, sembra che lo sia — anthropic che difende i diritti umani mentre openai che firma col pentagono — ma la realtà è più complicata. anthropic non ha nessuna aureola e vive di soldi. la cosa che conta davvero è capire cosa significa che lo stesso chatbot che usi per scrivere una mail o prepararti una ricetta può essere usato per individuare bersagli militari o sorvegliare i cittadini.

il contesto di partenza: già nel 2025, con trump presidente, aziende come google avevano rimosso dalle loro licenze d'uso, il divieto di impiegare le proprie AI per armi autonome e sorveglianza di massa. anthropic era stata la prima società ad avere contratti da centinaia di milioni col pentagono, ed era quella più coinvolta perché aveva integrato i suoi sistemi con palantir — un'azienda di analisi dati molto controversa che gestisce anche documenti classificati per la sicurezza nazionale.

**come funziona concretamente l'AI in ambito militare** (spiegato nel podcast): i modelli esaminano enormi quantità di informazioni in pochissimo tempo — immagini di droni, intercettazioni telefoniche, rapporti di intelligence — e all'interno identificano possibili obiettivi, classificano minacce, suggeriscono quale arma usare o dove bombardare. il rischio vero non è solo che la macchina decida da sola, ma che i comandanti umani si affidino troppo alla macchina e perdano quel senso di responsabilità diretta sulle conseguenze. ci sono già state simulazioni su GPT, Gemini e Claude inseriti in scenari di guerra: i risultati mostrano che i modelli ricorrono alle armi nucleari molto più facilmente di quanto farebbe un essere umano.

fonte: [worldy - podcast newsy su anthropic e pentagono](https://worldy.com/newsy)

---

## perché è iniziato tutto

il punto centrale è che il pentagono voleva usare claude "per qualsiasi scopo legale", senza limitazioni. anthropic aveva due "red lines" che non voleva togliere:

1. claude non deve essere usato per la sorveglianza di massa dei cittadini americani
2. claude non è pronto per essere usato in armi autonome (cioè senza un umano che decide di sparare) — la dicitura esatta era "adeguata supervisione umana"

hegseth (il segretario alla difesa, quello di fox news) disse che il pentagono doveva avere accesso "senza essere limitato da un contractor privato". anthropic ha detto no. e lì è partita la guerra.

da notare una cosa assurda: il pentagono stava usando claude per le operazioni militari in iran anche mentre litigava con anthropic per togliergli il contratto. praticamente lo usavano e contemporaneamente lo mettevano in blacklist.

c'è anche un retroscena politico: secondo un memo interno di amodei riportato da The Information, il governo ce l'ha con anthropic perché non ha fatto "donazioni o lodi da dittatore a trump". il sottosegretario emil michael su X aveva già definito amodei "un bugiardo con il complesso di dio". il pentagono aveva anche dato un ultimatum con orario preciso — le 17:01 del 27 febbraio — del tipo obbedisci o perdi tutto. amodei non si è piegato.

fonti: [Fortune](https://fortune.com/2026/03/09/anthropic-sues-pentagon-ai-supply-chain-risk-trump-adminstration/) | [CNBC - claude usato in iran](https://www.cnbc.com/2026/03/05/anthropic-pentagon-ai-claude-iran.html) | [ANSA](https://www.ansa.it/osservatorio_intelligenza_artificiale/notizie/approfondimenti/2026/02/28/ai-militare-il-pentagono-caccia-anthropic-e-sceglie-openai_ff9aea27-d545-45b7-9cf3-9b6ce6436253.html)

---

## cosa c'entra openai

questa è la parte un po' brutta. praticamente lo stesso giorno in cui sono saltate le trattative tra anthropic e pentagono, openai ha firmato un accordo con il ministero della difesa — apparentemente accettando condizioni simili a quelle che anthropic aveva rifiutato.

openai poi ha detto che il loro contratto avrebbe comunque garantito le stesse protezioni. ma worldy fa notare una cosa importante nel podcast: **le clausole di openai e quelle di anthropic sembrano uguali ma legalmente non lo sono**. la differenza sta nei dettagli:

- anthropic chiedeva il divieto di uso senza "adeguata supervisione umana"
- openai ha firmato con "responsabilità umana" — termine molto vago, che militarmente può anche significare che la macchina decide in autonomia e poi a posteriori c'è un comandante umano che è formalmente responsabile

e poi c'è la questione della dicitura "tutti gli scopi legali" che rende qualsiasi limitazione debole, perché è il governo stesso a decidere cosa è legale.

in più il testo completo del contratto non è mai stato reso pubblico. The Intercept ha chiesto a openai le clausole specifiche — nessuna risposta. altman ha detto su X che ci sono le protezioni ma non ha dato prove verificabili.

openai ha poi ammesso che l'annuncio sembrava "sloppy and opportunistic". e perfino il capo della robotica di openai (caitlin kalinowski) si è dimessa, scrivendo che "sorveglianza dei cittadini senza supervisione e autonomia letale senza autorizzazione umana sono linee di confine da non superare con leggerezza."

amodei in un memo interno ha definito i dipendenti di openai "gullibili" e ha accusato il management di diffondere "bugie belle e buone".

fonti: [Fortune](https://fortune.com/2026/03/09/anthropic-sues-pentagon-ai-supply-chain-risk-trump-adminstration/) | [The Intercept - il contratto segreto di openai](https://theintercept.com/2026/03/08/openai-anthropic-military-contract-ethics-surveillance/) | [Il Post - ricostruzione completa](https://www.ilpost.it/2026/03/08/pentagono-anthropic-openai/)

---

## cosa dice anthropic nella causa

le accuse principali nella denuncia sono tre:

- **violazione del primo emendamento**: il governo starebbe punendo anthropic per le sue posizioni pubbliche sull'IA (libertà di espressione). la citazione esatta dalla causa è: *"The Constitution does not allow the government to wield its enormous power to punish a company for its protected speech"*
- **trump ha ecceduto i suoi poteri**: non avrebbe l'autorità di ordinare a tutte le agenzie federali di smettere di usare anthropic, questo lo decide il congresso
- **mancanza di due process**: anthropic non è stata trattata con le procedure legali dovute prima di essere messa in blacklist

la causa chiede ai tribunali di annullare la designazione e bloccare l'enforcement. il CFO(direttore finanziario) di anthropic ha detto che potrebbero perdere "miliardi di dollari" di fatturato nel 2026 se la cosa va avanti.

fonte: [Axios](https://www.axios.com/2026/03/09/anthropic-sues-pentagon-supply-chain-risk-label) | [CNBC](https://www.cnbc.com/2026/03/09/anthropic-trump-claude-ai-supply-chain-risk.html)

---

## chi sta con anthropic

interessante notare che non sono soli:

- **microsoft** ha depositato un "amicus brief" (documento di supporto legale) chiedendo al tribunale di bloccare temporaneamente la designazione
- **circa 40 ricercatori di openai e google deepmind** (a titolo personale) hanno firmato un documento di supporto, tra cui jeff dean, chief scientist di google
- **esperti legali** su Lawfare hanno scritto che la designazione probabilmente "eccede quello che la legge autorizza"
- **senatori democratici** come kirsten gillibrand: "un uso pericoloso e improprio di uno strumento pensato per le minacce straniere"
- **perfino critici repubblicani**: un ex consigliere AI di trump ha definito la designazione una "death rattle della repubblica"

fonti: [La Voce di New York](https://lavocedinewyork.com/news/2026/03/11/microsoft-contro-il-pentagono-scontro-su-anthropic-e-sulluso-militare-dellia/) | [NPR](https://www.npr.org/2026/03/06/g-s1-112713/pentagon-labels-ai-company-anthropic-a-supply-chain-risk) | [TechCrunch](https://techcrunch.com/2026/03/05/its-official-the-pentagon-has-labeled-anthropic-a-supply-chain-risk/)

---

## amodei vs altman — due modi diversi di fare AI

questa vicenda mette in luce una differenza enorme tra i due CEO principali del settore.

**dario amodei (anthropic)** era dipendente di openai, si è licenziato nel 2021 e ha fondato anthropic con l'obiettivo esplicito di fare AI più sicura. anthropic ha una "costituzione" scritta insieme a una filosofa con una serie di principi etici che guidano claude. non è andato all'inaugurazione di trump. non ha donato soldi alla sua campagna. ha perso un contratto da 200 milioni pur di non cedere. si è beccato insulti personali ("leftist nutjob" da trump, "bugiardo con complesso di dio" dal sottosegretario) e non ha ceduto comunque.

**sam altman (openai)** ha partecipato all'inaugurazione. il presidente di openai greg brockman ha donato 25 milioni al super PAC di trump. openai ha firmato l'accordo col pentagono poche ore dopo che anthropic era stata messa in blacklist. poi ha dovuto fare marcia indietro su alcune clausole, e il testo dell'accordo non è mai stato reso pubblico. worldy fa anche notare che altman stesso, qualche anno fa, aveva firmato una lettera per "mitigare il rischio di estinzione causato dalle AI" — e adesso è quello che ha firmato col pentagono per gli usi militari senza le stesse garanzie che chiedeva anthropic.

in poche parole: altman gioca la partita del potere, amodei cerca di non giocarla. non so chi "vinca" sul lungo periodo, ma è chiaro chi sta prendendo il rischio maggiore per i propri valori.

fonti: [CNBC](https://www.cnbc.com/2026/03/05/anthropic-pentagon-ai-claude-iran.html) | [ANSA](https://www.ansa.it/osservatorio_intelligenza_artificiale/notizie/approfondimenti/2026/02/28/ai-militare-il-pentagono-caccia-anthropic-e-sceglie-openai_ff9aea27-d545-45b7-9cf3-9b6ce6436253.html)

---

## le domande da farsi (e che secondo me sono quelle giuste)

il podcast di worldy non si limita a raccontare la vicenda, finisce ponendo delle domande che rimangono aperte e che secondo me sono il punto più interessante di tutta la storia.

**devo disinstallare chatGPT?** è la domanda che si fanno in tanti dopo questa storia, forse, ma il problema è più grande di così. le disinstallazioni di chatgpt sono aumentate del 295% dopo l'annuncio dell'accordo col pentagono — la gente ha interpretato quella firma come il superamento di una linea etica. però anthropic non è una ONG, vive di soldi, e claude è stato usato in operazioni militari in iran comunque.

**il chatbot che uso ogni giorno può diventare uno strumento di sorveglianza?** sì, tecnicamente. il governo potrebbe usare queste tecnologie per analizzare geolocalizzazioni, cronologie di navigazione, transazioni economiche — dati che noi regaliamo quotidianamente ai chatbot in modo del tutto sereno. il confine tra tecnologia civile e tecnologia di guerra è sottilissimo.

**chi controlla queste aziende quando collaborano con gli stati?** questa è la domanda finale del podcast, quella che rimane senza risposta. chi stabilisce se un uso è "legittimo"? chi verifica che le clausole vengano rispettate? come dicono loro: "chi controlla i controllori?"

**e noi cosa possiamo fare davvero?** scegliere il software è un segnale, il nostro potere decisionale su queste questioni è limitato. i governi più bellicosi del mondo delegano a delle AI decisioni su chi considerare un terrorista e chi no. la domanda non è più solo "mi ruberanno i dati?" — è una questione molto più profonda di controllo democratico sulla tecnologia.

fonte: [worldy - podcast newsy](https://worldy.com/newsy)

---

## la mia posizione

secondo me anthropic ha ragione, e non solo per motivi legali.

il punto vero è che un governo non dovrebbe poter usare contratti e appalti come leva per forzare un'azienda privata ad abbandonare i propri principi etici. se questo precedente passa, domani qualsiasi azienda tech che non si allinea alla politica del momento può essere messa in blacklist. è un meccanismo che deve essere indipendente da chi sia al governo.

poi c'è la questione tecnica: le "red lines" di anthropic non sono capricci ideologici, sono posizioni ragionevoli. armi autonome che decidono da sole di sparare senza supervisione umana sono un problema serio, non è fantascienza — ci sono già simulazioni che mostrano i modelli AI ricorrere alle bombe nucleari come se fossero petardi. e la sorveglianza di massa dei cittadini americani tramite IA è roba da stato di polizia.

dario amodei su questo è stato coerente dall'inizio. ha rinunciato a miliardi pur di non cedere. la storia di openai invece non fa una bella figura — e il fatto che il contratto non sia mai stato reso pubblico dovrebbe preoccupare chiunque.

l'unica cosa su cui concordo con worldy è che non è una storia di buoni e cattivi pura. anthropic stava usando claude in operazioni militari in iran anche durante la causa. il problema non è solo chi firma cosa, è che non esistono ancora regole internazionali sull'uso dell'AI in guerra — le convenzioni di ginevra non contemplano macchine che selezionano autonomamente i bersagli. e finché non esistono quelle regole, siamo tutti un po' in balia di queste aziende e di questi governi.

---

## sviluppi recenti (10-11 marzo 2026)

- google sta espandendo la sua presenza nel portale AI del pentagono, approfittando del vuoto lasciato da anthropic ([CNBC](https://www.cnbc.com/2026/03/10/google-deepens-pentagon-ai-push-after-anthropic-sues-trump-admin.html))
- microsoft supporta ufficialmente anthropic in tribunale
- il sottosegretario alla difesa ha detto che non vede "nessuno scenario in cui si risolva" tramite negoziati
- **effetto inaspettato**: dopo tutta la vicenda, più di un milione di persone al giorno si sono iscritte a claude, superando chatgpt in oltre 20 paesi. le disinstallazioni di chatgpt sono aumentate del 295% rispetto alla media precedente ([NPR](https://www.npr.org/2026/03/06/g-s1-112713/pentagon-labels-ai-company-anthropic-a-supply-chain-risk))
- la causa è ancora nelle primissime fasi, non ci sono ancora udienze programmate

---

*fonti principali: TechCrunch, CNN, NPR, Fortune, Axios, CNBC, Washington Post, TechRadar, Il Post, ANSA, Il Sole 24 Ore, The Intercept, La Voce di New York, reddit (r/technology, r/MachineLearning), worldy (podcast newsy)*