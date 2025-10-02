import unittest
from calculatrice import Calculatrice, ErreurDivisionParZero, ErreurPileVide

class TestCalculatrice(unittest.TestCase):

    def setUp(self):
        self.calc = Calculatrice()

    def test_pile_vide(self):
        with self.assertRaises(ErreurPileVide):
            self.calc.evaluer(["+"])

    def test_division_par_zero(self):
        with self.assertRaises(ErreurDivisionParZero):
            self.calc.evaluer(["5", "0", "/"])

    def test_addition(self):
        self.assertEqual(self.calc.evaluer(["2", "3", "+"]), 5)

    def test_soustraction(self):
        self.assertEqual(self.calc.evaluer(["10", "4", "-"]), 6)

    def test_multiplication(self):
        self.assertEqual(self.calc.evaluer(["3", "5", "*"]), 15)

    def test_division(self):
        self.assertEqual(self.calc.evaluer(["8", "2", "/"]), 4)

    def test_modulo(self):
        self.assertEqual(self.calc.evaluer(["10", "3", "%"]), 1)

    def test_puissance(self):
        self.assertEqual(self.calc.evaluer(["2", "3", "^"]), 8)

    def test_factoriel(self):
        self.assertEqual(self.calc.evaluer(["5", "!"]), 120)


if __name__ == '__main__':
    unittest.main()
