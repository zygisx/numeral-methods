from data import *
from relaxation import Relaxation
from conjugate_gradients import ConjugateGradient
from inverse_iterations import InverseIterations
from reader import read_matrixes
from utilities import MAXIMUM_INVERESE_METHOD_ITERATIONS

from numpy import matrix, linalg, zeros

PRECISION = 0.000001

TASK_NUMBER = 12

COMPLEX_MODE = True

INVERSE_X_VECTOR = "1.0; 0.0; 0.0; 0.0"
INVERSE_PRECISION = 0.00001



MENU = \
    """
    1. Relaxation
    2. Union Gradient
    3. Inverse iterations
    """

def main():
    print MENU
    input = int(raw_input("Method: "))

    if input == 1 or input == 2:
        filename = raw_input("File name[data/task1.np]")
        if not filename.strip():
            filename = "data/task1.np"
        matrixes = read_matrixes(filename)
        if COMPLEX_MODE:
            B = matrix(matrixes[0])
            C = matrix(matrixes[1])
            D = matrix(matrixes[2])
            A = D + TASK_NUMBER * C
        else:
            A = matrix(matrixes[0])
            B = matrix(matrixes[1])
    elif input == 3:
        filename = raw_input("File name[data/task2.np]")
        if not filename.strip():
            filename = "data/task2.np"
        matrixes = read_matrixes(filename)
        if COMPLEX_MODE:
            T = matrix(matrixes[0])
            C = matrix(matrixes[1])
            A = T + TASK_NUMBER * C
            print A
        else:
            A = matrix(matrixes[0])
    
    if input == 1:
        ############ RELAXATION ################
        omega = float(raw_input("Omega: "))
        relaxation = Relaxation(A, B, zeros((len(B), 1)), PRECISION, omega=omega)
        result, iterations = relaxation.solve()

        print "-" * 100
        print "Calculated in %d iterations with omege %.3f" % (iterations, omega)
        print "Iterations: "
        for str_iteration in relaxation.iterations:
            print str_iteration
        print "\nResult:"
        print result

        print "-" * 100
        print "Real answer: "
        print linalg.solve(A, B)
        print "-" * 100

    elif input == 2:
        ####### Union Gradient Method ##########
        gradient = ConjugateGradient(A, B, zeros((len(B), 1)), PRECISION)
        result, iterations = gradient.solve()

        print "-" * 100
        print "Calculated in %d iterations" % iterations
        print "Iterations: "
        for str_iteration in gradient.iterations:
            print str_iteration
        print "\nResult:"
        print result

        print "-" * 100
        print "Real answer: "
        print linalg.solve(A, B)
        print "-" * 100

    elif input == 3:
        ###### Inverse iterations ##############
        # lambd = float(raw_input("Initial lambda: "))
        a = float(raw_input("a: "))
        b = float(raw_input("b: "))
        lambd = (a + b) / 2
        evals, evecs = linalg.eig(A)
        print "-" * 100
        print "Real eigen values:"
        print evals 
        print "Real normalized eigen vector"
        # print "[", " ".join(str(evecs[i,0]) for i in  range(len(evecs))), "]"
        print evecs
        print "-" * 100
        inverse = InverseIterations(A, matrix(INVERSE_X_VECTOR), lambd, INVERSE_PRECISION)
        eigenvector, eigenvalue, iterations = inverse.solve()
        if iterations < MAXIMUM_INVERESE_METHOD_ITERATIONS:
            print "Solved in %d iterations" % iterations
        else:
            print "Failed to solve..."
        for it in inverse.iterations:
            print it
        print "Eigen vector:"
        print " ".join("%.8f " % eigenvector[i,0] for i in  range(len(eigenvector)))
        print "Eigen value %.8f" % eigenvalue   
        print "-" * 100
    else:
        print "Bad input."

if __name__ == '__main__':
    try:
        main()
    except IOError, ex:
        print "Wrong filename"
        print ex
    except Exception, ex:
        print "Cant calculate."
        print ex
