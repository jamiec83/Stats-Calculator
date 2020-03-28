from RandomNumber.randomwseed import wseed
from RandomNumber.randwoseed import woseed
from RandomNumber.randomlistwseed import randomlist
from RandomNumber.randomItem import itemlist
from RandomNumber.randomItemwseed import itemlistwseed
from Calculator.Calculator import Calculator

class RandomNumber(Calculator):
    data = []

    def __init__(self):
        super().__init__()

    def wseed(self, data):
        self.result = wseed(data)
        return self.result

    def woseed(self, data):
        self.result = woseed(data)
        return self.result

    def list(self, data):
        self.result = randomlist(data)
        return self.result

    def itemlist(self, data):
        self.result = itemlist(data)
        return self.result

    def itemlistwseed(self, data):
        self.result = itemlistwseed(data)
        return self.result