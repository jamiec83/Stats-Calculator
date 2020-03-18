import unittest

from Calculator.Calculator import Calculator
from CsvReader.CsvReader import CsvReader


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_add_method_calculator(self):
        self.assertEqual(self.calculator.add(1, 1), 2)
        self.assertEqual(self.calculator.result, 2)

    def test_subtract_method_calculator(self):
        self.assertEqual(self.calculator.subtract(4, 4), 0)
        self.assertEqual(self.calculator.result, 0)

    def test_multiply_method_calculator(self):
        self.assertEqual(self.calculator.multiply(3, 2), 6)
        self.assertEqual(self.calculator.result, 6)

    def test_divide_method_calculator(self):
        self.assertEqual(self.calculator.divide(5, 5), 1)
        self.assertEqual(self.calculator.result, 1)

    def test_square_method_calculator(self):
        self.assertEqual(self.calculator.square(2), 4)
        self.assertEqual(self.calculator.result, 4)

    def test_square_root_method_calculator(self):
        self.assertEqual(self.calculator.squareroot(4), 2)
        self.assertEqual(self.calculator.result, 2)

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)


if __name__ == '__main__':
    unittest.main()