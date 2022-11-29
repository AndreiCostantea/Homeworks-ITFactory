# teme obligatorii
from abc import abstractmethod, ABC


# (1)

class FormaGeometrica(ABC):
    PI = 3.14

    @abstractmethod
    def aria(self):
        raise NotImplementedError

    def descrie(self):
        print('Cel mai probabil am colturi')

class Patrat(FormaGeometrica):
    def __init__(self, l):
        self.__latura = l

    @property
    def latura(self):
        return self.__latura

    @latura.getter
    def latura(self):
        print(f'Latura are lungimea de: {self.__latura} cm')
        return self.__latura

    @latura.setter
    def latura(self, latura):
        print(f'Ai setat ca latura sa aiba {self.__latura} cm')
        self.__latura = latura

    @latura.deleter
    def latura(self):
        print('Am sters latura')
        self.__latura = None

    def aria(self):
        print(f'Aria patratului este: {self.__latura * self.__latura}')

class Cerc(FormaGeometrica):
    __raza = 0

    def __init__(self, raza):
        self.__raza = raza

    @property
    def raza(self):
        return self.__raza

    @raza.getter
    def raza(self):
        print(f'Raza cercului este de {self.__raza} cm')
        return self.__raza

    @raza.setter
    def raza(self, razaNoua):
        self.__raza = razaNoua
        print(f'Am setat raza cercului la: {self.__raza} cm')

    @raza.deleter
    def raza(self):
        print('Am sters raza cercului')
        self.__raza = None

    def aria(self):
        print(f'Aria cercului este: {self.PI * (self.__raza * self.__raza)}')

    def descrie(self):
        print('Eu nu am colturi')


patrat = Patrat(2)
patrat.latura
patrat.latura = 4
patrat.latura
patrat.aria()
patrat.descrie()
cerc = Cerc(4)
cerc.raza
cerc.raza = 2
cerc.raza
cerc.aria()
cerc.descrie()


