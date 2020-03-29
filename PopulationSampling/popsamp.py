from Calculator.Calculator import Calculator
from Statistics.statistics import Statistics
from PopulationSampling.cochran import Cochrans
from PopulationSampling.confidenceinterval import ConfInt
from PopulationSampling.knownpopulation import ssk
from PopulationSampling.marginoferror import marginerror
from PopulationSampling.unknownpopulationsd import ssu
from PopulationSampling.systematic import sys_sample
from PopulationSampling.simplerandom import ran_sample

class PopSamp(Calculator):
    data = []

    def __init__(self):
        super().__init__()

    def cochran(self, data):
        self.result = Cochrans(data)
        return self.result

    def conf(self, data):
        self.result = ConfInt(data)
        return self.result

    def kpop(self, data):
        self.result = ssk(data)
        return self.result

    def margin(self, data):
        self.result = marginerror(data)
        return self.result

    def upop(self, data):
        self.result = ssu(data)
        return self.result

    def systematic(self, data):
        self.result = sys_sample(data)
        return self.result

    def simpran(self, data):
        self.result = ran_sample(data)
        return self.result