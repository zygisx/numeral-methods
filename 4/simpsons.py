

class Simpsons(object):

    def __init__(self, function, n, low, high):
        self.function = function
        self.n = n
        self.low = low
        self.high = high

    def integrete(self):
        assert self.low < self.high
        assert self.n > 0
        assert type(function) is callable

        result = 0.0
        h = (self.high - self.low)*1.0 / self.n
        

