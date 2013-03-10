#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import unittest
from tridiagonal_solver_test import KnownCasesTest
from spline_test import RangesTest, SplineExample1CalculationTest
from parser_test import ParserTest


class Task_1_TestSuite(unittest.TestSuite):

    def add(self, test_case):
        tests = unittest.defaultTestLoader.loadTestsFromTestCase(test_case)
        self.addTests(tests)

    def suite(self):
        self.add(KnownCasesTest)
        self.add(RangesTest)
        self.add(SplineExample1CalculationTest)
        self.add(ParserTest)

        return self
