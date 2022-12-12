import calc
import unittest
from random import randint

class TestCalc(unittest.TestCase):
    def test_plus(self):
        a = randint(1,100)
        b = randint(1,100)
        self.assertEqual(calc.plus(a,b), a+b)
    def test_minus(self):
        a = randint(1,100)
        b = randint(1,100)
        self.assertEqual(calc.minus(a,b), a-b)
    def test_devide(self):
        a = randint(1,100)
        b = randint(1,100)
        self.assertEqual(calc.devide(a,b), a/b)
    def test_multiply(self):
        a = randint(1,100)
        b = randint(1,100)
        self.assertEqual(calc.multiply(a,b), a*b)    
if __name__ == '__main__':        
    unittest.main()
