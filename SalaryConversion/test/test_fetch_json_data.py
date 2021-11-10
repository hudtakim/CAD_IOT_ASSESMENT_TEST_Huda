import sys
sys.path.append("..")

import unittest

from modules.fetch_json_data import fetch_json_data

class TestFetchJsonData(unittest.TestCase):

    def test_types(self):
        #Make sure value errors are raised if the input types is not string
        self.assertRaises(TypeError, fetch_json_data, 123)
        self.assertRaises(TypeError, fetch_json_data, 123.05)
        self.assertRaises(TypeError, fetch_json_data, True)