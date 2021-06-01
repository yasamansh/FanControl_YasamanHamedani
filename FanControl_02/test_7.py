# Negative- Impossible temratuer

import unittest
import Bot as b

class Test_test_Impossible(unittest.TestCase):

    def test_loadFile_Single_00(self):
        bub = b.Bot('SubSystem_nagative_00.json')
        self.assertIsNotNone(bub.LoadSubSystems())

    def test_validateTempDiff(self):
        bub = b.Bot('SubSystem_nagative_00.json')
        bub.LoadSubSystems()
        min = bub.GetMinTemp()
        max = bub.GetMaxTemp()
        self.assertGreater(50, abs(max - min), 'The diffrence of max and Min more that 50, impossible!')

    def test_validateMin(self):
        bub = b.Bot('SubSystem_nagative_00.json')
        bub.LoadSubSystems()
        min = bub.GetMinTemp()
        self.assertLess(  -10, min,'Temprature Too low, Impossible!')

    def test_validateMax(self):
        bub = b.Bot('SubSystem_nagative_00.json')
        bub.LoadSubSystems()
        max = bub.GetMaxTemp()
        self.assertGreater(max, 100, 'Temprature Too hight, Impossible!')

if __name__ == '__main__':
    unittest.main()