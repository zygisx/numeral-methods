from matrix import TridiagonalMatrix
import time

def solve_tridiagonal_matrix(matrix):
	assert isinstance(matrix, TridiagonalMatrix)
	C = []; D = []
	C.append( -matrix[0].c / matrix[0].b )
	D.append( matrix[0].res / matrix[0].b )

	# loop handle all elements except first and last
	for line in matrix[1:]:
		C.append( -line.c / (line.a*C[-1] + line.b) )
		D.append( (line.res - line.a*D[-1]) / (line.a*C[-2] + line.b ))

	# fill result list with zeros
	result = [0 for _ in xrange(len(matrix))]
	result[-1] = D[-1]
	for i in xrange(len(matrix)-2, -1, -1):
		result[i] = C[i]*result[i+1] + D[i]
	return result

def time_function(func, *args, **kwargs):
	start = time.Clock()
	ret_val = func(*args, **kwargs)
	end = time.Clock()
	return (start-end), ret_val


MATRIX = [
[0,    2, 0.5,   3],
[0.5,  2, 0.5,   6],
[0.5,  2, 0.5,   9],
[0  ,0.5,   2, 9.5],
]
MATRIX2 = [
	[0., 2., -1.,  1.],
	[-1., 2., -1., 0.],
	[-1., 2., 0.,  1.],
]
MATRIX3  = [
	[0.0, -2.16, 1.075,  -0.836],
	[0.889, -2.16, 1.111, 0.198],
	[0.834, -2.16, 1.166, 0.441],
	[0.752, -2.16, 0.0,  -8.238]
]

matrix = TridiagonalMatrix()
for line in MATRIX3:
	matrix.append_line(line)

# for i in matrix:
	# print i.res
print [x for x in solve_tridiagonal_matrix(matrix)]