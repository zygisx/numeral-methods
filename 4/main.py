from math import sin, exp, cos
from simpsons import Simpsons
from gaussian import Gaussian
from runge_kutta import RungeKutta
from utilities import runge_error

FUNCTION  = lambda x : sin(3*x)
FUNCTION2 = lambda x, y : y * cos(y - x/2.0)**2 + 0.1 * x**2

class TASK1:
    HIGH = 1.0
    LOW = 0
    PRECISION = 4

    NODES_LIMIT = 4096

class TASK2:
    HIGH = 5.0
    LOW = 0
    PRECISION = 6

    NODES_LIMIT = 4096

class TASK3:
    N_LIMIT = 4096 * 16
    PRECISION = 2

MENU = """
1. Simpsons
2. Gauss 3rd
3. Runge Kutta 
4. Runge Kutta [single h]
"""
INPUT = 3

def handle_simpsons_task():
    print "{0: >8}\t{1: <16} {2: <14} {3: <18}".format(
                "Nodes", "Result", "H", "Runge")

    nodes = 2
    prev_result = 0.0
    prev_runge = 0.0
    runge = 0.1
    while nodes <= TASK1.NODES_LIMIT:
        simpsons = Simpsons(FUNCTION, nodes, TASK1.HIGH, TASK1.LOW)
        result = simpsons.integrate()
        if prev_result != 0:
            runge = runge_error(prev_result, result, TASK1.PRECISION)
            if runge == 0.0: runge = 0.001
            output = "{0: >8}\t{1: <16} {2: <14} {3: <18} {4: <14}".format(
                nodes, result, simpsons.h, runge, prev_runge*1.0/runge)
        else:
            output = "{0: >8}\t{1: <16} {2: <14}".format(
                nodes, result, simpsons.h)
        print output

        prev_result = result
        prev_runge = runge
        nodes *= 2

def handle_gaussian_task():
    print "{0: >8}\t{1: <16} {2: <14} {3: <18}".format(
                "Nodes", "Result", "H", "Runge")
    nodes = 2
    prev_result = 0.0
    prev_runge = 0.0
    runge = 0.0
    while nodes <= TASK2.NODES_LIMIT:
        gauss = Gaussian(FUNCTION, TASK2.HIGH, TASK2.LOW, nodes)
        result = gauss.integrate()
        if prev_result != 0:
            runge = runge_error(prev_result, result, TASK2.PRECISION)
            output = "{0: >8}\t{1: <16} {2: <14} {3: <18} {4: <14}".format(
                nodes, result, gauss.h, runge, prev_runge*1.0/runge)
        else:
            output = "{0: >8}\t{1: <16} {2: <14}".format(
                nodes, result, gauss.h)
        print output

        prev_result = result
        prev_runge = runge
        nodes *= 2

def handle_runge_kutta(u0):
    print "{0: >16}\t{1: <16} {2: <14}".format(
                "H", "Result", "Runge")
    ranges = 10
    prev_result = 0.0
    prev_runge = 0.0
    runge = 0.0
    while ranges <= TASK3.N_LIMIT:
        runge_kutta = RungeKutta(FUNCTION2, u0=u0, start=0.0, end=1.0, ranges=ranges)
        result, h = runge_kutta.solve()
        if prev_result != 0:
            runge = runge_error(prev_result, result, TASK3.PRECISION)
            output = "{0: >16}\t{1: <16} {2: <14} {3: <14}".format(
                h, result, runge, prev_runge*1.0/runge)
        else:
            output = "{0: >16}\t{1: <16}".format(
                h, result)
        print output

        prev_result = result
        prev_runge = runge
        ranges *= 2

def main():
    print MENU
    INPUT = int(raw_input("Option: "))

    if INPUT == 1:
        handle_simpsons_task()
    elif INPUT == 2:
        handle_gaussian_task()
    elif INPUT == 3:
        u0 = float(raw_input("Enter u0: "))
        handle_runge_kutta(u0)
    elif INPUT == 4:
        u0 = float(raw_input("Enter u0: "))
        ranges = float(raw_input("Enter ranges: "))
        runge = RungeKutta(FUNCTION2, u0=u0, start=0.0, end=1.0, ranges=ranges)
        result, h = runge.solve(output=True)
        print "RESULT: {0} with h={1}".format(result, h)



if __name__ == "__main__":
    main()