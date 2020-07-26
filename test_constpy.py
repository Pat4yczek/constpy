import unittest
from constpy import *
import math

class TestConstPy(unittest.TestCase):
    def testMathConst(self):
        self.assertEqual(ConstPy.get('pi'), math.pi)