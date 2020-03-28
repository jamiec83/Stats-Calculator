from Statistics.statistics import Statistics
from RandomNumber.randomnum import wseed
from RandomNumber.randomnum import woseed
from RandomNumber.randomnum import randomlist
from RandomNumber.randomnum import itemlist
from pprint import pprint
import unittest

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.statistics = Statistics()

    def test_results_property_calculator(self):
        self.assertEqual(self.statistics.result, 0)

    def test_wseed_statistics(self):
        pprint("Generate with Seed:Ok")
        print(wseed(set))

    def test_woseed_statistics(self):
        pprint("Generate without Seed:Ok")
        print(woseed(set))

    def test_listwseed_statistics(self):
        pprint("Generate with Seed list of numbers in a range:Ok")
        print(randomlist(set))

    def test_itemlist_statistics(self):
        pprint("Generate Item from List:Ok")
        print(itemlist(set))