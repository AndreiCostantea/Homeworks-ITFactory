# (1)
# o variabila este o zona din memoria unui calculator care tine date,
# un fel de folder din calculator in care punem diferite poze, jocuri, etc

# (2)
ceas = 'Casio'
model = 1330
pret = 129.99
inStoc = False
print(ceas)
print(model)
print(pret)
print(inStoc)

#(3)
print('--------------------------')
print(type(ceas))
print(type(model))
print(type(pret))
print(type(inStoc))
print('-----------------------')

# (4)
round(pret)
print(round(pret))
pret = round(pret)
print(pret)
print(type(pret))
print('------------------------')

# (5)
print(f'Eu vreau un ceas {ceas}.')
print(f'Vreau sa fie modelul {model}.')
print(f'Acesta costa aproximativ {pret} de lei.')
print(f'Este valabil pe site?: {inStoc}')
print('---------------------------')

# (6)
nume = input('Nume: ')
prenume = input('Prenume: ')
print(f'Numele complet are {len(nume + prenume)} caractere')
print('---------------------------')

# (7)
lungimeDreptunghi = int(input('Lungimea dreptunghiului este:' ))
latimeDreptunghi = int(input('Latimea dreptunghiului este:'))
print(f'Aria dreptunghiului este {lungimeDreptunghi * latimeDreptunghi}')
print('--------------------------------')

# (8)
propozitie = 'Coral is either the stupidest animal or the smartest rock'
propozitie.count(' the ')
propozitie.count('the')
# sau
print(propozitie[15:-1].count('the'))
# (9)
print(propozitie.count('the'))
print(propozitie.count(' the '))
print(propozitie[15:-1].count('the'))

# (10)
propozitie.isnumeric()
assert propozitie.isnumeric() == False


