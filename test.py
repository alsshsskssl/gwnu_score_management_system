import io
import unittest
from unittest import TestCase

class MyTest(TestCase):
    def test_constructor(self):
        fp = io.open("score.csv","r",encoding = "utf-8")
        raw_value = fp.readlines()

if(__name__=="__main__"):
    unittest.main()
            
