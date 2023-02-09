from temeSesiunea6 import Angajat

class TestAngajat:

    def setup_method(self):
        self.Angajat = Angajat('Andrei', 'Costi', 5000)

    def teardown_method(self):
        print('Final')

    def test_numeComplet(self):
        rezultat = self.Angajat.numeComplet()
        expected = 'Andrei' + 'Costi'
        assert rezultat == expected, 'Numele complet nu este implementat corect'

    def test_salariuLunar(self):
        rezultat = self.Angajat.salariuLunar()
        expected = 5000
        assert rezultat == expected, 'Salariul lunar este implemetnat gresit'

    def test_salariuAnual(self):
        rezultat = self.Angajat.salariuAnual()
        expected = 60000
        assert rezultat == expected, 'Calculul salariului anual este implementat gresit'

    def test_marireSalariu(self):
        rezultat = self.Angajat.marireSalariu(10)
        expected = 5500
        assert rezultat == expected, 'Calculul de marire a salariului este implementat gresit'

    def test_descriere(self):
        rezultat = self.Angajat.descriere()
        expected = 'Andrei', 'Costi', 5000
        assert rezultat == expected, 'Descreirea nu este implementata corect'