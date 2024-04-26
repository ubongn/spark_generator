class Csvgen:
    def __init__(self, dic_columnames_types):
        self.dic_columnames_types = dic_columnames_types
        self.data = None

    def generate_data(self, rows_num):
        rows_data = {k: [] for k in self.dic_columnames_types.keys()}
    
        for _ in range(rows_num):
            for k, v in self.dic_columnames_types.items():
                if v == "str":
                    rows_data[k].append("Ubong")
                elif v == "int":
                    rows_data[k].append(1)
                elif v == "float":
                    rows_data[k].append(1.0)
                elif v == "date":
                    rows_data[k].append("2024-04-24")
                elif v == "boolean":
                    rows_data[k].append(True)
        
        self.data = rows_data
        return rows_data


column_names_types = {
    "Name": "str",
    "Age": "int",
    "Weight": "float",
    "DateOfBirth": "date",
    "IsStudent": "boolean"
}
csv_gen = Csvgen(column_names_types)

sample_data = csv_gen.generate_data(5)
print(sample_data)