from temeSesiunea6 import Cerc

class TestCerc:

    def setup_method(self):
        self.Cerc = Cerc(2, 'Rosu')

    def teardown_method(self):
        print('Final')

    def test_aria(self):
        rezultat = self.Cerc.aria()
        expected = 4
        assert rezultat == expected, 'Calculul ariei cercului este implementat gresit'

    def test_diametru(self):
        rezultat = self.Cerc.diametru()
        expected = 4
        assert rezultat == expected, 'Calculul diametrului cercului este implementat gresit'

    def test_circumferinta(self):
        rezultat = self.Cerc.circumferinta()
        expected = 4
        assert rezultat == expected, 'Calculul circumferintei cercului este implementat gresit'

    def test_descriere(self):
        rezultat = self.Cerc.descriere_cerc()
        expected = 2, 'Rosu'
        assert rezultat == expected, 'Descrierea cercului nu este implementata corect'