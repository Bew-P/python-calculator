import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)        

    # Add the following test methods to the TestCalculator class:
    def test_add2(self):
        self.assertEqual(self.calc.add(0, -2), -2)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)

    def test_subtract2(self):
        self.assertEqual(self.calc.subtract(5, 0), 5)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 7), 21)

    def test_multiply2(self):
        self.assertEqual(self.calc.multiply(4, 2), 8)

    def test_divide(self):
        self.assertEqual(self.calc.divide(5, 2), 2)
    
    def test_divide2(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(5, 2), 1)
    
    def test_modulo2(self):
        self.assertEqual(self.calc.modulo(9, 5), 4)

if __name__ == '__main__':
    unittest.main()