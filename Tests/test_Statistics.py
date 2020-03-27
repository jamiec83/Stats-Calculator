import unittest

from Calculator.Calculator import Calculator
from CsvReader.CsvReader import CsvReader
from Statistics.statistics import Statistics


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistics = Statistics()

    def test_results_property_calculator(self):
        self.assertEqual(self.statistics.result, 0)

    def test_mean_method_calculator(self):
        self.assertEqual(self.statistics.mean(4, 6), 5)
        self.assertEqual(self.statistics.result, 2)

