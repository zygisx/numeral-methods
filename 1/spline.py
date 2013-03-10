#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from matrix import TridiagonalMatrix
import math
import bisect
import numpy as np
import matplotlib.pyplot as plt

TICKNESS = 0.01  # describe plot


class Spline(object):

    def __init__(self, range_start, range_end, range_splits, function):
        self.ranges = Ranges(range_start, range_end, range_splits)
        self.function = function
        self.x = self.ranges.points
        self.y = [self.function(x) for x in self.x]
        self.h = []
        self.g = []

        self.n = len(self.x)

        self.find_h()
        self.find_g()

    def get_y(self, x):
        """	"""
        # find range index.
        i = self.ranges.find_index(x)
        return self.y[i] + self.E(i) * (x - self.x[i]) + self.G(i) * (x - self.x[i]) ** 2 + self.H(i) * (x - self.x[i]) ** 3

    f = get_y  # for readability: f(x) return y value at point x

    def find_h(self):
        for i in xrange(1, self.n):
            self.h.append(self.x[i] - self.x[i - 1])

    def find_g(self):
        matrix = TridiagonalMatrix()

        matrix.append_line([0, 1, 0, 0])
        for i in xrange(1, self.n - 1):
            matrix.append_line(
                [self.h[i - 1], 2 * (self.h[i - 1] + self.h[i]), self.h[i], 6 * ((
                                                                                 self.y[i + 1] - self.y[i]) / self.h[i] - (self.y[i] - self.y[i - 1]) / self.h[i - 1])]
            )
        matrix.append_line([0, 1, 0, 0])
        self.g = matrix.solve()
        self.g[0] = 0
        self.g[-1] = 0

    def draw(self):
        t = np.arange(self.ranges.start, self.ranges.end, TICKNESS)
        plt.plot(t, map(self.function, t), t, map(self.f, t))
        # plt.plot(t, map(self.f, t)) # to draw single plot

    def plot_to_file(self, filename):
        self.draw()
        plt.savefig(filename)

    def plot_on_screen(self):
        self.draw()
        plt.show()

    G = lambda self, i: self.g[i] / 2.0
    H = lambda self, i: (self.g[i + 1] - self.g[i]) / (6 * self.h[i])
    E = lambda self, i: (self.y[i + 1] - self.y[i]) / self.h[i] - self.g[
        i + 1] * self.h[i] / 6.0 - self.g[i] * self.h[i] / 3.0


class Ranges(object):
    def __init__(self, start, end, splits=10):
        self.start = float(start)
        self.end = float(end)
        self.splits = splits
        self.get_points()

    def get_points(self):
        step = (self.end - self.start) / self.splits

        self.points = []
        self.points.append(self.start)
        for i in xrange(self.splits):
            self.points.append(self.points[-1] + step)

    def find_index(self, number):
        """ Returns index of subrange in whom number fall in.
                Method return int value in range [0, self.splits-1].
        """
        return min(bisect.bisect(self.points, number) - 1, self.splits - 1)

    def __contains__(self, number):
        return self.start <= number <= self.end
