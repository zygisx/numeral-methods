

class RungeKutta(object):

    def __init__(self, function, start, end, ranges, u0=0.0, sigma=0.5):
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

    def solve(self):
        x = self.start
        y = self.u0
        h = (self.end - self.start) * 0.1 / self.ranges
        i = 0
        while i < self.ranges:
            k1 = self._k1(x, y)
            k2 = self._k2(x, y, h, k1)
            y  = self._y1(y, k1, k2, h)

            x += h
            i += 1 
        return y, h

