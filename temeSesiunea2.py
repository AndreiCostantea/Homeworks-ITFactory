# teme

# (1)
# in "if else" se executa si partea adevarata dar si partea falsa a conditiei.
# Daca conditia este adevarata, atunci se executa block-ul "if", iar daca conditia
# este falsa, se executa blocul "else"

# (2)

x = int(input('Introdu un numar: '))

if x >= 0:
    print(f"{x} este numar natural.")
else:
    print(f'{x} nu este numar natural')

# (3)

if x > 0:
    print(f'{x} este numar pozitiv')
elif x == 0:
    print(f'{x} este numar neutru')
else:
    print(f'{x} este numar negativ')

# (4)

if -2 < x < 13:
    print(f'{x} este intre -2 si 13')
else:
    print(f'{x} nu este intre -2 si 13')

# (5)

y = int(input('Alege inca un numar: '))

if x-y < 5:
    print(f'Diferenta dintre {x} si {y} este mai mica de 5')
else:
    print(f'Diferenta dintre {x} si {y} nu este mai mica de 5')

# (6)

if not(x > 5 and x < 27):
    print(f'{x} nu este intre 5 si 27')
else:
    print(f'{x} este intre 5 si 27')

# (7)

if x == y:
    print(f'{x} si {y} sunt egale')
elif x < y:
    print(f'{y} este mai mare decat {x}')
else:
    print(f'{x} este mai mare decat {y}')

# (8)

z = int(input('Introdu al 3-lea numar: '))

if x == y == z:
    print('Acesta este un triunghi echilateral')
elif x != y != z:
    print('Acesta este un triunghi oarecare')
else:
    print('Acesta este un triunghi isoscel')

# (9)

litera = input('Introdu o litera: ')

if litera.lower() in ('a', 'e', 'i', 'o', 'u', 'ă', 'î'):
    print('Litera este o vocala')
elif litera.lower() in ('b', 'c', 'd', 'f', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 'ș', 't', 'ț', 'v', 'w', 'x', 'z', 'y'):
    print('Litera este consoana')
else:
    print('Introdu o singura litera')

# (10)

nota = float(input('Introdu nota de la test: '))

if 10 >= nota >= 9:
    print('A')
elif 8 <= nota < 9:
    print('B')
elif 7 <= nota < 8:
    print('C')
elif 6 <= nota < 7:
    print('D')
elif 4 < nota < 6:
    print('E')
elif 0 <= nota <= 4:
    print('F')
elif nota > 10:
    print('Nota prea mare. Nu poti lua mai mult de 10')
else:
    print('Nota prea mica. Nu poti lua mai putin de 0')