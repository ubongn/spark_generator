from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType, DateType, BooleanType
import random
from datetime import datetime, timedelta

class SparkDataFrameGenerator:
    def __init__(self, column_names_types):
        self.column_names_types = column_names_types
        self.spark = SparkSession.builder \
            .appName("DataFrameGenerator") \
            .getOrCreate()

    def generate_data_frame(self, rows_num):
        rows = [self.generate_row(rows_num) for _ in range(rows_num)]
        schema = self.generate_schema()
        return self.spark.createDataFrame(rows, schema)

    def generate_row(self, rows_num):
        return Row(**{column: self.generate_column_data(column_type, rows_num) for column, column_type in self.column_names_types.items()})

    def generate_schema(self):
        fields = [StructField(column, self.map_type(column_type), True) for column, column_type in self.column_names_types.items()]
        return StructType(fields)

    def map_type(self, column_type):
        if column_type == 'str':
            return StringType()
        elif column_type == 'int':
            return IntegerType()
        elif column_type == 'float':
            return FloatType()
        elif column_type == 'date':
            return DateType()
        elif column_type == 'bool':
            return BooleanType()

    def generate_column_data(self, column_type, rows_num):
        if column_type == 'str':
            return [self.generate_random_string() for _ in range(rows_num)]
        elif column_type == 'int':
            return [random.randint(1, 100) for _ in range(rows_num)]
        elif column_type == 'float':
            return [random.uniform(1.0, 100.0) for _ in range(rows_num)]
        elif column_type == 'date':
            return [(datetime.now() - timedelta(days=random.randint(1, 365))) for _ in range(rows_num)]
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

data_frame_generator = SparkDataFrameGenerator(column_names_types)
data_frame = data_frame_generator.generate_data_frame(5)
data_frame.show()
