class Csvgen():
    def __init__(self, dic_columnames_types) -> None:
        {
            "Name" : "str",
            "Age" : "int",
        }
        
        
        self.dic_columnames_types = dic_columnames_types
        self.data = None
        
        
    def genratedata(self, rows_num):
        rows_data = {k:[] for k in self.dic_columnames_types.keys()}
        
        for _ in range(rows_num):
            for k,v in self.dic_columnames_types.items():
                if v == "str":
                    rows_data[k].append("Ubong")
                    
                if v == "int":
                    rows_data[k].append(1)        