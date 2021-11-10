import sys
sys.path.append("..")

import unittest

from modules.stream_to_csv import stream_to_csv

class TestStreamToCSV(unittest.TestCase):

    def test_types(self):
        #Raise error if the input types is not valid
        self.assertRaises(TypeError, stream_to_csv, 1223, ["col1", "col2"], 12, 3)
        self.assertRaises(TypeError, stream_to_csv, 12.234, ["col1", "col2"], 23, 23)
        self.assertRaises(TypeError, stream_to_csv, True, ["col1", "col2"], 23, 23)
        self.assertRaises(TypeError, stream_to_csv, "output/", {"col1", "col2"},2 , 2)
        self.assertRaises(TypeError, stream_to_csv, [1,2,3], {"col1", "col2"},2 , 2)
        self.assertRaises(TypeError, stream_to_csv, [1,2,3], "string",2 , 2.2)
