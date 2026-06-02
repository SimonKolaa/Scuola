#Esercizio: database studenti
#Crea un database SQLite chiamato "scuola.db".
#Crea due tabelle:
#Studenti: Matricola (INTEGER PRIMARY KEY), Nome (TEXT NOT NULL), Cognome (TEXT NOT NULL).
#Esami: Id (INTEGER PRIMARY KEY AUTOINCREMENT), Matricola (INTEGER NOT NULL), Corso (TEXT NOT NULL), Voto (INTEGER), con FOREIGN KEY su Studenti(Matricola).
#Inserisci i seguenti dati (tutti gli studenti devono avere gli stessi record di esami):
#Studenti:
#Matricola 101, Nome Mario, Cognome Rossi
#Matricola 102, Nome Lucia, Cognome Bianchi
#Esami (da inserire per ogni studente: per Matricola 101 e per Matricola 102):
#Corso "Matematica", Voto 28
#Corso "Informatica", Voto 30
#Corso "Fisica", Voto 27
#Esegui tre query semplici:
#Elenco di tutti gli studenti (Matricola, Nome, Cognome).
#Elenco dei corsi e voti sostenuti da uno studente specifico (usa la matricola 101 come esempio).
#Numero di esami sostenuti per ciascuno studente (GROUP BY Matricola).
#Suggerimento: usa INSERT OR IGNORE per evitare errori su violazioni di vincoli (es. PRIMARY KEY)

import sqlite3

conn = sqlite3.connect('scuola.db')
cursor = conn.cursor()

try:
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Studenti (
        Matricola INTEGER PRIMARY KEY,
        Nome TEXT NOT NULL,
        Cognome TEXT NOT NULL
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Esami (
        Id INTEGER PRIMARY KEY AUTOINCREMENT,
        Matricola INTEGER NOT NULL,
        Corso TEXT NOT NULL,
        Voto INTEGER,
    FOREIGN KEY (Matricola) REFERENCES Studenti(Matricola)
    )
    """)

    cursor.execute(
        "INSERT INTO Studenti (Matricola, Nome, Cognome) VALUES (?, ?, ?)",
        (101, 'Dario', 'Casali')
    )
    cursor.execute(
        "INSERT INTO Studenti (Matricola, Nome, Cognome) VALUES (?, ?, ?)",
        (102, 'Lucia', 'Bianchi')
    )
    cursor.execute (
        "INSERT INTO Esami (id, Matricola, Corso, Voto) VALUES (?, ?, ?, ?)",
        (1, 101, 'Matematica', 28),
        (2, 102, 'Matematica', 28) #per entrambi gli studenti
    )
    cursor.execute (
        "INSERT INTO Esami (id, Matricola, Corso, Voto) VALUES (?, ?, ?)",
        (1, 101, 'Informatica', 30),
        (2, 102, 'Informatica', 30)
    )
    cursor.execute (
        "INSERT INTO Esami (id, Matricola, Corso, Voto) VALUES (?, ?, ?)",
        (1, 101, 'Fisica', 27),
        (2, 102, 'Fisica', 27)
    )

    studenti = cursor.execute("SELECT * FROM Studenti").fetchall()

    cursor.execute("SELECT Corso, Voto FROM Esami WHERE Matricola = ?", (101,))

    cursor.execute ("SELECT Matricola, COUNT(*) as NumeroEsami FROM Esami GROUP BY Matricola")

finally:
    conn.commit()
    conn.close()