#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import sys
from logger import Logger
from utilities import MAX_ITERATIONS

class SecantMethod(object):
    """ Secant method SecantSolver
    """

    def __init__(self, function, log_device=sys.stdout):
        self.function = function
        self.logger = Logger(log_device, "%d. %.15f %.15f %.15f\n")

    def calculate(self, x0, x1, precision):
        i = 0

        while abs(x1 - x0) > precision:
            x1_funkc = self.function(x1)
            
            x = x1 - x1_funkc * ((x1-x0) / (x1_funkc-self.function(x0))) 

            self.logger.log((i, x0, x1, x1_funkc))
            x0 = x1
            x1 = x
            
            i += 1
            if i > MAX_ITERATIONS:
                return None

        return x1



