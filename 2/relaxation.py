#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import sys
import StringIO

from utilities import MAX_FLOAT, MAX_ITERATIONS
from logger import Logger

class RelaxationMethod(object):
    """ Relaxation method solver
    """

    DEFAULT_PRECISION = 1e-6

    def __init__(self, func, derivative_func=None, omega=1.0, log_device=sys.stdout):
        self.function = func
        self.derivative_func = derivative_func
        self.omega = omega
        self.result = None
        self.logger = Logger(log_device, "%d. %.15f %.15f\n")

    def calculate(self, precision=DEFAULT_PRECISION):
        n = 0
        x = 0.0
        x_new = self.function(x)
        current_precision = MAX_FLOAT
        i = 0

        while (current_precision > precision):
            x_new = (1 - self.omega) * x + self.omega * self.function(x)

            i += 1
            self.logger.log((i, x_new, x_new - x))
            # print "%d %.10f, %.30f" % (i, x_new, x_new - x)

            current_precision = abs(x_new - x)
            x = x_new

            if i > MAX_ITERATIONS:
                return None

        self.result = x  # save result
        return self.result

    def find_omega(self, derivative_func=None):
        # if user specifies derivative function than update to that function
        self.logger.off()
        self.derivative_func = derivative_func or self.derivative_func
        if not self.derivative_func:
            return None
        if not self.result:
            self.result = self.calculate()
            if self.result is None:
                return None

        M = -self.derivative_func(self.result - 0.01)
        m = -self.derivative_func(self.result + 0.01)

        self.omega = 2.0 / (2 + M + m)
        self.logger.on()
        return self.omega
