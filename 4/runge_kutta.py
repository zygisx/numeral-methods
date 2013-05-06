

class RungeKutta(object):

    def __init__(self, function, u0=0.0, start=0.0, end=1.0, ranges=2, sigma=0.5):
        self.function = function
        self.start = start
        self.end = end
        self.ranges = ranges
        self.u0 = u0
        self.sigma = sigma

        self.h = None

    _k1 = lambda self, x, y        : self.function(x, y)
    _k2 = lambda self, x, y, h, k1 : self.function(x + h, y + k1 * h)
    _y1 = lambda self, y, k1, k2, h: y + ((k1 + k2) / 2.0) * h

    def solve(self, output=False):
        if output:
            print "{0: <5} {1: <5} {2: <18} {3: <18} {4: <18}".format(
                "step", "x", "k1", "k2", "y")

        y = self.u0
        h = (self.end - self.start) * 1.0 / self.ranges
        x = self.start
        i = 0
        while i < self.ranges:
            k1 = self._k1(x, y)
            k2 = self._k2(x, y, h, k1)
            y  = self._y1(y, k1, k2, h)

            if output:
                print "{0: <5} {1: <5} {2: <18} {3: <18} {4: <18}".format(i, x, k1, k2, y)
            
            x += h
            i += 1 
        return y, h

