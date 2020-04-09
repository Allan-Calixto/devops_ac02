from unittest import TestCase
from com.calixto.operacoes import Operacoes

class TestOperacoes(TestCase):
    def setUp(self):
        self.operacoes = Operacoes()

    def test_soma(self):
        self.assertEqual(self.operacoes.soma([4,6]), 10, 'Should be 10')