#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from utilities import MAX_FLOAT


class RelaxationMethod(object):
    """ Relaxation method solver
    """

    def __init__(self, func, derivative_func, omega=1.0):
        self.function = func
        self.derivative_func = derivative_func
        self.omega = omega

    def calculate(self, precision):
        n = 0
        x = 0.0
        x_new = self.function(x)
        current_precision = MAX_FLOAT

        while (current_precision > precision):
            omega = self.omega
            x_new = (1 - omega) * x + omega * self.function(x)

            print "%.10f, %.30f" % (x_new, x_new - x)

            current_precision = abs(x_new - x)
            x = x_new


        self.result = x  # save result
        return self.result

    def find_omega(self):
        M = -self.derivative_func(self.result - 0.001)
        m = -self.derivative_func(self.result + 0.001)

        self.omega = 2.0 / (2 + M + m)
        return self.omega
