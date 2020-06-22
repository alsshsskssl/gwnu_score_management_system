import io
import unittest
from unittest import TestCase

class MyTest(TestCase):
    def test_constructor(self):
        fp = io.open("score.csv","r",encoding = "utf-8")
        raw_value = fp.readlines()
        self.assertIsNotNone(sum)   #unittest
        sum = list()
        avg = list()
        self.assertIsNotNone(sum)   #unittest

        for i in range(len(raw_value)):
            std = raw_value[i].split(",") 
            sum.append(int(std[2])+int(std[3])+int(std[4]))
            avg.append(round(sum[i]/3,3))

        rank = list()
        for value in sum:
            r = 1
            for value2 in sum:
                if value < value2:
                    r += 1
            rank.append(r)

        fp.close()
        with io.open("result.csv","w",encoding = "utf-8") as fw:
            for i in range(len(raw_value)):
                fw.write(raw_value[i].replace('\n','')+',')
                fw.write(sum[i].__str__()+',')
                fw.write(avg[i].__str__()+',')
                fw.write(rank[i].__str__()+'\n')
        self.assertEqual(1,2)   #unittest
        
if(__name__=="__main__"):
    unittest.main()
