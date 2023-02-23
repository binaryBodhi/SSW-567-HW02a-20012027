# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testScaleneTriangle(self):
        self.assertEqual(classifyTriangle(5, 7, 9), 'Scalene', '5, 7, 9 is a scalene triangle')

    def testIsoscelesTriangle(self):
        self.assertEqual(classifyTriangle(2, 2, 1), 'Isoceles', '2, 2, 1 is an isosceles triangle.')

    def testInvalidInput(self):
        self.assertEqual(classifyTriangle('a', 2, 1), 'InvalidInput', 'All sides shall be an integer value.')

    def testLengthLimit(self):
        self.assertEqual(classifyTriangle(201, 9, 100), 'InvalidInput', 'All sides shall have a value less than 200')

    def testNegativeInput(self):
        self.assertEqual(classifyTriangle(-1, 2, -9), 'InvalidInput', 'All sides shall have a positive value.')

    def testForNotATriangle(self):
        self.assertEqual(classifyTriangle(12, 5, 7), 'NotATriangle', 'For a triangle, the sum of any two sides shall be strictly less than the third side.')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
