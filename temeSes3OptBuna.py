# tema optionala

jucatori = ['Andrei', 'Alexandru', 'Valentin', 'Sorin', 'Catalin']

schimbari_efectuate = 0
schimbari_max = 3

rezerva = str(input('Alege o rezerva sa intre in teren: '))
jucator = str(input('Alege un jucator sa iasa din teren: '))

if jucator in jucatori and 0 < schimbari_max <= 3:
    jucatori.remove(jucator)
    jucatori.append(rezerva)
    schimbari_efectuate = schimbari_efectuate + 1
    schimbari_max = schimbari_max - 1
    print(f'A intrat {rezerva}, a iesit {jucator}, mai ai {schimbari_max} schimbari')
elif jucator not in jucatori:
    print(f'Nu se poate efectua schimbarea deparece jucatoul {jucator} nu e in teren')
    print(f'Mai ai {schimbari_max} schimbari')

print(f'In teren sunt: {jucatori}')