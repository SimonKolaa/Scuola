#visto che la consegna è fatto con chat, farò l'esercizio con chat
# Exercise 1: Write to a File
with open("exercise1.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("Welcome to file handling in Python.\n")

# Exercise 2: Read from a File
with open("exercise1.txt", "r") as file:
    contents = file.read()
    print(contents)

# Exercise 3: Append to a File
with open("exercise1.txt", "a") as file:
    file.write("This line was appended.\n")
#anche nella consegna c'era this line was appended
# Exercise 4: Read Lines from a File
with open("exercise1.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())

# Exercise 5: Copy a File
import shutil

shutil.copyfile("exercise1.txt", "exercise1_copy.txt")
#cos'è shutil?