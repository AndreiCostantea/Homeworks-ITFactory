# teme optionale
# (1)
# impar = input("Scrie un string de dimensiune impara: ")
# print(len(impar))
# def mijloc(impar):
#     return impar[(len(impar)-1)//2]
# print(mijloc(impar))

# (2)
# cuvant = input('Introdu cuvant: ')
# palindromCuvant = cuvant[::-1]
# assert palindromCuvant == cuvant
# print('Cuvantul este palindrom')

# (3)
# mancare = input('Scrie: '); a, b = mancare.split(); print(a); print(b)

# (4)
temaOpt = input('Scrie ceva: ')
primulCaracter = temaOpt[0]
temaOpt = temaOpt.replace(primulCaracter, primulCaracter.upper())
temaOpt = primulCaracter + temaOpt[1:len(temaOpt)-1] + primulCaracter
print(temaOpt)


# (5)
# user = input('Introdu userul: ')
# parola = input('Introdu parola: ')
# parola = '*' * len(parola)
# print(f'Parola pentru {user} este {parola} si are {len(parola)} caractere')