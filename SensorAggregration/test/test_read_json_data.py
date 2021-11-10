import sys
sys.path.append("..")

import unittest

from modules.read_json_data import read_json_data

class TestReadJsonData(unittest.TestCase):

    def test_types(self):
        #Raise error if the input types is not string
        self.assertRaises(TypeError, read_json_data, 123)
        self.assertRaises(TypeError, read_json_data, 123.05)
        self.assertRaises(TypeError, read_json_data, True)