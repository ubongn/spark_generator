import unittest
from csvgen import CsvGenerator 

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
        # Generate sample data
        rows_num = 2
        sample_data = self.csvgen.generate_data(rows_num)
        
        # Check if data is generated
        self.assertIsNotNone(sample_data)
        
        # Check if data contains the expected columns
        expected_columns = self.column_names_types.keys()
        self.assertCountEqual(sample_data.keys(), expected_columns)
        
        # Check data types of each column
        for col, dtype in self.column_names_types.items():
            for value in sample_data[col]:
                if dtype == "str":
                    self.assertIsInstance(value, str)
                elif dtype == "int":
                    self.assertIsInstance(value, int)
                elif dtype == "float":
                    self.assertIsInstance(value, float)
                elif dtype == "date":
                    self.assertIsInstance(value, str)  # Date is represented as string
                    # Add additional date format validation if required
                elif dtype == "boolean":
                    self.assertIsInstance(value, bool)
        
        # Check if the number of rows generated matches the expected number
        for col, values in sample_data.items():
            self.assertEqual(len(values), rows_num)

if __name__ == "__main__":
    unittest.main()