reg_voti = {}
reg_voti["carletto"] = 6
reg_voti["alberti"] = 8
reg_voti["matteo massa"] = 3
reg_voti["giuseppe"] = 7
reg_voti["franco"] = 4

for i in reg_voti.items():
    print(i)
reg_voti.update["mancio"] = 10
for i in reg_voti.items():
    print(i)


 
check = int(input("verifica studente"))

if check in reg_voti:
    print(reg_voti[check])
