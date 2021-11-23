from simple_calc import SimpleCalc
import unittest

class SimpleCalcTests(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalc()

    def test_add(self):
        actual = self.calc.add(2, 4)
        expected = 6
        self.assertEqual(expected, actual,
                         "Expected `add` to return 6.")

    def test_subtract(self):
        expected = 4
        actual = self.calc.subtract(10, 6)
        self.assertEqual(expected, actual)

    def test_multiply(self):
        self.assertEqual(25, self.calc.multiply(5, 5))

    def test_multiply_floats(self):
        self.assertAlmostEqual(7.85, self.calc.multiply(3.14, 2.50))

if __name__ == "__main__":
    unittest.main()