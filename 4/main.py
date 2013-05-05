from math import sin, exp
from simpsons import Simpsons
from gaussian import Gaussian
from utilities import runge_error

FUNCTION = lambda x : sin(3*x) 
# FUNCTION = lambda x : x*exp(2*x)
class TASK1:
    HIGH = 5.0
    LOW = 0
    PRECISION = 4

    NODES_LIMIT = 1024

class TASK2:
    HIGH = 5.0
    LOW = 0
    PRECISION = 6

    NODES_LIMIT = 4096


MENU = """
1. Simpsons
2. 
3. 
"""
INPUT = 2
# 58656263777
def handle_simpsons_task():
    print "{0: >8}\t{1: <16} {2: <14} {3: <18}".format(
                "Nodes", "Result", "H", "Runge")

    nodes = 2
    prev_result = 0.0
    while nodes <= TASK1.NODES_LIMIT:
        simpsons = Simpsons(FUNCTION, nodes, TASK1.HIGH, TASK1.LOW)
        result = simpsons.integrate()
        if prev_result != 0:
            runge = runge_error(prev_result, result, TASK1.PRECISION)
            output = "{0: >8}\t{1: <16} {2: <14} {3: <18}".format(
                nodes, result, simpsons.h, runge)
        else:
            output = "{0: >8}\t{1: <16} {2: <14}".format(
                nodes, result, simpsons.h)
        print output

        prev_result = result
        nodes *= 2

def handle_gaussian_task():
    print "{0: >8}\t{1: <16} {2: <14} {3: <18}".format(
                "Nodes", "Result", "H", "Runge")
    nodes = 2
    prev_result = 0.0
    while nodes <= TASK2.NODES_LIMIT:
        gauss = Gaussian(FUNCTION, TASK2.HIGH, TASK2.LOW, nodes)
        result = gauss.integrate()
        if prev_result != 0:
            runge = runge_error(prev_result, result, TASK2.PRECISION)
            output = "{0: >8}\t{1: <16} {2: <14} {3: <18}".format(
                nodes, result, gauss.h, runge)
        else:
            output = "{0: >8}\t{1: <16} {2: <14}".format(
                nodes, result, gauss.h)
        print output

        prev_result = result
        nodes *= 2

def main():
    # TODO handle input

    if INPUT == 1:
        handle_simpsons_task()
    elif INPUT == 2:
        handle_gaussian_task()
    elif INPUT == 3:
        pass


if __name__ == "__main__":
    main()