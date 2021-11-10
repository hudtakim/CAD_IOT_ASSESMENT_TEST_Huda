import sys
sys.path.append("..")

import unittest

from modules.convert_timestamp import convert_timestamp_to_day

class TestConvertTimestamp(unittest.TestCase):

    def test_types(self):
        #Raise error if the input types is not valid
        self.assertRaises(TypeError, convert_timestamp_to_day, "1232.234")
        self.assertRaises(TypeError, convert_timestamp_to_day, "555003003")
        self.assertRaises(TypeError, convert_timestamp_to_day, True)