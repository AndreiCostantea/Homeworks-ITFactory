# teme

# (1)

#masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# for
# for i in range(len(masini)):
#     print(f'Masina mea preferata este: {masini[i]}')
#     i +=1
# for each
# for marca in masini:
#     print(f'Masina mea preferata este {marca}')
# while
# i = 0
# while i <= len(masini)-1:
#     print(f'Masina mea preferata este: {masini[i]}')
#     i += 1

# (2)

# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# cars = []
# x = len(masini)
# while x > 0:
#     for masina in masini:
#         if masina == masini[0]:
#             cars.append(masina.lower())
#             x -= 1
#         elif masina == masini[-1]:
#             cars.append(masina.lower())
#             x -= 1
#         else:
#             cars.append(masina.upper())
#             x -= 1
#
# else:
#     print(cars)

# (3)

# for marca in masini:
#     if marca == 'Mercedes':
#         print('Am gasit masina dorita de dvs.')
#         break
#     else:
#         print(f'Am gasit masina {marca}. Mai cautam!')

# (4)

# for marca in masini:
#     if marca == 'Trabant':
#         continue
#     elif marca == 'Lăstun':
#         continue
#     else:
#         print(f'S-ar putea sa va placa masina {marca}')

# (5)
# masini_vechi =[]
#
# for marca in masini:
#     if marca == 'Trabant':
#         masini_vechi.append(marca)
#         masini.remove(marca)
#         masini.append('Tesla')
#     elif marca == 'Lăstun':
#         masini_vechi.append(marca)
#         masini.remove(marca)
#
# print(f'Modele noi: {masini}')
# print(f'Modele vechi: {masini_vechi}')

# (6)

# pret_masini = {'Dacia': 6800, 'Lăstun': 500, 'Opel': 1100, 'Audi': 19000, 'BMW': 23000}
# x = 15000
# for model, pret in pret_masini.items():
#     if pret <= x:
#         print(f'Puteti alege masina {model}')
#     else:
#         print(f'{model} este {pret}, mai aveti nevoie de {pret - x} de euro')

# (7)

# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

# x = 0
# for nr in numere:
#     if nr == 3:
#         x += 1
# print(x)


# (8)

# s = 0
# for i in numere:
#     s = s + i
# print(f'Suma numerelor este: {s}')


# (9)

# for nr1 in range(len(numere)-1):
#     for nr2 in range(len(numere)-1):
#         if numere[nr2] < numere[nr2 + 1]:
#             numere[nr2], numere[nr2+1] = numere[nr2+1], numere[nr2]
# print(numere[0])


# (10)

# for x in range(len(numere)):
#     if numere[x] > 0:
#         numere[x] = -numere[x]
# print(numere)
