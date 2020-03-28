from Calculator.Calculator import Calculator
from Statistics.Mean import mean
from Statistics.Median import median
from Statistics.Mode import mode
from Statistics.PopCor import correlation
from Statistics.Std_Deviation import sd
from Statistics.Variance import variance
from Statistics.Quartiles import quartiles
from Statistics.MeanDev import meandev
from Statistics.ZScore import ZScore
from Statistics.Skewness import skewness
from Statistics.pvalue import pvalue


class Statistics(Calculator):
    data = []

    def __init__(self):
        super().__init__()

    def median(self, data):
        self.result = median(data)
        return self.result

    def mode(self, data):
        self.result = mode(data)
        return self.result

    def mean(self, data):
        self.result = mean(data)
        return self.result

    def sd(self, data):
        self.result = sd(data)
        return self.result

    def variance(self, data):
        self.result = variance(data)
        return self.result

    def ZScore(self, data):
        self.result = ZScore(data)
        return self.result

    def correlation(self, data, data1):
        self.result = correlation(data, data1)
        return self.result

    def quartiles(self, data):
        self.result = quartiles(data)
        return self.result

    def meandev(self, data):
        self.result = meandev(data)
        return self.result

    def skewness(self, data):
        self.result = skewness(data)
        return self.result

    def pvalue(self, data):
        self.result = pvalue(data)
        return self.result

