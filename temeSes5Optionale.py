# teme optionale

# (1)

# def zileLuna(luna):
#     luni31 = ['ianuraie', 'martie', 'mai', 'iulie', 'august', 'octombrie', 'decembrie']
#     luni30 = ['aprilie', 'iunie', 'septembrie', 'noiembrie']
#     luni29 = ['februarie']
#     if luna in luni31:
#         print(f'{luna} are 31 de zile.')
#     elif luna in luni30:
#         print(f'{luna} are 30 de zile.')
#     elif luna in luni29:
#         an = input('Este an bisect sau nu?: ')
#         if an == 'Da':
#             print(f'In an bisect {luna} are 29 de zile')
#         elif an == 'Nu':
#             print(f'Daca nu e an bisect {luna} are 28 de zile')
#         else:
#             print('Raspunde cu da sau nu!')
#     else:
#         print('Aceasta luna nu exista!')
#
# zileLuna(input('Alege o luna din an: '))
# zileLuna('aprilie')

# (2)

# def operatii(a, b):
#     print(f'Suma numerelor este: {a + b}')
#     print(f'Diferenta numerelor este: {a - b}')
#     print(f'Inmultirea numerelor este: {a * b}')
#     print(f'Impartirea numerelor este: {a / b}')
#
# operatii(int(input('Introdu primul numar: ')), int(input('Introdu al doilea numar: ')))
# operatii(8, 4)
#
# def operatii(a, b):
#     w = a + b
#     x = a - b
#     y = a * b
#     z = a / b
#     print('Suma:', w)
#     print('Diferenta:', x)
#     print('Inmultirea:', y)
#     print('Impartirea:', z)
#
#
# operatii(10, 2)

# (3)

# def lista(cifre):
#     dictionar = {}
#     for x in range(len(cifre)+1):
#         dictionar[x] = str(cifre.count(x))
#     return dictionar
# numere = lista([1, 3, 1, 5, 9, 7, 7, 5, 5])
# print(numere)

# (4)

# def maxim(a, b, c):
#     print(max(a, b, c))
#
# maxim(int(input('Adauga primul numar: ')), int(input('Adauga al doilea numar: ')), int(input('Adauga al treilea numar: ')))
# maxim(5, 8, 1)

# (5)

# def nr(a):
#     print(sum(range(0, a+1)))
#
# nr(int(input('Alege un numar: ')))
# nr(8)

