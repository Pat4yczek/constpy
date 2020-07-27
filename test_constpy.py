import unittest
import constpy as const
import math

class TestConstPy(unittest.TestCase):
    def testMathConst(self):
        self.assertEqual(const.get('pi'), math.pi)