from unittest import TestCase
from codigo_avulso_test_tutorial.figura_geometrica import FiguraGeometrica


# O nome da classe deve iniciar com a palavra Test
class TestFiguraGeometrica(TestCase):

    # Inicia as variaveis usadas nos testes
    def setUp(self):
        TestCase.setUp(self)
        self.fig = FiguraGeometrica()

    # Todos os testes deven começar com test_

    def test_get_area(self):
        self.assertRaises(NotImplementedError, self.fig.get_area)

    def test_get_perimetro(self):
        self.assertRaises(NotImplementedError, self.fig.get_perimetro)
