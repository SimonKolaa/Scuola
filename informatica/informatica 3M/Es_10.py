voto1 = int(input("Inserisci voto esame: "))
voto2 = int(input("Inserisci voto esame: "))
voto3 = int(input("Inserisci voto esame: "))
crediti1 = int(input("Inserisci crediti: "))
crediti2 = int(input("Inserisci crediti: "))
crediti3 = int(input("Inserisci crediti: "))
voto=voto1+voto2+voto3
crediti =crediti1+crediti2+crediti3



if voto > 0 & voto < 91:
print("Voto: ",voto)
if crediti > 0 & crediti < 37:
print("Crediti: ",crediti)
media= ((voto/3)*(crediti/3))/(crediti)
print(media)