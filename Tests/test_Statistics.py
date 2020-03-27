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
    p_answers = CsvReader('Tests/Data/Test_Proportion.csv').data
    z_answers = CsvReader('Tests/Data/Test_ZScores.csv').data
    column_proportion = [float(row['Proportion']) for row in p_answers]
    column_zscore = [float(row['Z-Score']) for row in z_answers]



    def setUp(self) -> None:
        self.statistics = Statistics()

    def test_results_property_calculator(self):
        self.assertEqual(self.statistics.result, 0)

    def test_mean_method_calculator(self):
        for row in self.test_answer:
            self.assertEqual(self.statistics.mean(self.column1), float(row['mean']))
            self.assertEqual(self.statistics.result, float(row['mean']))

    def test_median_method_calculator(self):
        for row in self.test_answer:
            pprint(row["median"])
        self.assertEqual(self.statistics.median(self.column1), float(row['median']))
        self.assertEqual(self.statistics.result, float(row['median']))


    def test_mode_method_calculator(self):
        for row in self.test_answer:
            self.assertEqual(self.statistics.mode(self.column1), float(row['mode']))
            self.assertEqual(self.statistics.result, float(row['mode']))

    def test_dev_method_calculator(self):
        for row in self.test_answer:
            self.assertEqual(self.statistics.sd(self.column1), float(row['dev']))
            self.assertEqual(self.statistics.result, float(row['dev']))

    def test_var_method_calculator(self):
        for row in self.test_answer:
            self.assertEqual(self.statistics.variance(self.column1), float(row['var']))
            self.assertEqual(self.statistics.result, float(row['var']))

    def test_cor_method_calculator(self):
        for row in self.test_answer:
            self.assertEqual(self.statistics.correlation(self.column1, self.column2), float(row['cor']))
            self.assertEqual(self.statistics.result, float(row['cor']))

    def test_zscore_statistics(self):
        self.assertEqual(self.statistics.ZScore(self.column1), self.column_zscore)
        self.assertEqual(self.statistics.result, self.column_zscore)

    def test_pvalue_statistics(self):
        self.assertEqual(self.statistics.p_value(self.column1), self.column_zscore)
        self.assertEqual(self.statistics.result, self.column_zscore)



if __name__ == '__main__':
    unittest.main()