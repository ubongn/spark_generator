import unittest
from csvGenerator import CsvGenerator 

class TestCsvgen(unittest.TestCase):
    def setUp(self):
        self.column_names_types = {
            "Name": "str",
            "Age": "int",
            "Weight": "float",
            "DateOfBirth": "date",
            "IsStudent": "boolean"
        }
        self.csvgen = CsvGenerator(self.column_names_types)

    def test_generate_data(self):
        
        rows_num = 2
        sample_data = self.csvgen.generate_data(rows_num)
        
        self.assertIsNotNone(sample_data)
        
        expected_columns = self.column_names_types.keys()
        self.assertCountEqual(sample_data.keys(), expected_columns)
        
        for col, dtype in self.column_names_types.items():
            for value in sample_data[col]:
                if dtype == "str":
                    self.assertIsInstance(value, str)
                elif dtype == "int":
                    self.assertIsInstance(value, int)
                elif dtype == "float":
                    self.assertIsInstance(value, float)
                elif dtype == "date":
                    self.assertIsInstance(value, str)  
                elif dtype == "boolean":
                    self.assertIsInstance(value, bool)
        
        for col, values in sample_data.items():
            self.assertEqual(len(values), rows_num)

if __name__ == "__main__":
    unittest.main()
