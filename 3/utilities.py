from numpy.ma.core import transpose

MAXIMUM_ITERATIONS = 1000
DEFAULT_PRECISION  = 0.000001

class MatrixUtils(object):
    """ Class for matrix utilities functions
    """

    @staticmethod
    def is_symetric(matrix):
        tmp_matrix = transpose(matrix)
        return (tmp_matrix.all() == matrix.all())

    @staticmethod
    def is_positive(matrix):
        """ All main main minors are positive
        """
        pass
        