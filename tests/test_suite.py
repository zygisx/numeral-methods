#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import unittest
from tridiagonal_solver_test import KnownCasesTest

class Task_1_TestSuite(unittest.TestSuite):
	 
	def add(self, test_case):
		tests = unittest.defaultTestLoader.loadTestsFromTestCase(test_case)
		self.addTests(tests)

	def suite(self):
		self.add(KnownCasesTest)
		#TODO: add more test cases here

		return self