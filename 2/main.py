import sys
import math
import numpy as np
import matplotlib.pyplot as plt
import logging

from relaxation import RelaxationMethod
from secant import SecantMethod

MENU = \
    """
1 - Draw plot
2 - Relaxation method
3 - Relaxation method with optimal omega
4 - Secant method

0 - Quit
"""


FUNCTION_G = lambda x: math.exp(-x ** 2)
FUNCTION_F = lambda x: FUNCTION_G(x) - x
DERIVATIVE_FUNCTION_G = lambda x: -2 * x * math.exp(-x ** 2)

# FUNCTION_G = lambda x: math.cos(2*x)
# DERIVATIVE_FUNCTION_G = lambda x: -2*math.sin(x)

DEFAULT_RANGE_START = 0
DEFAULT_RANGE_END = 2
DEFAULT_PRECISION = 0.0000001
DEFAULT_X0 = 0.0
DEFAULT_X1 = 1.0

TICKNESS = 0.01


def get_int_or_empty_input(message=""):
    try:
        return int(raw_input(message))
    except ValueError:
        return ""


def get_float_or_empty_input(message=""):
    try:
        input = float(raw_input(message))
        return input
    except ValueError:
        return ""


def main():
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

    print MENU
    choose = get_int_or_empty_input()

    while choose != 0:
        if choose == 1:
            range_start = get_float_or_empty_input(
                "Enter range start [%d by default]: " % DEFAULT_RANGE_START)
            if range_start == "":
                range_start = DEFAULT_RANGE_START
            range_end = get_float_or_empty_input(
                "Enter range end[%d by default]: " % (DEFAULT_RANGE_END + range_start))
            if range_end == "":
                range_end = DEFAULT_RANGE_END + range_start

            t = np.arange(range_start, range_end, TICKNESS)
            plt.plot(t, map(FUNCTION_G, t), t, map(lambda x: x, t))
            plt.show()

        elif choose == 2:
            omega = get_float_or_empty_input("Enter omega value: ")
            if omega == "":
                print "Omega is not float value."
            elif not (0 < omega <= 1):
                print "Bad omega value not in (0;1]"
            else:
                point = get_float_or_empty_input("Enter point value: ")
                if point == "":
                    print "Point is not float. Use default 0.0"
                    point = 0.0

                precision = get_float_or_empty_input(
                    "Enter precision [%.15f by default]: " % DEFAULT_PRECISION)
                if precision == "":
                    precision = DEFAULT_PRECISION

                relaxation = RelaxationMethod(
                    FUNCTION_G, DERIVATIVE_FUNCTION_G, omega)
                print
                try:
                    result = relaxation.calculate(point, precision)
                    omega = relaxation.find_omega()
                except ZeroDivisionError:
                    print "Zero division detected, cant find answer."
                    result = None
                print
                if result is not None:
                    print "Equation result %.15f with precision %.15f" % (result, precision)
                    print "Exact value 0.652919"
                    print "Omega %.15f" % omega
                else:
                    print "Cant find answer. Equation diverges."

        elif choose == 3:
            precision = get_float_or_empty_input(
                "Enter precision [%.15f by default]: " % DEFAULT_PRECISION)
            if precision == "":
                precision = DEFAULT_PRECISION
            point = get_float_or_empty_input("Enter point value: ")
            if point == "":
                print "Point is not float. Use default 0.0"
                point = 0.0

            relaxation = RelaxationMethod(FUNCTION_G, DERIVATIVE_FUNCTION_G)
            omega = relaxation.find_omega()
            if omega is None:
                print "Cant find optimal omege. Equation diverges."
            else:
                print "Optimal omega is %.15f" % omega
                print
                print "Calculate with optimal omega: "
                try:
                    result = relaxation.calculate(point, precision)
                except ZeroDivisionError:
                    print "Zero division detected, cant find answer."
                    result = None

                if result is not None:
                    print "Equation result %.15f with precision %.15f" % (result, precision)
                    print "Exact value 0.652919"
                else:
                    print "Cant find answer. Equation diverges."
        elif choose == 4:
            x0 = get_float_or_empty_input(
                "Enter x0 [%f by default]: " % DEFAULT_X0)
            if x0 == "": x0 = DEFAULT_X0
            x1 = get_float_or_empty_input(
                "Enter x1 [%f by default]: " % DEFAULT_X1)
            if x1 == "": x1 = DEFAULT_X1
            precision = get_float_or_empty_input(
                "Enter precision [%.15f by default]: " % DEFAULT_PRECISION)
            if precision == "": precision = DEFAULT_PRECISION
            
            secant = SecantMethod(FUNCTION_F)
            try:
                result = secant.calculate(x0, x1, precision)
            except ZeroDivisionError:
                    print "Zero division detected, cant find answer."
                    result = None

            if result is not None:
                print "Equation result %.15f with precision %.15f" % (result, precision)
                print "Exact value 0.652919"
            else:
                print "Cant find answer. Equation diverges."
        else:
            print "Bad choise."
        print MENU
        choose = get_int_or_empty_input()

if __name__ == '__main__':
    main()
