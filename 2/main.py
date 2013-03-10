import sys

import math
from relaxation import RelaxationMethod


FUNCTION = lambda x: math.exp(-x ** 2)
DERIVATIVE_FUNCTION = lambda x: -2*x*math.exp(-x ** 2)


relaxation = RelaxationMethod(FUNCTION, DERIVATIVE_FUNCTION)
print relaxation.calculate(0.00001)
print relaxation.find_omega()



