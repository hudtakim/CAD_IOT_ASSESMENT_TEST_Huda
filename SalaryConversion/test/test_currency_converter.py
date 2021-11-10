import sys
sys.path.append("..")

import unittest

from modules.currency_converter import convertIDRToUSD

class TestCurrencyConverter(unittest.TestCase):
    def test_input_type(self):
        #Make sure to raise error if the input is not int or float
        self.assertRaises(TypeError, convertIDRToUSD, 3423, "14000")
        self.assertRaises(TypeError, convertIDRToUSD, "3423", 14000)
        self.assertRaises(TypeError, convertIDRToUSD, "3423", "14000")

    def test_input_value(self):
        #Make sure to raise error if the input is negative
        self.assertRaises(ValueError, convertIDRToUSD, -5, 14000)
        self.assertRaises(ValueError, convertIDRToUSD, 5, -14000)
        self.assertRaises(ValueError, convertIDRToUSD, -5, -14000)