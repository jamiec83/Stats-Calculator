from Calculator.Calculator import Calculator
from Statistics.Mean import mean
from Statistics.MeanDev import mean_dev
from Statistics.Median import median
from Statistics.Mode import mode
from Statistics.PopCor import pop_correlation
from Statistics.Quartiles import quarts
from Statistics.SampleCor import sample_cor
from Statistics.Std_Deviation import sdeviation
from Statistics.Variance import variance
from Statistics.ZScore import ZScore
from CsvReader.CsvReader import CsvReader



class Statistics(Calculator):
    data = []

    def __init__(self):
        super().__init__()

    def median (self,data):
        self.result = median(data)
        return self.result

    def mode(self,data):
        self.result = mode(data)
        return self.result

    def mean(self,data):
        self.result = mean(data)
        return self.result

    def sdeviation(self,data):
        self.result = sdeviation(data)
        return self.result

    def variance(self,data):
        self.result = variance(data)
        return self.result

    def ZScore(self,data):
        self.result = zscore(data)
        return self.result

    def pop_correlation(self,data):
        self.result = pop_correlation(data)
        return self.result
