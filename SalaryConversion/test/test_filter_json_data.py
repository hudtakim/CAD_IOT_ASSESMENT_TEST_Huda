import sys
sys.path.append("..")

import unittest

from modules.filter_json_data import filter_json_data

class TestFilterJsonData(unittest.TestCase):
    def test_types(self):
        #Make sure value errors are raised if the input are invalid
        json1 = [[{"id": 1, "name": "Andi" },{"id": 2,"name": "Budi" }]]
        json2 = [{"id": 1, "salary": 3000 },{"id": 2,"salary": 45.345 },["id", 3]]
        json3 = '[{"id": 1, "salary": 3000 },{"id": 2,"salary": 45.345 }]'

        self.assertRaises(TypeError, filter_json_data, json1)
        self.assertRaises(TypeError, filter_json_data, json2)
        self.assertRaises(TypeError, filter_json_data, json3)
        self.assertRaises(TypeError, filter_json_data, 123)
        self.assertRaises(TypeError, filter_json_data, "test")
        