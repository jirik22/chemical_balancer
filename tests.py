import unittest
import main
import ratios

class TestComptodict():
    def test_Coplex_Compounds(self): 
        self.assertDictEqual(main.comp_to_dict("K2[CrO4]2"), {'K': 2, 'Cr': 2, 'O': 8})
        
    def test_case_sensitivity(self):
        self.assertDictEqual(main.comp_to_dict("CsCS"),{'C': 1, 'Cs': 1, 'S': 1})
    
    def test_long_compounds(self):
        self.assertDictEqual(main.comp_to_dict("CuXeFeN5(NO3)2ClP"), {'Cu': 1, 'Xe': 1, 'Fe': 1, 'N': 7, 'O': 6, 'Cl': 1, 'P': 1})
        
    def test_multiple_didgits(self):
        self.assertDictEqual(main.comp_to_dict("C552He889O226"), {'C': 552, 'He': 889, 'O': 226})
        
    def test_hydrates(self):
        self.assertDictEqual(main.comp_to_dict("CuSO4*5H2O"), {'Cu': 1, 'S': 1, 'O': 9, 'H': 10})
             
    def test_mutliple_brackets(self):
        self.assertDictEqual(main.comp_to_dict("([(CaO2)3U2]2Fe5)2N"), {'Ca': 12, 'O': 24, 'U': 8, 'Fe': 10, 'N': 1 })

 
 
class TestRatios():
    def test_float_to_ratio(self):
        self.assertDictEqual(ratios.float_to_ratio([0.5, 0.25, 0.75]), [2, 1, 3])
        
    #def test_long_ratio(self):
        #self.assertDictEqual(ratios.float_to_ratio([0.29704, 0.792114, 0.29704, 0.19802, 0.39605]), [3, 8, 3, 2, 4])
        
    def test_fractions(self):
        self.assertDictEqual(ratios.float_to_ratio([1/3,2/3]), [1, 2])
        
    def test_long_fractions(self):
        self.assertDictEqual(ratios.float_to_ratio([2/53, 5/53, 8/53, 6/53]), [2, 5, 8, 6])
    #def test_random(self):
        #self.assertDictEqual(ratios.float_to_ratio([8/60, 10/60, 8/60, 7/60]), [8, 10, 8, 7]) 

class TestWhole(unittest.TestCase):
    def testOxidationReduction(self):
        self.assertEqual(main.main("H2O2 + Cr = CrO3 + H2O"), "3H2O2 + 1Cr = 1CrO3 + 3H2O")
    def testLongEquation(self):
        self.assertEqual(main.main("H2O2 + KI + H2S2O3 = H2O + I2 + K2S4O6O4"), "6H2O2 + 2KI + 2H2S2O3 = 8H2O + 1I2 + 1K2S4O6O4")
    def testHydrates(self):
        self.assertEqual(main.main("CuSO4*5H2O = CuSO4 + H2O"), "1CuSO4*5H2O = 1CuSO4 + 5H2O")
    def testComplexCompounds(self):
        self.assertEqual(main.main("NH3 + CuSO4 = [Cu(NH3)4]SO4"), "4NH3 + 1CuSO4 = 1[Cu(NH3)4]SO4")
if __name__ == "__main__":
    unittest.main()
