import unittest


class TestCsvgen(unittest.TestCase):
    def setUp(self):
       self.csvgen = TestCsvgen({"Name":"str", "Age": "int"})
       
    def test_genratedata(self):
        self.csvgen.genratedata(rows_num=3)   
        self.assertIsNone(self.csvgen.genratedata)
        
        
        
    def test_genpact(self):
        pass    
    
    
    
if __name__ == "__main__":
    unittest.main()