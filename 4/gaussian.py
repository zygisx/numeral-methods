from math import sqrt

class Consts(object):
    c1 = 5.0 / 9
    c2 = 8.0 / 9
    c3 = 5.0 / 9
    x1 = -1*sqrt(0.6)
    x2 = 0
    x3 = sqrt(0.6)

class Gaussian(object): 

    def __init__(self, function, high, low, n):
        self.function = function
        self.high = high
        self.low = low
        self.n = n

        self.h = None

    def integrate(self):
        self.h = (self.high - self.low) * 1.0 / self.n
        x = self.low
        result = 0.0
        while x < self.high:
            result += self.solve(x, x+self.h)
            x += self.h

        return result




    def solve(self, low, high):
        gs = lambda s : self.function(
            ((low + high) / 2.0) + 
            ((high - low) / 2.0)*s
        )
        dx = (high - low) / 2.0
        return dx * \
            (Consts.c1 * gs(Consts.x1) + \
            Consts.c2 * gs(Consts.x2) +  \
            Consts.c3 * gs(Consts.x3))




        