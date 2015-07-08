#lists and nestled loops

family=["Jessica","Michael","Maria"]
baskinrobins=["Coffee","De Luce","Cotton Candy"]

print("Printing Family")
print(family)
for person in family:
    print(person)

print("Printing Baskinrobins")
print(baskinrobins)
for icecream in baskinrobins:
    print(icecream)

print("Printing Combinations")
for person in family:
    for icecream in baskinrobins:
        print(person,icecream)
