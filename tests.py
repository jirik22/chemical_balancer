import unittest
import main as balancer
import ratios

#test parsing of compounds
class TestComptodict(unittest.TestCase):
    def test_Coplex_Compounds(self): 
        self.assertDictEqual(balancer.comp_to_dict("K2[CrO4]2"), {'K': 2, 'Cr': 2, 'O': 8})
        
    def test_case_sensitivity(self):
        self.assertDictEqual(balancer.comp_to_dict("CsCS"),{'C': 1, 'Cs': 1, 'S': 1})
    
    def test_long_compounds(self):
        self.assertDictEqual(balancer.comp_to_dict("CuXeFeN5(NO3)2ClP"), {'Cu': 1, 'Xe': 1, 'Fe': 1, 'N': 7, 'O': 6, 'Cl': 1, 'P': 1})
        
    def test_multiple_didgits(self):
        self.assertDictEqual(balancer.comp_to_dict("C552He889O226"), {'C': 552, 'He': 889, 'O': 226})
        
    def test_hydrates(self):
        self.assertDictEqual(balancer.comp_to_dict("CuSO4*5H2O"), {'Cu': 1, 'S': 1, 'O': 9, 'H': 10})
             
    def test_mutliple_brackets(self):
        self.assertDictEqual(balancer.comp_to_dict("([(CaO2)3U2]2Fe5)2N"), {'Ca': 12, 'O': 24, 'U': 8, 'Fe': 10, 'N': 1 })

 
 # test function to covert float ratios to int ratios
class TestRatios(unittest.TestCase):
    def test_float_to_ratio(self):
        self.assertEqual(ratios.float_to_ratio([0.5, 0.25, 0.75]), [2, 1, 3])
                
    def test_fractions(self):
        self.assertEqual(ratios.float_to_ratio([1/3,2/3]), [1, 2])
        
    def test_long_fractions(self):
        self.assertEqual(ratios.float_to_ratio([2/53, 5/53, 8/53, 6/53, 12/53, 62/53, 154/53]), [2, 5, 8, 6, 12, 62, 154])
        
    def test_periodic_threes(self):
        self.assertEqual(ratios.float_to_ratio([8/60, 10/60, 8/60, 7/60]), [8, 10, 8, 7])
        
    def test_larger_decimals(self):
        self.assertEqual(ratios.float_to_ratio([0.125, 0.875, 0.250]), [1, 7, 2])
        
    def test_irrational(self):
        sqrt2 = 2**(1/2)
        self.assertEqual(ratios.float_to_ratio([5*sqrt2, 11*sqrt2, 4*sqrt2]), [5, 11, 4])

        
#test balancing equations
class TestWholeProgram(unittest.TestCase):
    
    def testBizzareInput(self):
        self.assertEqual(balancer.main("H2        +      O2     =     H2O"), "2H2 + O2 = 2H2O")
        
    def testOxidationReduction(self):
        self.assertEqual(balancer.main("H2O2 + Cr = CrO3 + H2O"), "3H2O2 + Cr = CrO3 + 3H2O")
        
    def testLongEquation(self):
        self.assertEqual(balancer.main("H2O2 + KI + H2S2O3 = H2O + I2 + K2S4O6O4"), "6H2O2 + 2KI + 2H2S2O3 = 8H2O + I2 + K2S4O6O4")
        
    def testHydrates(self):
        self.assertEqual(balancer.main("CuSO4*5H2O = CuSO4 + H2O"), "CuSO4*5H2O = CuSO4 + 5H2O")
        
    def testComplexCompounds(self):
        self.assertEqual(balancer.main("NH3 + CuSO4 = [Cu(NH3)4]SO4"), "4NH3 + CuSO4 = [Cu(NH3)4]SO4")  
           
    def testLongCompoudn(self):
        self.assertEqual(balancer.main("C2Ne15OPo4I8ULa12 = C + Ne + O + Po + I + U + La"), "C2Ne15OPo4I8ULa12 = 2C + 15Ne + O + 4Po + 8I + U + 12La")
         
    def testBigCofficients(self):
        self.assertEqual(balancer.main("Cu23547K8944 = Cu + K"), "Cu23547K8944 = 23547Cu + 8944K")
                    
    def testHardBalancing(self):
        self.assertEqual(balancer.main("Cu + HNO3 = CuNO3 + NO + H2O"), "3Cu + 4HNO3 = 3CuNO3 + NO + 2H2O")
        
    def testHardBalancingII(self):
        self.assertEqual(balancer.main("Zn + HNO3 = Zn(NO3)2 + H2O + N2O"), "4Zn + 10HNO3 = 4Zn(NO3)2 + 5H2O + N2O")
        
    def testHardBalancingIII(self):
        self.assertEqual(balancer.main("NH4Cl + (CuOH)2CO3 = H2O + CO2 + Cu + N2 + CuCl2"), "2NH4Cl + 2(CuOH)2CO3 = 6H2O + 2CO2 + 3Cu + N2 + CuCl2")
        
    def testHardBalancingIV(self):
        self.assertEqual(balancer.main("H2SO4 + K2Cr2O7 + KI = H2O + K2SO4 + I2 + Cr2(SO4)3"), "7H2SO4 + K2Cr2O7 + 6KI = 7H2O + 4K2SO4 + 3I2 + Cr2(SO4)3")


if __name__ == "__main__":
    unittest.main()
