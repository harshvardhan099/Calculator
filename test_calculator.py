import unittest
from calculator import Calculator


class Test_Calculator(unittest.TestCase):

    def test_add(self):
        result = Calculator.add(4, 6)
        self.assertEqual(result, 10)

    def test_add_negative(self):
        result = Calculator.add((-2), 8)
        self.assertEqual(result, 6)

    def test_subtract(self):
        result = Calculator.subtract(-20, 8)
        self.assertEqual(result, -28)

    def test_multiply(self):
        result = Calculator.multiplication(-5, -6)
        self.assertEqual(result, 30)

    def test_division(self):
        result = Calculator.division(25, 5)
        self.assertEqual(result, 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            Calculator.division(30, 0)