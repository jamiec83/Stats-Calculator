import unittest
from pprint import pprint
from Calculator.Calculator import Calculator
from CsvReader.CsvReader import CsvReader
from Statistics.statistics import Statistics


class MyTestCase(unittest.TestCase):
    test_answer = CsvReader('Tests/Data/StatsAnswers.csv').data
    test_data = CsvReader('Tests/Data/test_data.csv').data
    column1 = [int(row['value1']) for row in test_data]
    column2 = [int(row['value2']) for row in test_data]

    def setUp(self) -> None:
        self.statistics = Statistics()

    def test_results_property_calculator(self):
        self.assertEqual(self.statistics.result, 0)

    def test_mean_method_calculator(self):
        for row in self.test_answer:
            self.assertEqual(self.statistics.mean(self.column1), float(row['mean']))
            self.assertEqual(self.statistics.result, float(row['mean']))

    def test_mode_method_calculator(self):
        for row in self.test_answer:
            self.assertEqual(self.statistics.mode(self.column1), float(row['mode']))
            self.assertEqual(self.statistics.result, float(row['mode']))