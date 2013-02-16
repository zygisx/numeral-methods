#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import unittest
import StringIO

from matrix import TridiagonalMatrix
from matrix_parser import TridiagonalMatrixParser


class ParserTest(unittest.TestCase):
	""" class to test parser module
	"""

	def setUp(self):
		self.parser = TridiagonalMatrixParser()

	def test_doc_parse(self):
		file_obj = StringIO.StringIO()

		#tridiagonal parse
		matrix = self.parser.parse_from_tridiagonal_matrix(file_obj)
		self.assertEqual(len(matrix), 0)
		self.assertEqual(matrix.description, "")

		file_obj = StringIO.StringIO()

		# from full matrix
		matrix = self.parser.parse_from_full_matrix(file_obj)
		self.assertEqual(len(matrix), 0)
		self.assertEqual(matrix.description, "")


	def test_doc_parse_tridiagonal(self):
		file_obj = StringIO.StringIO()
		file_obj.write("#First line.\n")
		file_obj.write("#Second line.\n")
		file_obj.seek(0)

		#tridiagonal parse
		matrix = self.parser.parse_from_tridiagonal_matrix(file_obj)
		self.assertEqual(len(matrix), 0)
		self.assertEqual(matrix.description, "First line.\nSecond line.\n")

	def test_doc_parse_full_matrix(self):
		file_obj = StringIO.StringIO()
		file_obj.write("#First line.\n")
		file_obj.write("#Second line.\n")
		file_obj.seek(0)

		# from full matrix
		matrix = self.parser.parse_from_full_matrix(file_obj)
		self.assertEqual(len(matrix), 0)
		self.assertEqual(matrix.description, "First line.\nSecond line.\n")

	def test_tridiagonal_matrix_parse(self):
		file_obj = StringIO.StringIO()
		file_obj.write("0 1. 2.0 3.0\n")
		file_obj.write("4.0 5. 6. 7.\n")
		file_obj.write("8. 9. 10. 11\n")
		file_obj.write("12 13. 0.0 15.0\n")
		file_obj.seek(0)

		#tridiagonal parse
		matrix = self.parser.parse_from_tridiagonal_matrix(file_obj)

		self.assertEqual(matrix[0].line, [0., 1., 2., 3.])
		self.assertEqual(matrix[1].line, [4, 5, 6, 7])
		self.assertEqual(matrix[2].line, [8, 9, 10, 11])
		self.assertEqual(matrix[3].line, [12, 13, 0, 15])
		self.assertEqual(matrix.description, "")



	def test_full_matrix_parse(self):
		file_obj = StringIO.StringIO()
		file_obj.write("1.  2.  0.  0.  3.0 \n")
		file_obj.write("4.0 5.  6.  0.  7.  \n")
		file_obj.write("0.  8.  9.  10. 11. \n")
		file_obj.write("0.  0.0 12. 13. 15.0\n")
		file_obj.seek(0)

		#tridiagonal parse
		matrix = self.parser.parse_from_full_matrix(file_obj)

		self.assertEqual(len(matrix), 4)
		self.assertEqual(matrix[0].line, [0, 1, 2, 3])
		self.assertEqual(matrix[1].line, [4, 5, 6, 7])
		self.assertEqual(matrix[2].line, [8, 9, 10, 11])
		self.assertEqual(matrix[3].line, [12, 13, 0, 15])
		self.assertEqual(matrix.description, "")





