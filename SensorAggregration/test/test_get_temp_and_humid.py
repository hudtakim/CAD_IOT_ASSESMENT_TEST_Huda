import sys
sys.path.append("..")

import unittest

from modules.get_temp_and_humid import get_temp_and_humid

class TestGetTempAndHumid(unittest.TestCase):

    def test_types(self):
        #Raise error if the input types is not valid
        self.assertRaises(TypeError, get_temp_and_humid, "1232.234", ['1', '2'], "input")
        self.assertRaises(TypeError, get_temp_and_humid, "555003003", {1,2,3}, [1,2,3,4])
        self.assertRaises(TypeError, get_temp_and_humid, True, (1,2,3), [1,2,3,4])
        self.assertRaises(TypeError, get_temp_and_humid, 8324, [1,2,3,4],(1,2,3))