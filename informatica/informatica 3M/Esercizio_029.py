def calcola_importo(fatture: list[dict]) -> list[float] | None:
    if not fatture:
        return None
    totale = 0
    totale_scontato = 0
    for fattura in fatture:
     importo = fattura["importo"]
    sconto = fattura["sconto_fattura"] / 100
    importo_scontato = importo * (1 - sconto)
    fattura["importo_scontato"] = importo_scontato
    totale += importo
    totale_scontato += importo_scontato
    return [totale,totale_scontato]


fatture = [
{"id": "Monticelli", "importo": 245.78, "sconto_fattura": 10},
{"id": "Kola", "importo": 325.71, "sconto_fattura": 12},
{"id": "Romagna_la_squale", "importo": 245.78, "sconto_fattura": 8},
{"id": "Bilancioni2drugrich", "importo": 245.78, "sconto_fattura": 15},
{"id": "Sanchi_la_rue", "importo": 245.78, "sconto_fattura": 5},
{"id": "Pontellini", "importo": 245.78, "sconto_fattura": 18},
{"id": "Clementino_la_street", "importo": 245.78, "sconto_fattura": 20},
{"id": "Arlotti", "importo": 245.78, "sconto_fattura": 19},
{"id": "Nedria_Mychajlo_Mudryk", "importo": 245.78, "sconto_fattura": 7},
{"id": "Santini", "importo": 245.78, "sconto_fattura": 22},
]

risultati = calcola_importo(fatture)
print("Totale importi:", risultati[0])
print("Totale importi scontati:", risultati[1])



print("mancio ha soldi sporchi dentro zainetti LV")