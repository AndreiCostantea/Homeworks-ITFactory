# teme optionale

# (1)

# x = int(input('Introdu un numar: '))
# x = str(x)
# if len(x) >= 4:
#     print(f'{x} are {len(x)} cifre')
# else:
#     print(f'{x} nu are minim 4 cifre')

# (2)

# x =  int(input('Introdu un numar: '))
# x = str(x)
#
# if len(x) == 6:
#     print(f'{x} are 6 cifre')
# else:
#     print(f'{x} nu are 6 cifre')

# (3)
# x =  int(input('Introdu un numar: '))
#
# if x %2 == 0:
#     print(f'{x} este numar par')
# else:
#     print(f'{x} este numar impar')

# (4)

# x = int(input('Introdu primul numar: '))
# y = int(input('Introdu al doilea numar: '))
# z = int(input('Introdu al treilea numar: '))
#
# if x > y and  x > z:
#     print(f'{x} este cel mai mare numar')
# elif y > z and y > x:
#     print(f'{y} este cel mai mare numar')
# elif z > y and z > x:
#     print(f'{z} este cel mai mare numar')
# else:
#     print('Alege 3 numere diferite')

# (5)

# x = int(input('Introdu primul unghi: '))
# y = int(input('Introdu al doilea unghi: '))
# z = int(input('Introdu al treilea unghi: '))
#
# if x+y+z == 180:
#     print('Triunghiul este valid')
# else:
#     print('Triunghiul nu este valid')

# (6)

# propozitie = 'Coral is either the stupidest animal or the smartest rock'
#
# x = int(input('Numar: '))
# print(propozitie[0:-x])

# (7)

# propozitie = 'Coral is either the stupidest animal or the smartest rock'
#
# porpozitieNoua = propozitie[0:5] + propozitie [53:57]
# print(porpozitieNoua)

# (8)

# propozitie = 'Coral is either the stupidest animal or the smartest rock'
#
# ind = propozitie.index('rock')
# x = slice(0, ind)
# print(propozitie[x])

# (9)

# prop = str(input('Scrie: '))
# assert prop[0].lower() == prop[-1].lower()

# (10)

# numere = '0123456789'
#
# x = slice(0, 10, 2)
# print('Numerele pare sunt: ' + numere[x])
#
# y = slice(1, 10, 2)
# print('Numerele impare sunt: ' + numere[y])