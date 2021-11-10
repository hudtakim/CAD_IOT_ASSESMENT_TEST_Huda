import sys
sys.path.append("..")

import unittest

from modules.set_val import set_val

class TestSetVal(unittest.TestCase):

    def test_types(self):
        #Raise error if the input types is not valid
        self.assertRaises(TypeError, set_val, "1232.234", ['1', '2'], "input")
        self.assertRaises(TypeError, set_val, "555003003", {1,2,3}, [1,2,3,4])
        self.assertRaises(TypeError, set_val, True, (1,2,3), [1,2,3,4])
        self.assertRaises(TypeError, set_val, 8324, [1,2,3,4],(1,2,3))