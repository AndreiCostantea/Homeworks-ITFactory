from temeSesiunea6 import Dreptunghi

class TestDreptunghi:

    def setup_method(self):
        self.Dreptunghi = Dreptunghi(2, 5, 'albastru')

    def teardown_method(self):
        print('Final')

    def test_descrie(self):
        rezultat = self.Dreptunghi.descrie()
        expected = 2, 5, 'albastru'
        assert rezultat == expected, 'Descrierea nu este implementata corect'

    def test_aria(self):
        rezultat = self.Dreptunghi.aria()
        expected = 10
        assert rezultat == expected, 'Calculul ariei nu este implementat corect'

    def test_perimetru(self):
        rezultat = self.Dreptunghi.perimetru()
        expected = 14
        assert rezultat == expected, 'Calculul perimetrului nu este implementat corect'

