pas = int(input("Numero Pasticcini:"))

if pas >= 5:
 scg = int(pas/5) 
 pas= pas % 5 
 print("Scatola Grande:",scg)
 
if pas >= 3:
 scm = int (pas/3)
 pas = pas % 3
 print("Scatola Media:",scm)
 
if pas >= 1:
 scp= pas
 print("Scatola Piccola:",scp)