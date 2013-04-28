from utilities import MatrixUtils, MAXIMUM_ITERATIONS
import numpy

class Relaxation(object):

    def __init__(self, A, B, X, precision, omega=1.0):
        self.A = A
        self.B = B
        self.X = X
        self.omega = omega
        self.precision  = precision
        self.iterations = []

    def solve(self):
        """ Preconditions: matrix is symetrix and positive.
            Omega is in range (0, 2)
        """
        if not MatrixUtils.is_symetric(self.A):
            return
        # if not MatrixUtils.is_positive(self.A):
        #     return

        iterations = 0
        precision = 10000.0

        vector_length = len(self.X)
        result = numpy.copy(self.X)

        while precision > self.precision and iterations < MAXIMUM_ITERATIONS:
            for i in xrange(vector_length):
                sum = 0.0

                for j in xrange(i):
                    sum += self.A[i,j] * result[j,0]

                for j in xrange(i+1, vector_length):
                    sum += self.A[i,j] * self.X[j,0]

                result[i,0] = self.X[i,0] + self.omega * (((self.B[i,0] - sum) / self.A[i,i]) - self.X[i,0])

            self.X = result
            
            precision = self.current_precision()
            print iterations, precision
            # self.iterations.append({'vector':copy(self.X), 'precision':precision})
            iterations += 1
        
        return self.X

    def current_precision(self):
        precision = 0.0
        
        vect_prec = self.A * self.X - self.B
        
        for row in xrange(len(vect_prec)):
            if abs(vect_prec[row,0]) > precision:
                precision = abs(vect_prec[row,0])
        
        return precision


