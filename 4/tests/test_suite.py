#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import unittest
from integral_tests import SimpsonsTest, GaussianTest


class Task_4_TestSuite(unittest.TestSuite):

    def add(self, test_case):
        tests = unittest.defaultTestLoader.loadTestsFromTestCase(test_case)
        self.addTests(tests)

    def suite(self):
        self.add(SimpsonsTest)
        self.add(GaussianTest)

        return self
