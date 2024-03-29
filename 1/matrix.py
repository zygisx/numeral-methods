
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
            isStrictConditionSatisfied = isStrictConditionSatisfied or abs(
                line.b) > abs(line.a) + abs(line.c)
            if abs(line.b) < abs(line.a) + abs(line.c):
                return False
        return isStrictConditionSatisfied

    def solve(self):
        matrix = self  # for code readability
        C = []
        D = []
        C.append(-matrix[0].c / matrix[0].b)
        D.append(matrix[0].res / matrix[0].b)

        # loop handle all elements except first
        for line in matrix[1:]:
            denominator = line.a * C[-1] + line.b
            C.append(-line.c / denominator)
            D.append((line.res - line.a * D[-1]) / denominator)

        # fill result list with zeros
        result = [0 for _ in xrange(len(matrix))]
        result[-1] = D[-1]
        for i in xrange(len(matrix) - 2, -1, -1):  # loop from one before last to 0
            result[i] = C[i] * result[i + 1] + D[i]
        return result


class Line(object):
    """ Class describe line in matrix.
            For interacting with matrix lines like high level objects.
    """
    def __init__(self, values=list()):
        assert isinstance(values, list)
        self.line = values

    def __getitem__(self, key):
        return self.line[key]

    def __setitem__(self, key, value):
        self.line[key] = value

    @property
    def res(self):
        return self[-1]

    # Properties for simpler tridiagonal matrix access

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
