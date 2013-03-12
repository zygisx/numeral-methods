#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import unittest
import math
import StringIO
from relaxation import RelaxationMethod
from secant import SecantMethod

class RelaxationTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_calculation(self):
        func = lambda x: math.exp(-x ** 2)

        relaxation = RelaxationMethod(func, log_device=StringIO.StringIO())
        result = relaxation.calculate(0.000001)
        self.assertAlmostEqual(result, 0.652919, 6)


class SecantTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_calculation(self):
        func = lambda x: math.exp(-x ** 2) - x

        secant = SecantMethod(func, log_device=StringIO.StringIO())
        result = secant.calculate(0.0, 2.0, 0.0000001)
        self.assertAlmostEqual(result, 0.652919, 6)