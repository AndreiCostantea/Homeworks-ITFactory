# teme obligatorii

# (1)

class Cerc:
    raza = 0
    culoare = None
    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def descriere_cerc(self):
        return self.raza, self.culoare
        # print(self.raza)
        # print(self.culoare)

    def aria(self):
        return (self.raza * self.raza)
        #print(f'Aria cercului este: {self.raza * self.raza}π')

    def diametru(self):
        return 2 * self.raza
        #print(f'Diametru cercului este {2 * self.raza}')

    def circumferinta(self):
        return 2 * self.raza
        #print(f'Circumferinta cercului este: {2 * self.raza}π')

cerc1 = Cerc(5, 'Albastru')
cerc2 = Cerc(2, 'Rosu')

# (2)

class Dreptunghi:
    lungime = 0
    latime = 0
    culoare = None
    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descrie(self):
        return self.lungime, self.latime, self.culoare
        # print(self.lungime)
        # print(self.latime)
        # print(self.culoare)


    def aria(self):
        return self.lungime * self.latime
        # print(f'Aria dreptunghiului este {self.lungime * self.latime}')


    def perimetru(self):
        return 2 * (self.lungime + self.latime)
        # print(f'Perimetrul dreptunghoiului este: {2 * (self.lungime + self.latime)}')

    def schimba_culoarea(self, culoareNoua):
        self.culoare = culoareNoua

dreptunghi1 = Dreptunghi(4, 2, 'Albastru')

# (3)

class Angajat:
    nume = None
    prenume = None
    salariu = 0
    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descriere(self):
        return self.nume, self.prenume, self.salariu
        # print(f'Numele angajatului: {self.nume}')
        # print(f'Prenumele angajatului: {self.prenume}')
        # print(f'Salariul angajatului: {self.salariu}')

    def numeComplet(self):
        return self.nume + self.prenume
        #print(f'Numele complet al angajatul: {self.nume} {self.prenume}')

    def salariuLunar(self):
        return self.salariu
        #print(f'Salariul lunar al angajatului este: {self.salariu}')

    def salariuAnual(self):
        return self.salariu * 12
        print(f'Salariul anual al angajatului este: {self.salariu * 12}')

    def marireSalariu(self, procent):
        return self.salariu + self.salariu * procent / 100
        #print(f'Dupa marire salariul este: {self.salariu + self.salariu * procent / 100}')
        self.salariu = self.salariu + self.salariu * procent / 100

angajat1 = Angajat('Costantea', 'Andrei', 100)
angajat1.marireSalariu(10)

# (4)

class Cont:
    iban = 0
    titularCont = None
    sold = 0
    def __init__(self, iban, titular, sold):
        self.iban = iban
        self.titularCont = titular
        self.sold = sold

    def afisareSold(self):
        return self.sold
        #print(f'Titularul {self.titularCont} are in contul {self.iban} suma de {self.sold}')

    def debitareCont(self, suma):
        return self.sold - suma
        #print(f'Am debitat contul cu {suma} de lei. Noul sold al contului este: {self.sold - suma}')
        self.sold = self.sold - suma

    def creditareCont(self, suma):
        return self.sold + suma
        #print(f'Am creditat contul cu {suma} de lei. Noul sold al contului este: {self.sold + suma}')
        self.sold = self.sold + suma

cont1 = Cont('RO70PORL1851589282479371', 'Costantea Andrei', 5000)
cont1.afisareSold()
# iban luat random de pe randomiban.com
