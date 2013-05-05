

class Simpsons(object):

    def __init__(self, function, n, high, low):
        self.function = function
        self.n = n
        self.low = low
        self.high = high

        self.h = None

    def integrete(self):
        assert self.low < self.high
        assert self.n > 0

        result = 0.0
        self.h = (self.high - self.low)*1.0 / self.n
        
        x = []
        x.append(self.low)
        for _ in xrange(self.n):
            x.append(x[-1] + self.h)

        sum1 = sum(self.function(x[i]) for i in xrange(1, self.n, 2))
        # print sum1


        sum2 = sum(self.function(x[i]) for i in xrange(2, self.n, 2))
        # print sum2

        sn = (self.high - self.low)*1.0 / (self.n * 3.0) * (self.function(self.low) + 4*sum1 + 2*sum2 + self.function(self.high))
        return sn
