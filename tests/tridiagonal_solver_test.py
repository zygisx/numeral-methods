
import unittest
from solver import solve_tridiagonal_matrix
from matrix import TridiagonalMatrix, Line

DEFAULT_ACCURACY = 7


class KnownCasesTest(unittest.TestCase):

	def setUp(self):
		pass

	def create_tridiagonal_matrix(self, matrix_array):
		matrix = TridiagonalMatrix()
		for line in matrix_array:
			matrix.append_line(line)
		return matrix

	def default_tridiagonal_solve_test(self, initial, expected, accuracy=DEFAULT_ACCURACY):
		matrix = self.create_tridiagonal_matrix(initial)
		# assert matrix.validate()
		result = solve_tridiagonal_matrix(matrix)
		print result
		self.assertEqual(len(result), len(expected), "Wrong length of array returned by solver function")
		for res, exp in zip(result, expected):
			self.assertAlmostEqual(res, exp, accuracy)

	def test_simple_matrix(self):
		INITIAL_MATRIX = [
			[0. , 2., -1.,  1.],
			[-1., 2., -1.,  0.],
			[-1., 2.,  0.,  1.],
		]
		EXPECTED_RESULT = [1, 1, 1]
		self.default_tridiagonal_solve_test(INITIAL_MATRIX, EXPECTED_RESULT)

	def test_4_x_4_matrix(self):
		INITIAL_MATRIX = [
			[  0.0, -2.16, 1.075,  -0.836],
			[0.889, -2.16, 1.111,  0.198],
			[0.834, -2.16, 1.166,   0.441],
			[0.752, -2.16,   0.0,  -8.238]
		]
		EXPECTED_RESULT = [ 1.51, 2.257, 3.357, 4.983]
		self.default_tridiagonal_solve_test(INITIAL_MATRIX, EXPECTED_RESULT, 2)

	def test_9_x_9_matrix(self):
		INITIAL_MATRIX = [
			[0.0, -3.0, -1.0, -5.0],
			[2.0, 5.0, -2.0, 5.0],
			[1.0, -5.0, 3.0, 2.0],
			[1.0, -3.0, 0.0, 0.0],
			[2.0, 4.0, 2.0, 3.0],
			[2.0, 3.0, 1.0, -4.0],
			[0.0, -3.0, -1.0, 1.0],
			[-2.0, 5.0, 3.0, 5.0],
			[-1.0, 5.0, -2.0, -4.0],
		]
		EXPECTED_RESULT = [
			 1.609,
			 0.174,
			-0.457,
			-0.152,
			 2.066,
			-2.480,
			-0.691,
			 1.074,
			-0.585,
		]
		self.default_tridiagonal_solve_test(INITIAL_MATRIX, EXPECTED_RESULT, 3)

	def test_12_x_12_matrix(self):
		INITIAL_MATRIX = [ 
			[0.0 , 27.0, 5.0 , 21.0],
			[1.0 , 41.0, 28.0, 38.0],
			[2.0 , 29.0, 10.0, 22.0],
			[17.0, 43.0, 18.0, 21.0],
			[19.0, 28.0, 2.0 , 46.0],
			[1.0 , 32.0, 15.0, 42.0],
			[1.0 , 26.0, 4.0 , 20.0],
			[8.0 , 38.0, 21.0, 48.0],
			[11.0, 41.0, 17.0, 16.0],
			[4.0 , 47.0, 22.0, 8.0],  
			[2.0 , 26.0, 9.0 , 1.0], 
			[11.0, 37.0, 0.0 , 3.0],
		]
		EXPECTED_RESULT = [
			 0.738479,
			 0.212214,
			 1.020027,
			-0.800521,
			 2.115663,
			 0.985661,
			 0.556212,
			 1.138208,
			 0.014209,
			 0.170420,
			-0.003026,
			 0.081981,
		]
		self.default_tridiagonal_solve_test(INITIAL_MATRIX, EXPECTED_RESULT, 6)

	def test_20_x_20_matrix(self):
		INITIAL_MATRIX = [ 
			[0.0 , 40.0, 8.0 , 49.0],
			[16.0, 42.0, 6.0 , 45.0],
			[1.0 , 17.0, 11.0, 31.0],
			[22.0, 28.0, 5.0 , 1.0 ], 
			[10.0, 36.0, 16.0, 28.0],
			[9.0 , 28.0, 4.0 , 1.0 ],
			[20.0, 49.0, 16.0, 42.0],
			[6.0 , 43.0, 24.0, 8.0 ],
			[2.0 , 46.0, 14.0, 46.0],
			[3.0 , 46.0, 29.0, 42.0],
			[20.0, 42.0, 11.0, 33.0],
			[11.0, 34.0, 19.0, 4.0 ],
			[8.0 , 18.0, 4.0 , 47.0],
			[11.0, 40.0, 26.0, 48.0],
			[12.0, 44.0, 28.0, 49.0],
			[14.0, 22.0, 2.0 , 9.0 ],
			[1.0 , 23.0, 3.0 , 40.0],
			[1.0 , 44.0, 38.0, 22.0],
			[19.0, 39.0, 5.0 , 30.0],
			[3.0 , 29.0, 0.0 , 29.0],
		]
		EXPECTED_RESULT = [
			 1.223075,
			 0.009626,
			 4.171087,
			-3.628918,
			 2.169160,
			-0.862536,
			 1.407145,
			-0.606211,
			 1.067675,
			-0.135759,
			 1.553168,
			-2.683445,
			 4.113278,
			-1.392860,
			 2.248782,
			-1.186861,
			 1.813992,
			-0.178315,
			 0.737681,
			 0.923688,
		]
		self.default_tridiagonal_solve_test(INITIAL_MATRIX, EXPECTED_RESULT, 3)







