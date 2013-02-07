
class TridiagonalMatrix(Matrix):
	""" Class to hold tridiagonal matrix data 
	"""
	def __init__(self):
		Matrix.__init__(self)


class Matrix(object):
	""" Class to hold all matrix data.
	"""
	def __init__(self):
		self.lines = []
		self.description = ""

	def append_line(line):
		self.lines.append(Line())

	def __getitem__(self, key):
		return self.lines[key]

	def __iter__(self):
		return self.lines.__iter__()

	def __len__(self):
		return len(self.lines)





class Line(object):
	""" Class describe line in matrix. 
		For interacting with matrix lines like high level objects.
	"""
	def __init__(self, values=[]]):
		assert isinstance(values, list)
		self.line = values

	def __getitem__(self, key):
		return self.line[key]
	
	@property
	def res():
		return self.line[-1]

	#Properties for simpler tridiagonal matrix access

	@property
	def a(self):
		return self[0]
	@property
	def b(self):
		return self[1]
	@property
	def c(self):
		return self[2]