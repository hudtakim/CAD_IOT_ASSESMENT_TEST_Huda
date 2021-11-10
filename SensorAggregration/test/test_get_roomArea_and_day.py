import sys
sys.path.append("..")

import unittest

from modules.convert_timestamp import convert_timestamp_to_day
from modules.get_roomArea_and_day import get_roomArea_and_day

class TestConvertTimestamp(unittest.TestCase):

    def test_types(self):
        #Raise error if the input types is not valid
        self.assertRaises(TypeError, get_roomArea_and_day, 1232.234, convert_timestamp_to_day)
        self.assertRaises(TypeError, get_roomArea_and_day, "555003003", convert_timestamp_to_day)
        self.assertRaises(TypeError, get_roomArea_and_day, 123423 ,convert_timestamp_to_day)