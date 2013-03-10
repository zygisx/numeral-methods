#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from matrix import TridiagonalMatrix, Matrix, Line

COMMENT_SYMBOL = "#"


class TridiagonalMatrixParser(object):

    def __init__(self):
        pass

    def parse_from_tridiagonal_matrix(self, file):
        if isinstance(file, str):
            file = open(file, "r")

        matrix = TridiagonalMatrix()
        for line in file:
            line, _, doc = line.partition(COMMENT_SYMBOL)
            line = line.rstrip()
            if line:
                matrix.append_line([float(x) for x in line.split()])
            elif doc:
                matrix.description += doc
        file.close()
        return matrix

    def parse_from_full_matrix(self, file):
        if isinstance(file, str):
            file = open(file, "r")

        matrix = TridiagonalMatrix()
        line_num = 0
        for line in file:
            line, _, doc = line.partition(COMMENT_SYMBOL)
            line = line.rstrip()
            if line:
                vals = [float(x) for x in line.split()]
                matrix.append_line([vals[line_num - 1], vals[
                                   line_num], vals[line_num + 1], vals[-1]])
                line_num += 1
            elif doc:
                matrix.description += doc
        file.close()
        if len(matrix) > 0:
            matrix[0][0] = 0.0
            matrix[-1][2] = 0.0
        return matrix
