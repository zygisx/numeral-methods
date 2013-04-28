from data import *
from relaxation import Relaxation

from numpy import matrix, linalg, zeros
PRECISION = 0.000001
TASK_NUMBER = 12


def main():
    
    B = matrix(MATRIX_B)
    C = matrix(MATRIX_C)
    D = matrix(MATRIX_D)

    A = D + TASK_NUMBER * C


    ############ RELAXATION ################
    relaxation = Relaxation(A, B, zeros((4, 1)), PRECISION, omega=1.0)
    result = relaxation.solve()

    print "Result: ", result

    print "Real answer: "
    print linalg.solve(A, B)


    ####### Union Gradient Method ##########
    


if __name__ == '__main__':
    main()