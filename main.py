#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from spline import Spline
from matrix_parser import TridiagonalMatrixParser

import math
from multiprocessing import Process

MENU = \
"""
1 - Spline draw
2 - Draw spline from binary number
3 - Matrix test

0 - Quit
"""

# Functions
# FUNCTION = lambda x: 0.5 * x**2 + 8 + 8.0 / x  # 15
# FUNCTION = lambda x: math.pow(math.e, -0.5*x) * math.cos(x)   # 5
# FUNCTION = lambda x: x**3 - 5*x**2 + 3*x + 4
# FUNCTION = lambda x: x**2

FUNCTION = lambda x : math.sqrt(x) - math.cos(1.5*x) # 12

### Binary task
BINARY_NUMBER = "001100"
BINAZY_TAKS_FUNCTION = lambda x: 209 if BINARY_NUMBER[x] == "1" else 0

RANGE_SPLITS = 1000

def get_int_input(message=""):
	try:
		return int(raw_input(message))
	except ValueError:
		print "Not a number. Please enter number."
		return get_int_input()

def get_float_or_empty_input(message=""):
	try:
		input = float(raw_input(message))
		return input
	except ValueError:
		return ""
	

def main():
	print MENU
	choose = get_int_input()

	while choose:
		if choose == 1:
			range_start = get_int_input("Enter range start: ")
			range_end = get_int_input("Enter range end: ")

			spline = Spline(range_start, range_end, RANGE_SPLITS, FUNCTION)
			
			print "Maple functions:"
			print "s := spline(%s, %s, x, cubic)" % (str(spline.x), str(spline.x))
			print "plot(s, x=%d..%d, thickness = 2)" % (range_start, range_end)
			print
			print "POINTS:"
			print "X: "
			print spline.x
			print "Y: "
			print spline.y
			print
			print "Coefficients:"
			print spline.n
			for i in xrange(spline.n-1):
				print "e[%(i)d]= %(e).5f \tG[%(i)d]= %(G).5f \tH[%(i)d]= %(H).5f" % {
					"i" : i,
					"e" : spline.E(i),
					"G" : spline.G(i),
					"H" : spline.H(i),
				}
			print 	

			file_name = raw_input("Enter file name for plot image [enter to show on screen]: ")
			if file_name:
				try:
					spline.plot_to_file(file_name)
				except IOError:
					print "File or directory don't exist."
			else:
				spline.plot_on_screen()

			point = get_float_or_empty_input("Enter x value: ")
			while isinstance(point, float):
				if point in spline.ranges:
					print "X: %.3f, Y: %.3f" % (point, spline.f(point))
				else:
					print "Number %.3f not in range. Enter number again." % point
				point = get_float_or_empty_input("Enter x value: ")

		elif choose == 2:
			pass
		elif choose == 3:
			file_name = raw_input("Enter file name for matrix [data/1.matrix by default]: ") or "data/1.matrix"
			parser = TridiagonalMatrixParser()

			matrix = parser.parse_from_tridiagonal_matrix(file_name)

			if matrix.validate():
				for i, res in enumerate(matrix.solve()):
					print "X%d= %f" % (i+1, res)
			else:
				print "Not valid matrix."

		print MENU
		choose = int(raw_input())

if __name__ == '__main__':
	main()