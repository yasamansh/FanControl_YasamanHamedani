## Single validateion

import unittest
import Bot as b

class Test_test_single(unittest.TestCase):

    def test_loadFile_Single_00(self):
        bub= b.Bot('SubSystem_Single_00.json')
        self.assertIsNotNone(bub.LoadSubSystems())

    def test_validatePWM_Single_00(self):
        bub = b.Bot('SubSystem_Single_00.json')
        bub.LoadSubSystems()
        maxTemp = bub.GetMaxTemp()
        PWM = bub.getPWMs()[0]
        if (maxTemp < 25):
            return self.assertEqual(PWM, 0)
        if (maxTemp > 75):
            return self.assertEqual(PWM, 100)
        else:
            return self.assertEqual(PWM, round((maxTemp - 25) * 2,2))

    def test_loadFile_Single_01(self):
        bub= b.Bot('SubSystem_Single_01.json')
        self.assertIsNotNone(bub.LoadSubSystems())

    def test_validatePWM_Single_01(self):
        bub = b.Bot('SubSystem_Single_01.json')
        bub.LoadSubSystems()
        maxTemp = bub.GetMaxTemp()
        PWM = bub.getPWMs()[0]
        if(maxTemp < 25):
            return self.assertEqual(PWM, 0)
        if (maxTemp > 75):
            return self.assertEqual(PWM, 100)
        else:
            return self.assertEqual(PWM, round((maxTemp - 25) * 2,2))

    def test_loadFile_Single_02(self):
        bub= b.Bot('SubSystem_Single_02.json')
        self.assertIsNotNone(bub.LoadSubSystems())

    def test_validatePWM_Single_0(self):
        bub = b.Bot('SubSystem_Single_02.json')
        bub.LoadSubSystems()
        maxTemp = bub.GetMaxTemp()
        PWM = bub.getPWMs()[0]
        if(maxTemp < 25):
            return self.assertEqual(PWM, 0)
        if (maxTemp > 75):
            return self.assertEqual(PWM, 100)
        else:
            return self.assertEqual(PWM, round((maxTemp - 25) * 2,2))


    def test_loadFile_Single_03(self):
        bub= b.Bot('SubSystem_Single_03.json')
        self.assertIsNotNone(bub.LoadSubSystems())

    def test_validatePWM_Single_03(self):
        bub = b.Bot('SubSystem_Single_03.json')
        bub.LoadSubSystems()
        maxTemp = bub.GetMaxTemp()
        PWM = bub.getPWMs()[0]
        if(maxTemp < 25):
            return self.assertEqual(PWM, 0)
        if (maxTemp > 75):
            return self.assertEqual(PWM, 100)
        else:
            return self.assertEqual(PWM, round((maxTemp - 25) * 2,2))


    def test_loadFile_Single_04(self):
        bub= b.Bot('SubSystem_Single_04.json')
        self.assertIsNotNone(bub.LoadSubSystems())

    def test_validatePWM_Single_04(self):
        bub = b.Bot('SubSystem_Single_04.json')
        bub.LoadSubSystems()
        maxTemp = bub.GetMaxTemp()
        PWM = bub.getPWMs()[0]
        if(maxTemp < 25):
            return self.assertEqual(PWM, 0)
        if (maxTemp > 75):
            return self.assertEqual(PWM, 100)
        else:
            return self.assertEqual(PWM, round((maxTemp - 25) * 2,2))


    def test_loadFile_Single_05(self):
        bub= b.Bot('SubSystem_Single_05.json')
        self.assertIsNotNone(bub.LoadSubSystems())

    def test_validatePWM_Single_05(self):
        bub = b.Bot('SubSystem_Single_05.json')
        bub.LoadSubSystems()
        maxTemp = bub.GetMaxTemp()
        PWM = bub.getPWMs()[0]
        if(maxTemp < 25):
            return self.assertEqual(PWM, 0)
        if (maxTemp > 75):
            return self.assertEqual(PWM, 100)
        else:
            return self.assertEqual(PWM, round((maxTemp - 25) * 2,2))


    def test_loadFile_Single_06(self):
        bub= b.Bot('SubSystem_Single_06.json')
        self.assertIsNotNone(bub.LoadSubSystems())

    def test_validatePWM_Single_06(self):
        bub = b.Bot('SubSystem_Single_06.json')
        bub.LoadSubSystems()
        maxTemp = bub.GetMaxTemp()
        PWM = bub.getPWMs()[0]
        if(maxTemp < 25):
            return self.assertEqual(PWM, 0)
        if (maxTemp > 75):
            return self.assertEqual(PWM, 100)
        else:
            return self.assertEqual(PWM, round((maxTemp - 25) * 2,2))

    def test_loadFile_Single_07(self):
        bub= b.Bot('SubSystem_Single_07.json')
        self.assertIsNotNone(bub.LoadSubSystems())

    def test_validatePWM_Single_07(self):
        bub = b.Bot('SubSystem_Single_07.json')
        bub.LoadSubSystems()
        maxTemp = bub.GetMaxTemp()
        PWM = bub.getPWMs()[0]
        if(maxTemp < 25):
            return self.assertEqual(PWM, 0)
        if (maxTemp > 75):
            return self.assertEqual(PWM, 100)
        else:
            return self.assertEqual(PWM, round((maxTemp - 25) * 2,2))

    def test_loadFile_Single_08(self):
        bub= b.Bot('SubSystem_Single_08.json')
        self.assertIsNotNone(bub.LoadSubSystems())

    def test_validatePWM_Single_08(self):
        bub = b.Bot('SubSystem_Single_08.json')
        bub.LoadSubSystems()
        maxTemp = bub.GetMaxTemp()
        PWM = bub.getPWMs()[0]
        if(maxTemp < 25):
            return self.assertEqual(PWM, 0)
        if (maxTemp > 75):
            return self.assertEqual(PWM, 100)
        else:
            return self.assertEqual(PWM, round((maxTemp - 25) * 2,2))


if __name__ == '__main__':
    unittest.main()