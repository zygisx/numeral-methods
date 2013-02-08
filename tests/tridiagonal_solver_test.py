
import unittest
from solver import solve_tridiagonal_matrix
from matrix import TridiagonalMatrix

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



