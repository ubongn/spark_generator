import unittest
from sparkdfGenerator import SparkDataFrameGenerator

class TestSparkDataFrameGenerator(unittest.TestCase):
    def setUp(self):
        self.column_names_types = {
            'Name': 'str',
            'Age': 'int',
            'Weight': 'float',
            'DateOfBirth': 'date',
            'IsStudent': 'bool'
        }
        self.generator = SparkDataFrameGenerator(self.column_names_types)

    def test_generate_data_frame(self):
        rows_num = 5
        df = self.generator.generate_data_frame(rows_num)
        self.assertIsNotNone(df)
        self.assertEqual(df.count(), rows_num)

if __name__ == '__main__':
    unittest.main()
