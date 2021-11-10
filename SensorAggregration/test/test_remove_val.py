import sys
sys.path.append("..")

import unittest

from modules.remove_val import remove_val

class TestRemoveVal(unittest.TestCase):

    def test_types(self):
        #Raise error if the input types is not valid
        self.assertRaises(TypeError, remove_val, "1232.234", ['1', '2'], "input")
        self.assertRaises(TypeError, remove_val, "555003003", {1,2,3}, [1,2,3,4])
        self.assertRaises(TypeError, remove_val, True, (1,2,3), [1,2,3,4])
        self.assertRaises(TypeError, remove_val, 8324, [1,2,3,4],(1,2,3))