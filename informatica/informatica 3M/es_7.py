num1 = int(input("Numero primo:"))
num2 = int(input("Numero secondo:"))
num3 = int(input("Numero terzo:"))

if num1 > num2 and num1 > num3:
    print("Il numero maggiore è",num1)


elif num2 > num1 and num2 > num3:
    print("Il numero maggiore è",num2)


elif num3 > num2 and num3 > num1:
    print("Il numero maggiore è",num3)