from temeSesiunea6 import Cont

class TestCont:

    def setup_method(self):
        self.Cont = Cont('RO70PORL1851589282479371', 'Andrei Costantea', 5000)

    def teardown_method(self):
        print('Final')

    def test_afisareSold(self):
        rezultat = self.Cont.afisareSold()
        expected = 5000
        assert rezultat == expected, 'Afisarea soldului nu este implementata corect'

    def test_debitareCont(self):
        rezultat = self.Cont.debitareCont(250)
        expected = 4750
        assert rezultat == expected, 'Calculul de debitare a contului este implementat gresit'

    def test_creditareCont(self):
        rezultat = self.Cont.creditareCont(500)
        expected = 5500
        assert rezultat == expected, 'Calculul de creditare a contului este implementat gresit'