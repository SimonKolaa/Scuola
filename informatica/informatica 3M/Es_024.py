#Simon Kola
#Esercizio 24
dipendente1 = {
    "Nome" : "Carlo",
    "Lavoro" : "capo",
    "Stipendio" : 3000
}
dipendente2 = {
    "Nome" : "Giuseppina",
    "Lavoro" : "Attrice",
    "Stipendio" : 1200
}
dipendente3 = {
    "Nome" : "Saverio",
    "Lavoro" : "Player",
    "Stipendio" : 1000
}
dipendente4 = {
    "Nome" : "Massa",
    "Lavoro" : "Spacciatore",
    "Stipendio" : 6000
}

a = dipendente1["Nome"]
b = dipendente2["Nome"]
c = dipendente3["Nome"]
d = dipendente4["Nome"]
print("",a,"\n",b,"\n",c,"\n",d)

progetto = {
    "Budget iniziale" : 100,
    "Costo orario" : 5
}
azienda = [dipendente1,dipendente2,dipendente3,dipendente4,progetto]

ore_disponibili = progetto["Budget iniziale"] / progetto["Costo orario"]

nome_dip1 = dipendente1["Nome"]
totale_ore1 = int(input(f"Inserire la quantità di ore lavorative di {nome_dip1}:"))
nome_dip2 = dipendente2["Nome"]
totale_ore2 = int(input(f"Inserire la quantità di ore lavorative di {nome_dip2}:"))
nome_dip3 = dipendente3["Nome"]
totale_ore3 = int(input(f"Inserire la quantità di ore lavorative di {nome_dip3}:"))
nome_dip4 = dipendente4["Nome"]
totale_ore4 = int(input(f"Inserire la quantità di ore lavorative di {nome_dip4}:"))

budget_rim = progetto["Budget iniziale"] - (totale_ore1 + totale_ore2 + totale_ore3 + totale_ore4)* progetto["Costo orario"]

progetto["Budget rimanente"] = budget_rim

dipendente1["Stipendio"] = dipendente1["Stipendio"] + totale_ore1 * progetto["Costo orario"]
dipendente2["Stipendio"] = dipendente2["Stipendio"] + totale_ore2 * progetto["Costo orario"]
dipendente3["Stipendio"] = dipendente3["Stipendio"] + totale_ore3 * progetto["Costo orario"]
dipendente4["Stipendio"] = dipendente4["Stipendio"] + totale_ore4 * progetto["Costo orario"]


