import unittest
import main

class TestComptodict(unittest.TestCase):
    
    def testCoplexCompounds(self): 
        self.assertDictEqual(main.comp_to_dict("K2[CrO4]2"), {'K': 2, 'Cr': 2, 'O': 8})
    
    def test_long_compounds(self):
        self.assertDictEqual(main.comp_to_dict("CuXeFeN5(NO3)2ClP"), {'Cu': 1, 'Xe': 1, 'Fe': 1, 'N': 7, 'O': 6, 'Cl': 1, 'P': 1})
        
    def test_multiple_didgits(self):
        self.assertDictEqual(main.comp_to_dict("C552He889O226"), {'C': 552, 'He': 889, 'O': 226})
        
    #def test_combined_brackets(self):
        #self.assertDictEqual(main.comp_to_dict("Cu[N22Po]21[(H2Fr)15(NO37)5]52"), {'Cu': 1, 'N': 22, 'Po': 21, 'H': 30, 'Fr': 15, 'O': 185}) 

if __name__ == "__main__":
    unittest.main()
