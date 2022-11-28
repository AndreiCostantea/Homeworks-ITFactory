# teme obligatorii

# (1)

# def suma(x, y):
#     print(x + y)
#
# suma(4, 6)
# suma(100, 500)

# (2)

# def numar(x):
#     if x % 2 == 0:
#         return True
#     else:
#         return False
#
# raspuns = numar(int(input('Scrie un numar: ')))
# print(raspuns)

# (3)

# def numeComplet(nume, prenume, nume_mijlociu):
#     print(len(nume) + len(prenume) + len(nume_mijlociu))
#
# numeComplet('Andrei', 'Costantea', 'Raul')
# numeComplet('a', 'b', 'c')

# (4)

# def ariaDreptunghi(L, l):
#     print(f'Aria dreptunghiului este: {L * l}')
#
# ariaDreptunghi(int(input('Introdu lungimea: ')), int(input('Introdu latimea: ')))
# ariaDreptunghi(4, 4)

# (5)

# def ariaCercului(R):
#     print(f'Aria cercului este: {(R * R) * 3.14}')
#     print(f'Aria cercului este: {(R * R)}π')
#
# ariaCercului(4)

# (6)

# def propozitie(prop):
#     x = input('Scrie un caracter: ')
#     if x in prop:
#         return True
#     else:
#         return False
#
# if propozitie(input('Scrie ceva: ')):
#     print('True')
# else:
#     print('False')

# (7)

# def prop(cuvinte):
#     low = 0
#     big = 0
#     for x in range(len(cuvinte)):
#         if cuvinte[x].islower() == True:
#             low = low + 1
#         elif cuvinte[x].isupper() == True:
#             big = big + 1
#     print(f'Numarul de caractere lower case este: {low}')
#     print(f'Numarul de caractere upper case este: {big}')
#
# prop(input('Scrie o propozitie: '))

# (8)

# def lista(lista):
#     numerePozitive = []
#     for x in lista:
#         if x > 0:
#             numerePozitive.append(x)
#         else:
#             continue
#     print(numerePozitive)
#
# lista([2, 3, 5, -1, -23, -5, 12, -56, 1, -45])

# (9)

# def numere(a, b):
#     if a > b:
#         print(f'Primul numar {a} este mai mare decat al doilea numar {b}.')
#     elif b > a:
#         print(f'Al doilea numar {b} este mai mare decat primul numar {a}.')
#     else:
#         print('Numerele sunt egale.')
#
# numere(int(input('Introdu primul numar: ')), int(input('Introdu al doilea numar: ')))

# (10)

# def nrSet(nr, set):
#     if nr not in set:
#         print(f'Am adaugat numarul nou {nr} in set')
#         return True
#     else:
#         print(f'Nu am adaugat nuamrul in set. {nr} exista deja in set.')
#         return False
#
# nrSet(4, {2, 4, 6, 7, 9})
