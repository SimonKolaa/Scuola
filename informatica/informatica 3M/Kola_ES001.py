fruit = ["mele, banan, uva ,melone"]
for i in fruit:
  print(i)
  fruit.append("kiwi")
  print("\n")
  
  
fruit.pop("banana")
print("\n")
for i in fruit:
    print(i)
    
print("\n")
print(fruit[2])