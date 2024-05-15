import unittest
from unittest.mock import Mock

from calculation import add, subtract, multiplication, division


class Test_Calculator(unittest.TestCase):

    def test_add(self):
        result = add(4, 6)
        self.assertEqual(result, 10)

    def test_subtract(self):
        result = subtract(-20, 8)
        self.assertEqual(result, -28)

    def test_multiply(self):
        result = multiplication(-5, -6)
        self.assertEqual(result, 30)

    def test_division(self):
        result = division(25, 5)
        self.assertEqual(result, 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            division(30, 0)

    def test_fetch_data(self):
        connect_to_db = Mock()
        connect_to_db.return_value = [('add', 10), ('subtract', -28), ('multiply', 30), ('division', 5)]
        expected_data = [('add', 10), ('subtract', -28), ('multiply', 30), ('division', 5)]
        self.assertEqual(expected_data, connect_to_db.return_value)


if __name__ == '__main__':
    unittest.main()
