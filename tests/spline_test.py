#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import unittest

from spline import Ranges, Spline

class RangesTest(unittest.TestCase):

	def setUp(self):
		pass

	def test_points_finder(self):
		_range = Ranges(-3, 5, 4)

		self.assertEqual(len(_range.points), 5)
		self.assertEqual(_range.points[0], -3)
		self.assertEqual(_range.points[1], -1)
		self.assertEqual(_range.points[2],  1)
		self.assertEqual(_range.points[3],  3)
		self.assertEqual(_range.points[4],  5)

	def test_index_find(self):
		_range = Ranges(0, 10, 3)

		self.assertEqual(_range.find_index(0), 0)
		self.assertEqual(_range.find_index(2), 0)
		self.assertEqual(_range.find_index(3.0), 0)
		self.assertEqual(_range.find_index(6), 1)
		self.assertEqual(_range.find_index(9), 2)
		self.assertEqual(_range.find_index(10), 2)

class SplineExample1CalculationTest(unittest.TestCase):

	def setUp(self):
		def function(x):
			return x if x % 2 == 0 else x / 2
		self.spline = Spline(0, 3, 3, function)

	def test_h_values(self):


		self.assertEqual(len(self.spline.h), 3)
		self.assertEqual(self.spline.h[0], 1.0) 
		self.assertEqual(self.spline.h[1], 1.0) 
		self.assertEqual(self.spline.h[2], 1.0) 

	def test_g_values(self):


		self.assertEqual(len(self.spline.g), 4)
		self.assertEqual(self.spline.g[0], 0.0) 
		self.assertEqual(self.spline.g[1], 2.4) 
		self.assertEqual(self.spline.g[2], -3.6)
		self.assertEqual(self.spline.g[3], 0.0) 

	def test_e_values(self):


		self.assertAlmostEqual(self.spline.E(0), 0.1)
		self.assertAlmostEqual(self.spline.E(1), 1.3)
		self.assertAlmostEqual(self.spline.E(2), 0.7) 

	def test_G_values(self):


		self.assertAlmostEqual(self.spline.G(0), 0.0)
		self.assertAlmostEqual(self.spline.G(1), 1.2)
		self.assertAlmostEqual(self.spline.G(2), -1.8) 

	def test_H_values(self):


		self.assertAlmostEqual(self.spline.H(0), 0.4)
		self.assertAlmostEqual(self.spline.H(1), -1.0)
		self.assertAlmostEqual(self.spline.H(2), 0.6) 

	def test_spline_y_value(self):


		self.assertAlmostEqual(self.spline.f(0), 0.0)
		self.assertAlmostEqual(self.spline.f(0.25), 0.03125)
		self.assertAlmostEqual(self.spline.f(0.5), 0.1)
		self.assertAlmostEqual(self.spline.f(0.99), 0.4871196)
		self.assertAlmostEqual(self.spline.f(1.01), 0.513119)
		self.assertAlmostEqual(self.spline.f(1.5), 1.325)
		self.assertAlmostEqual(self.spline.f(1.8), 1.796)
		self.assertAlmostEqual(self.spline.f(2), 2)
		self.assertAlmostEqual(self.spline.f(2.01), 2.0068206)
		self.assertAlmostEqual(self.spline.f(2.5), 1.975)
		self.assertAlmostEqual(self.spline.f(2.99), 1.51099939)
		self.assertAlmostEqual(self.spline.f(3.0), 1.5)

