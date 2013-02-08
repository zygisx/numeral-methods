#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from matrix import TridiagonalMatrix, Matrix, Line

COMMENT_SYMBOL = "#"

class MatrixParser(object):

	def __init__(self):
		pass

	def read_file(self, filename):
		with open(filename) as f:
			matrix = Matrix()
			for line in f:
				line, _, doc = line.line.partition(COMMENT_SYMBOL)
				print line, doc
				line = line.rstrip()
				if line:
					matrix.append_line(
						[float(x) for x in line.split()]
					)
		return matrix

	def read_file(self, filename):
		with open(filename) as f:
			matrix = Matrix()
			for line in f:
				line, _, doc = line.line.partition(COMMENT_SYMBOL)
				print line, doc
				line = line.rstrip()
				if line:
					vals =  [float(x) for x in line.split()]
					[vals[line_num-1], vals[line_num], vals[line_num+1]
					matrix.append_line(
						[float(x) for x in line.split()]
					)
					line_num += 1
		return matrix


	# def read_file(self, filename):
	# 	""" Reads matrix data from matrix data file.
	# 	"""
	# 	with open(filename) as f:
	# 		matrixes = []
	# 		line_number = 0 
	# 		matrix = Matrix()
	# 		for line in f:
	# 			line, _, doc = line.line.partition(COMMENT_SYMBOL)
	# 			print line, doc
	# 			line = line.rstrip()
	# 			if line:
	# 				matrix.append_line(
	# 					[float(x) for x in line.split()]
	# 				)
	# 			else:
	# 				matrix.description = doc

	# 				line_number = 0
	# 				matrixes.append(matrix)

	# 				#TODO: append documentaion to matrix
	

	def read_matrix_line(self, line):
		return [float(x) for x in line.split()]
	def read_tridiagonal_matrix_line(self, line, line_num):
		vals =  [float(x) for x in line.split()]
		return [vals[line_num-1], vals[line_num], vals[line_num+1]
		
