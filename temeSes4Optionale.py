# teme optionale
import random

# (1)

# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere_pare = []
# numere_impare = []
# numere_pozitive =[]
# numere_negative = []
#
# for x in alte_numere:
#     if x % 2 == 0:
#         numere_pare.append(x)
#         if x > 0:
#             numere_pozitive.append(x)
#         elif x < 0:
#             numere_negative.append(x)
#     elif x % 2 != 0:
#         numere_impare.append(x)
#         if x > 0:
#             numere_pozitive.append(x)
#         elif x < 0:
#             numere_negative.append(x)
# print(f'Numerele pare sunt: {numere_pare}')
# print(f'Numerele impare sunt: {numere_impare}')
# print(f'Numerele pozitive sunt: {numere_pozitive}')
# print(f'Numerele negarive sunt: {numere_negative}')

# (2)

# for i in range(len(alte_numere)-1):
#     for j in range(len(alte_numere)-1):
#         if alte_numere[j] > alte_numere[j+1]:
#             alte_numere[j], alte_numere[j+1] = alte_numere[j+1], alte_numere[j]
# print(alte_numere)

# (3)

numar_secret = random.randint(0, 30)
numar_ghicit = int(input('Introdu un numar intre 1 si 30: '))

while numar_ghicit != numar_secret:
    if numar_ghicit > numar_secret:
        print('Nr secret este mai mic')
        numar_ghicit = int(input('Introdu un numar intre 1 si 30: '))
    elif numar_ghicit < numar_secret:
        print('Nr secret este mai mare')
        numar_ghicit = int(input('Introdu un numar intre 1 si 30: '))
else:
    print('Felicitari ai ghicit!')

# (4)

# numar = int(input('Alege un numar: '))
#
# for i in range(1, numar+1):
#     for j in range(1,i+1):
#         print(i, end='')
#     print()

# (5)

# tastatura_telefon = [
# [1, 2, 3],
# [4, 5, 6],
# [7, 8, 9],
# [0]
# ]
#
# for i in tastatura_telefon:
#     for j in i:
#         print(f'Cifra curenta este: {j}')


