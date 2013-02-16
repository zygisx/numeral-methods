#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from random import randrange
from sys import argv
import time


from matrix import TridiagonalMatrix, Line


def time_function(func, *args, **kwargs):
	start = time.time()
	ret_val = func(*args, **kwargs)
	end = time.time()
	return (end-start), ret_val

def tridiagonal_to_full_matrix_string(initial_matrix):
	""" Returns string of full matrix. Useful for checking result in matrix calculators
	"""
	index = 0
	n = len(initial_matrix)
	matrix = ""
	for line in initial_matrix[:-1]:
		l = [0 for i in range(n+1)]
		l[index - 1] = line.a
		l[index]     = line.b
		l[index + 1] = line.c
		l[-1]        = line.res
		matrix += " ".join("%.1f" % x for x in l)
		matrix += "\n" 

		index += 1
	# last matrix line
	l = [0 for i in range(n+1)]
	l[-3] = initial_matrix[-1].a
	l[-2] = initial_matrix[-1].b
	l[-1] = initial_matrix[-1].res
	matrix += " ".join("%.1f" % x for x in l)

	return matrix

def tridiagonal_to_compact_matrix_string(initial_matrix):
	""" Returns string of compact matrix. Matrix size will be n*4
	"""
	index = 0
	matrix = "%.1f %.1f %.1f\t\t%.1f\n" % (0, initial_matrix[0].b, initial_matrix[0].c, initial_matrix[0].res)
	for line in initial_matrix[1:-1]:
		matrix += "%.1f %.1f %.1f\t\t%.1f\n" % (line.a, line.b, line.c, line.res)
	matrix += "%.1f %.1f %.1f\t\t%.1f\n" % (initial_matrix[-1].a, initial_matrix[-1].b, 0, initial_matrix[-1].res)
	return matrix

def random_tridiagonal_matrix(n=3):
	""" Returns random tridiagobal matrix as TridiagonalMatrix object
	"""
	valid = False
	compare = lambda line: abs(line.b) >= abs(line.a) + abs(line.c)
	strict_compare = lambda line: abs(line.b) > abs(line.a) + abs(line.c)
	isValid = compare
	matrix = TridiagonalMatrix()
	startTime = time.time()
	for _ in xrange(n):
		valid = False
		while not valid:
			line = Line([float(randrange(1,50)) for x in xrange(4)])
			if isValid(line):
				matrix.append_line(line)
				valid = True
			if time.time() - startTime > 240:
				return None

		isValid = compare
	return matrix

def silly_tridiagonal_martix(n=3):
	""" Returns silly tridiagonal matrix. Useful when need very large matrix very fast
	"""
	matrix = TridiagonalMatrix()
	for _ in xrange(n):
		a = randrange(1, 200)
		res = randrange(1, 500)
		line = Line([a, 3*a+1, 2*a, res])
		matrix.append_line(line)
	return matrix


DEFAULT_MATRIX_SIZE = 50

if __name__ == '__main__':
	n = int(argv[1]) if len(argv) > 1 else DEFAULT_MATRIX_SIZE
	print "Random %dx%d matrix:" % (n, n)
	rand_matrix = random_tridiagonal_matrix(n)
	# rand_matrix = silly_tridiagonal_martix(n)
	if rand_matrix:
		print tridiagonal_to_full_matrix_string(rand_matrix)
		print 
		print tridiagonal_to_compact_matrix_string(rand_matrix)
		time, res = time_function(rand_matrix.solve)
		print 
		print res
		print "Time to solve:", time
	else:
		print "Too less time."