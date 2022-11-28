# teme optionale
from datetime import datetime
# (1)

class Factura:
    seria = 'AC'
    numar = 0
    numeProdus = None
    cantitate = 0
    pret_buc = 0
    def __init__(self, numar, numeProdus, cantitate, pret_buc):
        self.numar = numar
        self.numeProdus = numeProdus
        self.cantitate = cantitate
        self.pret_buc = pret_buc

    def schimba_cantitatea(self, cantitateNoua):
        self.cantitate = cantitateNoua

    def schimba_pretul(self, pret):
        self.pret_buc = pret

    def schimba_nume_produs(self, nume):
        self.numeProdus = nume

    def genereaza_factura(self):
        print(f'Factura seria: {self.seria} numar: {self.numar}')
        dataora = datetime.now()
        dataAzi = dataora.date()
        print(f'Data: {dataAzi}')
        print('Produs     Cantitate   Pret bucata  Total')
        print(f'{self.numeProdus}     {self.cantitate}        {self.pret_buc}           {self.cantitate * self.pret_buc}')



factura1 = Factura(1, 'tastatura', 7, 700)


# (2)

class Masina:
    marca = 'Dacia'
    model = None
    vitezaMaxima = None
    viteza_actuala = 0
    culoarea = 'Gri'
    culori_discponibile = {'alb', 'negru', 'albastru', 'rosu', 'galben', 'verde', 'portocaliu'}
    inmatriculata = False
    def __init__(self, model, vitezaMaxima):
        self.model = model
        self.vitezaMaxima = vitezaMaxima

    def descrie(self):
        print(f'Marca masinii este: {self.marca}')
        print(f'Modelul masinii este: {self.model}')
        print(f'Viteza maxima a masinii este: {self.vitezaMaxima}')
        print(f'Viteza actuala a masinii este: {self.viteza_actuala}')
        print(f'Culoarea masinii este: {self.culoarea}')
        print(f'Masina inmatriculata: {self.inmatriculata}')

    def inmatriculare(self):
        self.inmatriculata = True

    def vopseste(self, culoareNoua):
        if culoareNoua in self.culori_discponibile:
            self.culoarea = culoareNoua
            print(f'Ai vopsit masina in {culoareNoua}.')
        else:
            print(f'Culoarea {culoareNoua} nu este disponibila.')

    def accelereaza(self, vitezaNoua):
        if 1 <= vitezaNoua <= self.vitezaMaxima:
            self.viteza_actuala = vitezaNoua
        elif vitezaNoua > self.vitezaMaxima:
            self.viteza_actuala = 250
        else:
            print('Nu poti avea viteza negativa')

    def franeaza(self):
        self.viteza_actuala = 0
        print('Masina s-a oprit')


masina1 = Masina('Sandero', 250)

# (3)

class TodoList:
    todo = {}

    def adaugaTask(self, nume, descriere):
        self.todo[nume] = descriere
        print(self.todo)

    def finalizeazaTask(self, nume):
        if nume in self.todo:
            print(f'Felicitari! Ai terminat task-ul: {nume}')
            del self.todo[nume]
            print(self.todo)
        else:
            print('Task-ul nu exista')

    def afiseazaToDo(self):
        print(self.todo.keys())

    def detaliiSuplimentare(self,numeTask):
        if numeTask not in self.todo:
            intrebare = input('Task-ul nu exista. Adaugam task-ul in ToDo List?: ')
            if intrebare == 'Da':
                descriere = input('Alege descrierea taskului: ')
                self.todo[numeTask] = descriere
                print(self.todo)
            elif intrebare == 'Nu':
                print('La revedere!')
            else:
                print('Raspunde cu Da sau Nu!')
        else:
            print('Taskul exista deja!')

todo1 = TodoList()
