CREATE TABLE Prodotto (
    Id INTEGER PRIMARY KEY,
    Nome TEXT NOT NULL,
    Prezzo FLOAT NOT NULL
);

CREATE TABLE Ordine (
    Id INTEGER PRIMARY KEY,
    cliente_nome INTEGER NOT NULL,
     data DATE NOT NULL,
);

CREATE TABLE OrdineProdotto (
    Id INTEGER PRIMARY KEY,
    ordine_id INT
    prodotto_id INT
    FOREIGN KEY (Id) REFERENCES Prodotto(Id)
    FOREIGN KEY (Id) REFERENCES Ordine(Id)
quantità FLOAT NOT NULL --FLOAT NON INT

);

INSERT INTO Prodotto(id, nome, prezzo) VALUES
(1, 'Notebook', 12.5)
(2, 'Penna a sfera', 1.2)
(3, 'Zaino', 28.0)
(4, 'Agenda', 7.5)
(5, 'Quaderno', 5.0)

INSERT INTO Ordine (id, data, cliente_nome) VALUES
(1, '2025-10-01', 'Anna Verdi')
(2, '2025-10-02', 'Marco Neri')
(3, '2025-10-03', 'Anna Verdi')

INSERT INTO OrdineProdotto (id, ordine_id, prodotto_id, quantità) VALUES
(1, 1, 1, 2)
(2, 1, 2, 5)
(3, 2, 3, 1)
(4, 3, 4, 2)
(5, 3, 2, 3)

--Elenco dei prodotti che costano meno di 10.
SELECT nome, prezzo
FROM Prodotto
WHERE prezzo < 10

--Elenco dei prodotti ordinati in un determinato ordine (id ordine come esempio)
SELECT P.nome, P.prezzo, O.quantità
FROM OrdineProdotto O
JOIN Prodotto P ON O.prodotto_id = P.id
WHERE O.ordine_id = 1

--Numero di ordini per ogni cliente
SELECT cliente_nome, COUNT(*) AS numero_ordine
FROM Ordine
GROUP BY cliente_nome;

--Media dei prezzi dei prodotti.
SELECT AVG(prezzo) AS media_prezzi
FROM Prodotto;

--Quantità totale venduta per ogni prodotto
SELECT P.nome, SUM(O.quantità) AS quantita_totale
FROM Prodotto P
JOIN OrdineProdotto O ON P.id = O.prodotto_id
GROUP BY P.nome;

-- Prodotti con quantità totale venduta maggiore di 5.
SELECT P.nome, SUM(O.quantità) AS quantita_totale
FROM Prodotto P
JOIN OrdineProdotto O ON P.id = O.prodotto_id
GROUP BY P.nome
HAVING SUM(O.quantità) > 5;

--Elenco di tutti i prodotti con la quantità totale venduta (NULL per quelli mai venduti).
SELECT P.nome, SUM(O.quantità) AS quantita_totale
FROM Prodotto P
LEFT JOIN OrdineProdotto O ON P.id = O.prodotto_id
GROUP BY P.nome;

--Totale speso per ogni cliente.
SELECT cliente_nome, COUNT(*) AS numero_ordine
FROM Ordine
GROUP BY cliente_nome;