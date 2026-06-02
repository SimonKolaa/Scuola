voti = 0
somma_voti = 0
voto = float(input("inserire voto: "))
while voto > 0:
    if (voto <= 10):
        voti += 1
        somma_voti += voto
    voto = float(input("inserire voto: "))      
media = somma_voti / voti
print("la tua media è di",media)
