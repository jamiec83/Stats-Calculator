import unittest

from Calculator.Calculator import Calculator
from CsvReader.CsvReader import CsvReader
from pprint import pprint

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_add_method_calculator(self):
        self.assertEqual(self.calculator.add(1, 1), 2)
        self.assertEqual(self.calculator.result, 2)
        test_data = CsvReader('Tests/Data/Addition.csv').data
        pprint("Addition: OK")
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.add(row['Value 2'], row['Value 1']), result)
            self.assertEqual(self.calculator.result, result)

    def test_subtract_method_calculator(self):
        self.assertEqual(self.calculator.subtract(4, 4), 0)
        self.assertEqual(self.calculator.result, 0)
        test_data = CsvReader('Tests/Data/Subtraction.csv').data
        pprint("Subtraction: OK")
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.subtract(row['Value 2'], row['Value 1']), result)
            self.assertEqual(self.calculator.result, result)

    def test_multiply_method_calculator(self):
        self.assertEqual(self.calculator.multiply(3, 2), 6)
        self.assertEqual(self.calculator.result, 6)
        test_data = CsvReader('Tests/Data/Multiplication.csv').data
        pprint("Multiplication: OK")
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.multiply(row['Value 2'], row['Value 1']), result)
            self.assertEqual(self.calculator.result, result)

    def test_divide_method_calculator(self):
        self.assertEqual(self.calculator.divide(5, 5), 1)
        self.assertEqual(self.calculator.result, 1)
        test_data = CsvReader('Tests/Data/Division.csv').data
        pprint("Division: OK")
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.divide(row['Value 2'], row['Value 1']), result)
            self.assertEqual(self.calculator.result, result)

    def test_square_method_calculator(self):
        self.assertEqual(self.calculator.square(2), 4)
        self.assertEqual(self.calculator.result, 4)
        test_data = CsvReader('Tests/Data/Square.csv').data
        pprint("Square: OK")
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.square(row['Value 1']), result)
            self.assertEqual(self.calculator.result, result)

    def test_square_root_method_calculator(self):
        self.assertEqual(self.calculator.squareroot(4), 2)
        self.assertEqual(self.calculator.result, 2)
        test_data = CsvReader('Tests/Data/SquareRoot.csv').data
        pprint("Square Root: OK")
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.squareroot(row['Value 1']), result)
            self.assertEqual(self.calculator.result, result)




    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)


if __name__ == '__main__':
    unittest.main()