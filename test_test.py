import unittest
import test

class TestClass(unittest.TestCase):

    def test_add(self):
        #test the add function from test.py
        self.assertAlmostEqual(test.addNumber(1,3),4)
        self.assertAlmostEqual(test.addNumber(3,3),6)
        self.assertAlmostEqual(test.addNumber(-3,-3),-6)
        self.assertAlmostEqual(test.addNumber(-5,3),-2)

    def test_subtract(self):
        self.assertAlmostEqual(test.subtractNumber(1,3),-2)
        self.assertAlmostEqual(test.subtractNumber(3,3),0)
        self.assertAlmostEqual(test.subtractNumber(-3,-3),0)
        self.assertAlmostEqual(test.subtractNumber(-5,3),-8)
