import sys
sys.path.append("..")

import unittest

from modules.join_json_data import join_json_data


class TestJoinJsonData(unittest.TestCase):

    def test_join_json_data1(self):
        #Test if the id for each data on both JSON files are exactly the same 
        firstJson = [{"id": 1, "name": "Andi" },{"id": 2,"name": "Budi" }]
        secondJson = [{"id": 1, "salary": 3000 },{"id": 2,"salary": 45.345 }]
        joinedJson = [{"id": 1, "name": "Andi", "salary": 3000 },{"id": 2,"name": "Budi", "salary": 45.345 }]

        self.assertAlmostEqual(join_json_data(firstJson, secondJson), joinedJson)

    def test_join_json_data2(self):
        #Test the function if the secondJSON (salaryJSON) used as first parameter
        firstJson = [{"id": 1, "name": "Andi" },{"id": 2,"name": "Budi" }]
        secondJson = [{"id": 1, "salary": 3000 },{"id": 2,"salary": 45.345 }]
        joinedJson = [{"id": 1, "name": "Andi", "salary": 3000 },{"id": 2,"name": "Budi", "salary": 45.345 }]

        self.assertAlmostEqual(join_json_data(secondJson, firstJson), joinedJson)

    def test_join_json_data3(self):
        #Test the function if the secondJSON (salaryJSON) contain data with id which is not in firstJSON
        firstJson = [{"id": 1, "name": "Andi" },{"id": 2,"name": "Budi" }]
        secondJson = [{"id": 1, "salary": 3000 },{"id": 2,"salary": 45.345 },{"id": 3,"salary": 5000 }]
        joinedJson = [{"id": 1, "name": "Andi", "salary": 3000 },{"id": 2,"name": "Budi", "salary": 45.345 }]

        self.assertAlmostEqual(join_json_data(firstJson, secondJson), joinedJson)

    def test_join_json_data4(self):
        #Test the function if the firstJSON contain data with id which is not in secondJSON (salaryJSON)
        firstJson = [{"id": 1, "name": "Andi" },{"id": 2,"name": "Budi"},{"id": 3,"name": "Agus"}]
        secondJson = [{"id": 1, "salary": 3000 },{"id": 2,"salary": 45.345 }]
        joinedJson = [{"id": 1, "name": "Andi", "salary": 3000 },{"id": 2,"name": "Budi", "salary": 45.345 }, {"id": 3,"name": "Agus"}]

        self.assertAlmostEqual(join_json_data(firstJson, secondJson), joinedJson)

    def test_types(self):
        #Make sure value errors are raised if the input are invalid
        firstJson = [[{"id": 1, "name": "Andi" },{"id": 2,"name": "Budi" }]]
        secondJson = [{"id": 1, "salary": 3000 },{"id": 2,"salary": 45.345 }]

        self.assertRaises(TypeError, join_json_data, firstJson, secondJson)
        self.assertRaises(TypeError, join_json_data, firstJson, 2432)
        self.assertRaises(TypeError, join_json_data, "testing", secondJson)