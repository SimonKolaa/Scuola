
fotocopie = int(input("Numero fotocopie: "))
nome_c = str(input("Nome Cliente: "))
plico = str(input("Vuoi rilegare il plico: S/N or s/n: "))


if fotocopie> 0 and fotocopie < 20:
    somma = 0.10*fotocopie  
elif fotocopie > 19 and fotocopie < 101:
    somma = 0.08*fotocopie
elif fotocopie > 100 :
    somma = 0.05*fotocopie   
else:
    somma=0

if plico == "n" or pli=="N":    
    print(f"Gentile Sig. {nome_c}, il suo preventivo è di {somma:.2f}")
elif plico=="s" or  plico=="S":
    somma=somma+1.80
    print(f"Gentile Sig. {nome_c}, il suo preventivo è di {somma:.2f} euro compresa la rilegatura.")
else:
    print("Vivo per lei")