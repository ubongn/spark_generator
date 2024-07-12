import unittest
import os
from faker import Faker
from csvGenerator import CsvGenerator

class TestCsvGenerator(unittest.TestCase):
    def setUp(self):
        fake = Faker()
        num_rows = 10
        self.column_names_types = {
            'Name': 'str',
            'Age': 'int',
            'Weight': 'float',
            'DateOfBirth': 'date',
            'IsStudent': 'bool'
        }
        self.data = {
            column: self.generate_fake_data(column_type, num_rows, fake)
            for column, column_type in self.column_names_types.items()
        }
        self.output_path = 'test_output.csv'
        self.csv_generator = CsvGenerator(self.column_names_types, self.output_path)

    def generate_fake_data(self, column_type, num_rows, fake):
        if column_type == 'str':
            return [fake.name() for _ in range(num_rows)]
        elif column_type == 'int':
            return [fake.random_int(min=18, max=80) for _ in range(num_rows)]
        elif column_type == 'float':
            return [fake.random_number() for _ in range(num_rows)]
        elif column_type == 'date':
            return [fake.date() for _ in range(num_rows)]
        elif column_type == 'bool':
            return [fake.boolean() for _ in range(num_rows)]

    def test_generate_csv(self):
        # Generate the CSV file
        self.csv_generator.generate_csv(self.data)

        # Check if the file exists
        self.assertTrue(os.path.exists(self.output_path))

        # Read the CSV file
        with open(self.output_path, 'r') as f:
            lines = f.readlines()

        self.assertEqual(len(lines), len(self.data[list(self.column_names_types.keys())[0]]) + 1)  # Plus 1 for header

    def tearDown(self):
        
        if os.path.exists(self.output_path):
            os.remove(self.output_path)

if __name__ == '__main__':
    unittest.main()
