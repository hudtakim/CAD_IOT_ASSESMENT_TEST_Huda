import sys
sys.path.append("..")

import unittest

from modules.stream_json_data import stream_json_data

class TestStreamJsonData(unittest.TestCase):

    def test_types(self):
        #Raise error if the input types is not valid
        self.assertRaises(TypeError, stream_json_data, 1223)
        self.assertRaises(TypeError, stream_json_data, 12.234)
        self.assertRaises(TypeError, stream_json_data, True)