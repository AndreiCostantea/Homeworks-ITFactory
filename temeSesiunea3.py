# teme

# (1)

note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
print(note_muzicale)

noteSliced = note_muzicale[::-1]
print(noteSliced)

noteSliced.reverse()
print(noteSliced)

# (2)

print(noteSliced.count('do'))

# (3)

list1 = [3, 1, 0, 2]
list2 = [6, 5, 4]
# varianta 1
listeUnite = list1 + list2
print(listeUnite)
# varianta 2
list1.extend(list2)
print(list1)

# (4)

listeUnite.remove(0)
print(listeUnite)

# (5)

if len(listeUnite) > 0:
    print('Lista nu este goala')
else:
    print('Lista este goala')

# (6)

listeUnite.clear()
print(listeUnite)

# (7)

if len(listeUnite) > 0:
    print('Lista nu este goala')
else:
    print('Lista este goala')

# (8)

dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
print(dict1.keys())

# (9)

ana = dict1.get('Ana')
gigel = dict1.get('Gigel')
dorel = dict1.get('Dorel')
print(f'Ana a luat nota: {ana}')
print(f'Gigel a luat nota: {gigel}')
print(f'Dorel a luat nota: {dorel}')

# (10)

marireDorel = {'Dorel': 6}
dict1.update(marireDorel)
print(dict1)
dorel = dict1.get('Dorel')
print(f'Dupa marire, Dorel are nota: {dorel}')

# (11)

dict1.pop('Gigel')
ionica = {'Ionica':9}
dict1.update(ionica)
print(dict1)

# (12)

zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}

zile_sapt.add('luni')
print(zile_sapt)

# (13)

if weekend.issubset(zile_sapt):
    print('Weekend este un subset al zilelor din săptămânii.')
else:
    print('Weekend nu este un subset al zilelor din săptămânii.')

# (14)

print(zile_sapt.difference(weekend))

# (15)

print(zile_sapt.intersection(weekend))