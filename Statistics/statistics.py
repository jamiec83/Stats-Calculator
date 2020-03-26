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
        
