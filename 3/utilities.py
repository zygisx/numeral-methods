from numpy.ma.core import transpose
from numpy.linalg import cholesky, LinAlgError

MAXIMUM_ITERATIONS = 1000
MAXIMUM_INVERESE_METHOD_ITERATIONS = 1000
DEFAULT_PRECISION  = 0.000001

class MatrixUtils(object):
    """ Class for matrix utilities functions
    """

    @staticmethod
    def is_symetric(matrix):
        try:
            for i in range(len(matrix)):
                for j in range(i):
                    if matrix[i,j]  != matrix[j,i]:
                        return False
            return True
        except:
            print "Raised exception"
            raise Exception("Matrix not symertic")
        # tmp_matrix = transpose(matrix)
        # print tmp_matrix
        # print matrix
        # print "***"
        # return (tmp_matrix.all() == matrix.all())

    @staticmethod
    def is_positive(matrix):
        """ All main main minors are positive
        """
        try:
            cholesky(matrix)
            return True
        except LinAlgError:
            return False
        