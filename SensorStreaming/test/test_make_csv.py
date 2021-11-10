import sys
sys.path.append("..")

import unittest

from modules.make_csv import make_csv

class TestMakeCSV(unittest.TestCase):

    def test_types(self):
        #Raise error if the input types is not valid
        self.assertRaises(TypeError, make_csv, 1223, ["col1", "col2"])
        self.assertRaises(TypeError, make_csv, 12.234, ["col1", "col2"])
        self.assertRaises(TypeError, make_csv, True, ["col1", "col2"])
        self.assertRaises(TypeError, make_csv, "output/", {"col1", "col2"})
