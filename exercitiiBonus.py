from datetime import datetime
from datetime import date
import pytz
# Exercitii optionale - Bonus

# (1)

# def nrComune(lista1, lista2):
#     for x in lista1 and lista2:
#         if x in lista1 and x in lista2:
#             lista1.remove(x)
#             print(x)
#         else:
#             continue
#
# nrComune([1, 1, 2, 3], [2, 2, 3, 4])

# (2)

# def reducerePret(pret, reducere):
#     if 0 < reducere < 100:
#         pret = pret - pret * reducere / 100
#     else:
#         print('Reducerea este invalida!')
#     print(f'Pretul redus al produsului este: {pret}')
# reducerePret(int(input('Introdu pretul produsului: ')), int(input('Cat % este reducerea?: ')))
# reducerePret(100, 10)

# (3)

# def timp():
#     dataora = datetime.now()
#     print(f'Data si ora curenta in Romania este: {dataora}')
#
# timp()

# def timpChina():
#     oraCh = pytz.timezone('Asia/Shanghai')
#     china = datetime.now(oraCh)
#     print(china)
#
# timpChina()

# (4)

# def ziuaDeNastere():
#     ro = datetime.now()
#     ziuaMea = date(2023, 4, 24)
#     print(f'Pana la ziua mea mai sunt: {(ziuaMea - ro.date()).days} de zile')
#
# ziuaDeNastere()
