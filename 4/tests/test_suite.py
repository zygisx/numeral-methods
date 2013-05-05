#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import unittest


class Task_4_TestSuite(unittest.TestSuite):

    def add(self, test_case):
        tests = unittest.defaultTestLoader.loadTestsFromTestCase(test_case)
        self.addTests(tests)

    def suite(self):
        # TODO: add more test cases here

        return self
