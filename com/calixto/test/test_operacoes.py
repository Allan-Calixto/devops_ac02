from unittest import TestCase
from com.calixto.operacoes import Operacoes

class TestOperacoes(TestCase):

    def SetUp(Self):
        self.operacoes = Operacoes()

    def test_soma(self):
        self.assertEqual(self.operacoes.soma([1,5]), 6, "Should be 6")
