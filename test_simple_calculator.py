import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Initialize the calculator before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):  # Changed from test_add
        """Test addition method."""
        self.assertEqual(self.calc.addition(2, 3), 5)
        self.assertEqual(self.calc.addition(-1, -1), -2)
        self.assertEqual(self.calc.addition(0, 0), 0)
        self.assertEqual(self.calc.addition(-5, 5), 0)
        # Additional edge case
        self.assertEqual(self.calc.addition(2.5, 3.5), 6.0)

    def test_subtraction(self):  # Changed from test_subtract
        """Test subtraction method."""
        self.assertEqual(self.calc.subtraction(10, 5), 5)
        self.assertEqual(self.calc.subtraction(-1, -1), 0)
        self.assertEqual(self.calc.subtraction(0, 5), -5)
        self.assertEqual(self.calc.subtraction(5, 10), -5)

    def test_multiply(self):
        """Test multiplication method."""
        self.assertEqual(self.calc.multiplication(2, 3), 6)
        self.assertEqual(self.calc.multiplication(-2, 3), -6)
        self.assertEqual(self.calc.multiplication(0, 100), 0)
        self.assertEqual(self.calc.multiplication(2.5, 4), 10.0)

    def test_divide(self):
        """Test division method."""
        self.assertEqual(self.calc.division(10, 2), 5)
        self.assertEqual(self.calc.division(-10, 2), -5)
        self.assertEqual(self.calc.division(0, 5), 0)
        self.assertEqual(self.calc.division(5, 2), 2.5)

    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        with self.assertRaises(ValueError):
            self.calc.division(5, 0)
        with self.assertRaises(ValueError):
            self.calc.division(0, 0)

if __name__ == '__main__':
    unittest.main()