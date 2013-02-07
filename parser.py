from matrix import TridiagonalMatrix, Matrix, Line

COMMENT_SYMBOL = "#"

class MatrixParser(Parser):

	def __init__(self):
		pass

	def read_file(self, filename):
		""" Reads matrix data from matrix data file.
		"""
		with open(filename) as f:
			matrixes = []
			line_number = 0 
			matrix = Matrix()
			for line in f:
				line, _, doc = line.line.partition(COMMENT_SYMBOL)
				line = line.rstrip()
				if line:
					#Handel matrix
					#TODO: add to matrix numbers
				else:
					line_number = 0
					#TODO: append documentaion to matrix

	def __string_to_numbers_line(self, string):
		return [float(x) for x in string.split()]
