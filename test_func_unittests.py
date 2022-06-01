import unittest
from functions_to_test import Calculator

class TestForCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(Calculator.add(4, 8), 12)
        self.assertEqual(Calculator.add(10, 5), 15)

    def test_subtract(self):
        self.assertEqual(Calculator.subtract(8, 4), 4)
        self.assertEqual(Calculator.subtract(7, 9), -2)

    def test_multiply(self):
        self.assertEqual(Calculator.multiply(4, 8), 32)
        self.assertEqual(Calculator.multiply(7, 6), 42)

    def test_divide(self):
        self.assertRaises(ValueError, lambda: Calculator.divide(10, 0))
        self.assertEqual(Calculator.divide(10, 2), 5)

if __name__ == '__main__':
    unittest.main()
