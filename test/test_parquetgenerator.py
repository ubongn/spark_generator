import unittest
import os
import pandas as pd
from parquetGenerator import ParquetGenerator

class TestParquetGenerator(unittest.TestCase):
    def setUp(self):
        self.data = {
            'column1': [1, 2, 3],
            'column2': ['a', 'b', 'c']
        }
        self.output_path = 'test_output.parquet'
        self.parquet_generator = ParquetGenerator(self.data, self.output_path)

    def test_generate_parquet(self):
        
        self.parquet_generator.generate_parquet()

        self.assertTrue(os.path.exists(self.output_path))

        df = pd.read_parquet(self.output_path)

        self.assertEqual(len(df), len(self.data['column1']))
        for column, values in self.data.items():
            self.assertTrue(column in df.columns)
            self.assertListEqual(list(df[column]), values)

    def tearDown(self):
        if os.path.exists(self.output_path):
            os.remove(self.output_path)

if __name__ == '__main__':
    unittest.main()
