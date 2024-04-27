import pandas as pd
import random
from datetime import datetime, timedelta

class DataFrameGenerator:
    def __init__(self, column_names_types):
        self.column_names_types = column_names_types

    def generate_data_frame(self, rows_num):
        data = {column: self.generate_column_data(column_type, rows_num) for column, column_type in self.column_names_types.items()}
        return pd.DataFrame(data)

    def generate_column_data(self, column_type, rows_num):
        if column_type == 'str':
            return [self.generate_random_string() for _ in range(rows_num)]
        elif column_type == 'int':
            return [random.randint(1, 100) for _ in range(rows_num)]
        elif column_type == 'float':
            return [random.uniform(1.0, 100.0) for _ in range(rows_num)]
        elif column_type == 'date':
            return [(datetime.now() - timedelta(days=random.randint(1, 365))).strftime('%Y-%m-%d') for _ in range(rows_num)]
        elif column_type == 'bool':
            return [random.choice([True, False]) for _ in range(rows_num)]

    def generate_random_string(self):
        return ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=random.randint(5, 10)))



column_names_types = {
    'Name': 'str',
    'Age': 'int',
    'Weight': 'float',
    'DateOfBirth': 'date',
    'IsStudent': 'bool'
}

data_frame_generator = DataFrameGenerator(column_names_types)
data_frame = data_frame_generator.generate_data_frame(5)
print(data_frame)
