from utilities import MatrixUtils, MAXIMUM_INVERESE_METHOD_ITERATIONS
from numpy import matrix, linalg, zeros
from copy import copy
from math import sqrt

class InverseIterations(object):

    def __init__(self, A, X, lambd, precision):
        self.A = A
        self.X = X
        self.lambd = lambd
        self.precision = precision
        self.iterations = []

    def solve(self):
        precision = 1e6
        iterations = 0
        initial = self.create_initial_matrix(self.A)

        while precision > self.precision and iterations < MAXIMUM_INVERESE_METHOD_ITERATIONS:
            y_vect = linalg.solve(self.A + initial*self.lambd*(-1), self.X)
            x_vect = y_vect / self.vector_power_normalization(y_vect)

            lambda1 = self.multiply_vect(self.A * x_vect, x_vect)
            
            if self.multiply_vect(self.X, x_vect) < 0:
                self.X = x_vect

            if abs(lambda1 - self.lambd) >= 1.9:
               x_vect = x_vect * (-1)
            
            precision = self.vector_normalize(x_vect - self.X)
            

            iter_str = " ".join("%.3f " % x_vect[i,0] for i in  range(len(x_vect)))
            self.iterations.append("[ %s ] %.6f %.6f" % (iter_str, lambda1, precision))
            if precision < abs(self.lambd - lambda1):
                precision = abs(self.lambd - lambda1)

            # if precision nearly 2 than vector change vector direction


            self.lambd = lambda1
            self.X = x_vect

            iterations += 1

        return self.X, lambda1, iterations



    def create_initial_matrix(self, mat):
        ret_mat = copy(mat)   
        ret_mat.fill(0)

        for i in xrange(len(ret_mat)):
            ret_mat[i,i] = 1.0
        return ret_mat

    def vector_normalize(self, vect):
        result = 0.0
        for i in xrange(len(vect)):
            if abs(vect[i,0]) > result:
                result = abs(vect[i,0])
        return result

    def vector_power_normalization(self, vect):
        sum = 0.0
        for i in xrange(len(vect)):
            sum += pow(vect[i,0], 2)
        return sqrt(sum)

    def multiply_vect(self, a, b):
        sum = 0.0
        for i in xrange(len(a)):
            sum += a[i,0] * b[i,0]
        return sum


# from data import *

# # c = matrix(MATRIX_C)

# A = matrix(MATRIX_TEST)
# evals, evecs = linalg.eig(A)
# print "Real eigen values:"
# print evals 
# print "Real normalized eigen vector"
# print "[", " ".join(str(evecs[i,0]) for i in  range(len(evecs))), "]"

# inverse = InverseIterations(A, matrix('1.0; 0.0; 0.0; 0.0'), 4.0, 0.00001)
# eigenvector, eigenvalue, iterations = inverse.solve()
# if iterations < MAXIMUM_INVERESE_METHOD_ITERATIONS:
#     print "Solved in %d iterations" % iterations
# for it in inverse.iterations:
#     print it
# print "Eigen vector:"
# print " ".join("%.8f " % eigenvector[i,0] for i in  range(len(eigenvector)))
# print "Eigen value %.8f" % eigenvalue
