import pandas as pd

class ParquetGenerator:
    def __init__(self, data, output_path):
        self.data = data
        self.output_path = output_path

    def generate_parquet(self):
        df = pd.DataFrame(self.data)
        df.to_parquet(self.output_path)


data = {
    'column1': [1, 2, 3],
    'column2': ['a', 'b', 'c']
}
output_path = 'example.parquet'

parquet_generator = ParquetGenerator(data, output_path)
parquet_generator.generate_parquet()
