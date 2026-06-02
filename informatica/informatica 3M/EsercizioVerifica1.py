voto1=int(input("Inserisci Primo Voto:"))
voto2=int(input("Inserisci Secondo Voto:"))
voto3=int(input("Inserisci Terzo Voto:"))
voto4=int(input("Inserisci QuartoVoto:"))
voto5=int(input("Inserisci Quinto Voto:"))

voti_sufficienti=0
voti_validi=0

if voto1 > 0 and voto1 < 11:voti_validi = voti_validi + 1

if voto1 > 5:voti_sufficienti = voti_sufficienti + 1
   
if voto2 > 0 and voto2 < 11: voti_validi = voti_validi + 1 

voto2 > 5: voti_sufficienti = voti_sufficienti + 1

if voto3 > 0 and voto3 < 11: voti_validi = voti_validi + 1
   
if voto3 > 5: voti_sufficienti = voti_sufficienti + 1
           
if voto4 > 0 and voto4 < 11:voti_validi = voti_validi + 1
      
if voto4 > 5: voti_sufficienti = voti_sufficienti + 1
            
if voto5 > 0 and voto5 < 11: voti_validi = voti_validi + 1
   
if voto5 > 5: voti_sufficienti = voti_sufficienti + 1
print("Voti sufficienti:",voti_sufficienti)
print("Voti Validi:",voti_validi)