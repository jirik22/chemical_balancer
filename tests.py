import unittest
import main
import ratios

class TestComptodict(unittest.TestCase):
    def test_Coplex_Compounds(self): 
        self.assertDictEqual(main.comp_to_dict("K2[CrO4]2"), {'K': 2, 'Cr': 2, 'O': 8})
        
    def test_case_sensitivity(self):
        self.assertDictEqual(main.comp_to_dict("CsCS"),{'C': 1, 'Cs': 1, 'S': 1})
    
    def test_long_compounds(self):
        self.assertDictEqual(main.comp_to_dict("CuXeFeN5(NO3)2ClP"), {'Cu': 1, 'Xe': 1, 'Fe': 1, 'N': 7, 'O': 6, 'Cl': 1, 'P': 1})
        
    #def test_multiple_didgits(self):
    #    self.assertDictEqual(main.comp_to_dict("C552He889O226"), {'C': 552, 'He': 889, 'O': 226})
        
    def test_mutliple_brackets(self):
        self.assertDictEqual(main.comp_to_dict("([(CaO2)3U2]2Fe5)2N"), {'Ca': 12, 'O': 24, 'U': 8, 'Fe': 10, 'N': 1 })

class TestRatios(unittest.TestCase):
    def test_float_to_ratio(self):
        self.assertEqual(ratios.float_to_ratio([0.5, 0.25, 0.75]), [2, 1, 3])
        
    def test_long_ratio(self):
        self.assertEqual(ratios.float_to_ratio([0.29704, 0.792114, 0.29704, 0.19802, 0.39605]), [3, 8, 3, 2, 4])
        
    def test_fractions(self):
        self.assertEqual(ratios.float_to_ratio([0.3333333333333333, 0.6666666666666666]), [1, 2])
        
    def test_long_fractions(self):
        self.assertEqual(ratios.float_to_ratio([2/53, 5/53, 8/53, 12/106]), [2, 5, 8, 6])
        self.assertEqual(ratios.float_to_ratio([2/15, 5/30, 8/60, 7/60]), [8, 10, 8, 7])

if __name__ == "__main__":
    unittest.main()
