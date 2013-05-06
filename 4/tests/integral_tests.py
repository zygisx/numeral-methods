import unittest
from math import sin
from simpsons import Simpsons
from gaussian import Gaussian

FUNCTION  = lambda x : sin(3*x) 

class BaseIntegralTests(unittest.TestCase):

    def setUp(self):
        self.function = FUNCTION
        self.accurate_result = 0.5865626376
        self.low = 0
        self.high = 5

class SimpsonsTest(BaseIntegralTests):

    def test_simpsons_result_with_32_nodes(self):
        self.common_flow(32, 3)

    def test_simpsons_result_with_256_nodes(self):
        self.common_flow(256, 7)

    def common_flow(self, nodes, accuracy):
        simpsons = Simpsons(self.function, nodes, self.high, self.low)
        result = simpsons.integrate()

        self.assertAlmostEquals(result, self.accurate_result, accuracy)

class GaussianTest(BaseIntegralTests):

    def test_gaussian_result_with_8_nodes(self):
        self.common_flow(32, 3)

    def test_gaussian_result_with_256_nodes(self):
        self.common_flow(64, 7)

    def common_flow(self, nodes, accuracy):
        gauss = Gaussian(self.function, self.high, self.low, nodes)
        result = gauss.integrate()

        self.assertAlmostEquals(result, self.accurate_result, accuracy)

