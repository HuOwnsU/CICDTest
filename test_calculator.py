#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 15:48:51 2023

@author: faridharati
"""

import unittest
from calculator import addition, subtraction

class CalculatorTest(unittest.TestCase):
    def test_addition(self):
        result = addition(2,3)
        self.assertEqual(result, 5)
    def test_subtraction(self):
        result = subtraction(5,2)
        self.assertEqual(result, 3)