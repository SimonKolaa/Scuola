Come funziona il mio sistema di contatti
Ho sviluppato un sistema completo per gestire i messaggi del mio Portfolio. Ecco i passaggi che avvengono quando qualcuno invia un messaggio:

Visita il Sito: Vai sul mio portfolio ufficiale all'indirizzo simonkolaaa.github.io.

Sezione Contatti: Naviga fino alla sezione "Get in Touch" (Contatti) in fondo alla pagina.

Invia un Messaggio: Compila il form con il tuo nome, la tua email e il tuo messaggio. Appena cliccherai su "Invia", il frontend (React) spedirà una richiesta asincrona al mio server privato.

Elaborazione Backend: Il mio backend personalizzato, scritto in Python e Flask e ospitato su PythonAnywhere, riceve la richiesta. Grazie a un sistema di sicurezza apposito (CORS), il server accetta solo i messaggi provenienti dal mio sito ufficiale.

Salvataggio su Database: Il messaggio viene registrato istantaneamente all'interno di un database SQLite (portfolio.sqlite). Questo garantisce che nessun messaggio vada perso, anche se il server dovesse riavviarsi.

Dashboard di Controllo: si possono visualizzare tutti i messaggi ricevuti in tempo reale visitando la nuova Dashboard all'indirizzo:
simonkolaaa.pythonanywhere.com/api/contacts

Caratteristiche Tecniche
Il sistema è stato progettato per essere estremamente resiliente: se un componente dovesse avere problemi, il form è isolato e continuerà a funzionare senza sosta