from utilities import MatrixUtils, MAXIMUM_ITERATIONS
import numpy
import math
import scipy


class ConjugateGradient(object):


    def __init__(self, A, B, X, precision):
        self.A = A
        self.B = B
        self.X = X
        self.precision  = precision
        self.iterations = []

    def solve(self):
        """ Preconditions: matrix is symetrix and positive.
        """
        if not MatrixUtils.is_symetric(self.A):
            raise Exception("Matrix not symertic")
        if not MatrixUtils.is_positive(self.A):
            raise Exception("Matrix not positive definite")
        iterations = 0

        vector_length = len(self.B)
        z_vect = self.A * self.X - self.B
        p_vect = z_vect.copy()
        precision_need = self.precision ** 2
        precision = self.scalar_mul(z_vect, z_vect)

        while precision_need < precision and iterations < MAXIMUM_ITERATIONS:
            r_vect = self.A * p_vect

            tetra = self.scalar_mul(z_vect, p_vect) / self.scalar_mul(r_vect, p_vect)
            
            self.X = self.X - p_vect * tetra

            z_vect = z_vect - r_vect * tetra

            got_precision = self.scalar_mul(z_vect, z_vect)

            beta = got_precision / precision

            p_vect = z_vect + beta * p_vect

            precision = got_precision

            iterations += 1
            iter_str = " ".join("%.3f " % self.X[i,0] for i in  range(len(self.X)))
            self.iterations.append("%d.  %s %.12f" % (iterations, iter_str, precision))


        return self.X, iterations

    def scalar_mul(self, vect_a, vect_b):
        sum = 0.0
        for i in xrange(len(vect_a)):
            sum += vect_a[i,0] * vect_b[i,0]
        return sum

