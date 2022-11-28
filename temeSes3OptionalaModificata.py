# tema optionala

jucatori = ['Andrei', 'Alexandru', 'Valentin', 'Sorin', 'Catalin']
rezerve = ['Simona', 'Raluca', 'Edith', 'Cristina', 'Stefania']
schimbariMax = 3
schimbariEfectuate = 0
print(f'Rezervele sunt: {rezerve}')
print(f'Jucatorii din teren sunt: {jucatori}')
rezerva = str(input('Alege o rezerva sa intre in teren: '))
jucator = str(input('Alege un jucator sa iasa din teren: '))

if jucator in jucatori and 0 < schimbariMax <= 3 and rezerva in rezerve:
    jucatori.remove(jucator)
    rezerve.remove(rezerva)
    schimbariEfectuate = schimbariEfectuate + 1
    schimbariMax = schimbariMax - 1
    jucatori.append(rezerva)
    print(f'A intrat {rezerva}, a iesit {jucator}. Mai ai {schimbariMax} schimbari.')
    print(f'Ai efectuat {schimbariEfectuate} schimbari')
    print('-----------------------------------------------------------------------------')
    schimbare = str(input('Mai vrei sa faci o schimbare? '))
    if schimbare == 'Nu':
        exit()
    elif schimbare == 'Da':
        print(f'Rezervele sunt: {rezerve}')
        print(f'Jucatorii din teren sunt: {jucatori}')
        rezerva = str(input('Alege o rezerva sa intre in teren: '))
        jucator = str(input('Alege un jucator sa iasa in teren: '))
        assert jucator in jucatori and 0 < schimbariMax <= 3 and rezerva in rezerve
        jucatori.remove(jucator)
        rezerve.remove(rezerva)
        schimbariEfectuate = schimbariEfectuate + 1
        schimbariMax = schimbariMax - 1
        jucatori.append(rezerva)
        print(f'A intrat {rezerva}, a iesit {jucator}. Mai ai {schimbariMax} schimbari.')
        print(f'Ai efectuat {schimbariEfectuate} schimbari')
        print('-----------------------------------------------------------------------------')
        schimbare = str(input('Mai vrei sa faci o schimbare? '))
        if schimbare == 'Nu':
            exit()
        elif schimbare == 'Da':
            print(f'Rezervele sunt: {rezerve}')
            print(f'Jucatorii din teren sunt: {jucatori}')
            rezerva = str(input('Alege o rezerva sa intre in teren: '))
            jucator = str(input('Alege un jucator sa iasa in teren: '))
            assert jucator in jucatori and 0 < schimbariMax <= 3 and rezerva in rezerve
            jucatori.remove(jucator)
            rezerve.remove(rezerva)
            schimbariEfectuate = schimbariEfectuate + 1
            schimbariMax = schimbariMax - 1
            jucatori.append(rezerva)
            print(f'A intrat {rezerva}, a iesit {jucator}. Mai ai {schimbariMax} schimbari.')
            print(f'Ai efectuat toate cele {schimbariEfectuate} schimbari')
            print('Nu mai ai schimbari!')
            print('-----------------------------------------------------------------------------')
        else:
            print('Raspunde cu Da sau Nu!')
    else:
        print('Raspunde cu Da sau Nu!')
elif jucator not in jucatori and rezerva not in rezerve:
    print(f'Nu se poate efectua deoarece jucatorul {jucator} nu e in teren si {rezerva} nu e pe banca de rezerve')
elif jucator not in jucatori:
    print(f'Nu se poate efectua schimbarea deoarece jucatorul {jucator} nu e in teren')
    print(f'Mai ai {schimbariMax} schimbari.')
elif rezerva not in rezerve:
    print(f'Nu se poate efectua schimbarea deoarece jucatorul {rezerva} nu e pe banca de rezerve')
    print(f'Mai ai {schimbariMax} schimbari.')
elif schimbariMax <= 0:
    print('Nu mai ai schimbari la dispozitie')

