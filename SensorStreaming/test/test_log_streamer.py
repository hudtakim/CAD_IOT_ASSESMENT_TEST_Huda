import sys
sys.path.append("..")

import unittest

from modules.log_streamer import log_streamer
class TestLogStreamer(unittest.TestCase):

    def test_types(self):
        #Raise error if the input types is not valid
        self.assertRaises(TypeError, log_streamer, "string", "string", {1,2,3,4}, 12)
        self.assertRaises(TypeError, log_streamer, "string", "string", [1,2,3,3], 12.4)
        self.assertRaises(TypeError, log_streamer, "string", 23, [1,2,3,4], 12)
        self.assertRaises(TypeError, log_streamer, 1212, "String", [1,2,3,4], 12)
