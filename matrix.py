
#!/usr/local/bin/python
# -*- coding: utf-8 -*-

class Matrix(object):
	""" Class to hold all matrix data.
	"""
	def __init__(self):
		self.lines = []
		self.description = ""

	def append_line(self, line):
		self.lines.append(Line(line))

	def __getitem__(self, key):
		return self.lines[key]

	def __iter__(self):
		return self.lines.__iter__()

	def __len__(self):
		return len(self.lines)

class TridiagonalMatrix(Matrix):
	""" Class to hold tridiagonal matrix data 
	"""
	def __init__(self):
		Matrix.__init__(self)


	def validate(self):
		isStrictConditionSatisfied = False
		for line in self:
			isStrictConditionSatisfied = isStrictConditionSatisfied or line.b > line.a + line.c
			if line.b < line.a + line.c:
				return False
		return isStrictConditionSatisfied



class Line(object):
	""" Class describe line in matrix. 
		For interacting with matrix lines like high level objects.
	"""
	def __init__(self, values=list()):
		# print values
		# assert isinstance(values, list)
		self.line = values

	def __getitem__(self, key):
		return self.line[key]
	
	@property
	def res(self):
		return self[-1]

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

	def __repr__(self):
		return str(self.line)