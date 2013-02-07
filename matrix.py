

class Matrix(object):
	pass

class Line(object):

	def __init__(self):
		self.line = []



	def __getitem__(self, key):
		if 0 <= key < len(self.line):
			return self.line[key]
	 