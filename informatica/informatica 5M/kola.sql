-- Query 1: Elenco delle piscine in ordine alfabetico della città di Milano
SELECT nome, indirizzo, telefono, responsabile
FROM Piscina
WHERE citta = "Milano"
ORDER BY nome;

-- Query 2: Nome, cognome, qualifica e nome della piscina degli insegnanti, in ordine alfabetico
SELECT i.nome, i.cognome, q.descrizione AS qualifica,
FROM Insegnante i
JOIN Qualifica q ON i.codice_fiscale = q.insegnante_cf
ORDER BY i.cognome, i.nome, q.descrizione;

-- Query 3: Per ogni piscina, indicare il suo nome ed il numero di insegnanti che possiede
SELECT p.nome AS nome_piscina, COUNT(i.codice_fiscale) AS numero_insegnanti
FROM Piscina p
JOIN Insegnante i ON p.nome = i.piscina_nome
GROUP BY p.nome
ORDER BY p.nome;