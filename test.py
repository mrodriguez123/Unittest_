import unittest
import main
import pytest

class TestMain(unittest.TestCase):
    
    #testing each individual function
    # this only counts as 1 test, no matter how many assertions
    def test_add(self): 
        self.assertEqual(main.add(3,2), 5)
        self.assertEqual(main.add(-1,1), 0)
        self.assertEqual(main.add(-3,-2), -5)

        
    def test_mult(self): 
        self.assertEqual(main.mult(3,2), 6)
        self.assertEqual(main.mult(-1,1), -1)
        self.assertEqual(main.mult(-1,0), 0)
    
    def test_div(self): 
        self.assertEqual(main.div(6,2), 3)
        self.assertEqual(main.div(-1,1), -1)
        self.assertEqual(main.div(2,4), 1/2)
        #to check for value error:
        with self.assertRaises(ValueError):
            main.div(3,0)
        
    def test_exp(self): 
        self.assertEqual(main.exp(3,2), 9)
        self.assertEqual(main.exp(-1,2), 1)
        self.assertEqual(main.exp(2,-2), 1/4)
        self.assertEqual(main.exp(2,0), 1)

        
# python sets name variable to be "main" when ran directly 

if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)
    
# need the exit to be False- 
# https://stackoverflow.com/questions/40172281/unit-tests-for-functions-in-a-jupyter-notebook

