import unittest
import pandas as pd
from dataframe_generator import DataFrameGenerator

class TestDataFrameGenerator(unittest.TestCase):
    def setUp(self):
        self.column_names_types = {
            'Name': 'str',
            'Age': 'int',
            'Weight': 'float',
            'DateOfBirth': 'date',
            'IsStudent': 'bool'
        }
        
        self.data_frame_generator = DataFrameGenerator(self.column_names_types)

    def test_generate_data_frame(self):
        rows_num = 5
        
        data_frame = self.data_frame_generator.generate_data_frame(rows_num)
        
        self.assertIsInstance(data_frame, pd.DataFrame)
        
        self.assertEqual(len(data_frame), rows_num)
        
        self.assertEqual(set(data_frame.columns), set(self.column_names_types.keys()))

    def test_generate_column_data(self):
        column_type = 'str'
        rows_num = 5
        
        column_data = self.data_frame_generator.generate_column_data(column_type, rows_num)
        
        self.assertEqual(len(column_data), rows_num)
        
        self.assertTrue(all(isinstance(value, str) for value in column_data))

if __name__ == '__main__':
    unittest.main()
