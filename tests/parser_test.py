#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import unittest
import StringIO

from matrix import TridiagonalMatrix
from matrix_parser import MatrixParser


class TridiagonalParserTest(unittest.TestCase):
	""" class to test parser module
	"""

	def setUp(self):
		self.parser = MatrixParser()

	def test_empty_file(self):
		pass

	def test_only_comments_file_parse(self):
		pass

	def test_only_matrix_parse(self):
		pass

	def test_matrix_and_comments_parse(self):
		pass





