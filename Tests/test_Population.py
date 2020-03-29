import unittest
from PopulationSampling.cochran import Cochrans
from PopulationSampling.confidenceinterval import ConfInt
from PopulationSampling.knownpopulation import ssk
from PopulationSampling.marginoferror import marginerror
from PopulationSampling.unknownpopulationsd import ssu
from PopulationSampling.systematic import sys_sample
from PopulationSampling.simplerandom import ran_sample
from Statistics.statistics import Statistics
from pprint import pprint

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.statistics = Statistics()

    def test_results_property_calculator(self):
        self.assertEqual(self.statistics.result, 0)

    def test_cochran_statistics(self):
        pprint("Cochrans: Ok")
        print(Cochrans(set))

    def test_conf_statistics(self):
        pprint("Confidence Interval: Ok")
        print(ConfInt(set))

    def test_kpop_statistics(self):
        pprint("Known Population: Ok")
        print(ssk(set))

    def test_margin_statistics(self):
        pprint("Margin Of Error: Ok")
        print(marginerror(set))

    def test_upop_statistics(self):
        pprint("Unknown Population: Ok")
        print(ssu(set))

    def test_systematic_statistics(self):
        pprint("Systematic Sampling: Ok")
        print(sys_sample(set))

    def test_simplerandom_statistics(self):
        pprint("Simple Random Sampling: Ok")
        print(ran_sample(set))

if __name__ == '__main__':
    unittest.main()
