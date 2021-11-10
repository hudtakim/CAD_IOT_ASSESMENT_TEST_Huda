import sys
sys.path.append("..")

import unittest

from modules.make_dict import make_dict

class TestMakeDict(unittest.TestCase):

    def test_types(self):
        #Raise error if the input types is not integer
        self.assertRaises(TypeError, make_dict, "1232.234", ['1', '2'])
        self.assertRaises(TypeError, make_dict, "555003003", {1,2,3})
        self.assertRaises(TypeError, make_dict, True, (1,2,3))
        self.assertRaises(TypeError, make_dict, 8324, (1,2,3))