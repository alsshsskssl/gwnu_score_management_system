import io
import unittest
from unittest import TestCase

class MyTest(TestCase):
    def test_constructor(self):
        fp = io.open("score.csv","r",encoding = "utf-8")
        raw_value = fp.readlines()
        
        sum = list()
        avg = list()
        self.asserIsNotNone(sum)

        for i in range(len(raw_value)):
            std = raw_value[i].split(",")
            sum.append(int(std[2])+int(std[3])+int(std[4]))
            avg.append(round(sum[i]/3,3))   #평균

        rank = list()
        for value in sum:
            r=1
            for value2 in sum:
                if value < value2:
                    r += 1
            rank.append(r)

        fp.close()

if(__name__=="__main__"):
    unittest.main()
            
