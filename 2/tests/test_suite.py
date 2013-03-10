#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import unittest
from solve_tests import RelaxationTest, SecantTest


class Task_2_TestSuite(unittest.TestSuite):

    def add(self, test_case):
        tests = unittest.defaultTestLoader.loadTestsFromTestCase(test_case)
        self.addTests(tests)

    def suite(self):
        self.add(RelaxationTest)
        self.add(SecantTest)
        # TODO: add more test cases here

        return self
