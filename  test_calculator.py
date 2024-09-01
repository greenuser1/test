
import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(5, 3), 8)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -3), -8)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        self.assertEqual(self.calc.subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4, 3), 12)
        self.assertEqual(self.calc.multiply(-2, 5), -10)
        self.assertEqual(self.calc.multiply(0, 7), 0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-10, -2), 5)
        self.assertRaises(ValueError, self.calc.divide, 10, 0)

    def test_power(self):
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.power(5, 0), 1)
        self.assertEqual(self.calc.power(0, 5), 0)

    def test_sqrt(self):
        self.assertEqual(self.calc.sqrt(9), 3)
        self.assertEqual(self.calc.sqrt(0), 0)
        self.assertRaises(ValueError, self.calc.sqrt, -1)

    def test_divide_negative(self):
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(10, -2), -5)

    def test_power_negative_exponent(self):
        self.assertEqual(self.calc.power(2, -1), 0.5)
        self.assertEqual(self.calc.power(10, -2), 0.01)

    def test_sqrt_large_number(self):
        self.assertEqual(self.calc.sqrt(1e6), 1000)

    def test_power_large_numbers(self):
        self.assertEqual(self.calc.power(10, 5), 100000)
        self.assertEqual(self.calc.power(2, 10), 1024)

    def test_add_floats(self):
        self.assertAlmostEqual(self.calc.add(5.5, 2.3), 7.8)
        self.assertAlmostEqual(self.calc.add(-1.1, 1.1), 0.0)

    def test_subtract_floats(self):
        self.assertAlmostEqual(self.calc.subtract(5.5, 2.2), 3.3)
        self.assertAlmostEqual(self.calc.subtract(-1.5, -2.5), 1.0)

    def test_multiply_floats(self):
        self.assertAlmostEqual(self.calc.multiply(3.3, 2.2), 7.26)
        self.assertAlmostEqual(self.calc.multiply(-1.5, 2.5), -3.75)

    def test_divide_floats(self):
        self.assertAlmostEqual(self.calc.divide(7.7, 2.2), 3.5)
        self.assertAlmostEqual(self.calc.divide(-7.5, 3.0), -2.5)

    def test_power_zero(self):
        self.assertEqual(self.calc.power(0, 0), 1)
        self.assertEqual(self.calc.power(0, 5), 0)

    def test_power_large_exponent(self):
        self.assertEqual(self.calc.power(2, 20), 1048576)

if __name__ == '__main__':
    unittest.main()
