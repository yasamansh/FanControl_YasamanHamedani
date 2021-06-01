## 25 - 50

import unittest
import Bot as b

class Test_test_01(unittest.TestCase):

    def test_loadFile(self):
        bub= b.Bot('SubSystem_01.json')
        self.assertIsNotNone(bub.LoadSubSystems())
        # Not necessary
    def test_getTempOfOneSS(self):
        bub = b.Bot('SubSystem_01.json')
        bub.LoadSubSystems()
        self.assertEqual(bub.getTempOfOneSS(1),25)

    def test_CountLoadedSubSys(self):
        bub = b.Bot('SubSystem_01.json')
        bub.LoadSubSystems()
        self.assertEqual(bub.CountLoadedSubSys(), 51)

    def test_validateMaxTemp(self):
        bub = b.Bot('SubSystem_01.json')
        bub.LoadSubSystems()
        self.assertEqual(bub.GetMaxTemp(),50)

    def test_SolidPWM(self):
        bub = b.Bot('SubSystem_01.json')
        bub.LoadSubSystems()
        PWM = []
        PWM = bub.getPWMs()
        return all(x == PWM[0] for x in PWM)
    #Necassary
    def test_validatePWM(self):
        bub = b.Bot('SubSystem_01.json')
        bub.LoadSubSystems()
        maxTemp = bub.GetMaxTemp()
        PWM = bub.getPWMs()[0]
        if(maxTemp < 25):
            self.assertEqual(PWM, 0)
        if (maxTemp > 75):
            self.assertEqual(PWM, 100)
        else:
            self.assertEqual(PWM, (maxTemp - 25) * 2)

    def test_getPMWVariable(self):
        bub = b.Bot('SubSystem_00.json')
        bub.LoadSubSystems()
        PWMVariiable = bub.getPMWVariable()
        SubTemp = bub.GetMaxTemp()
        if(SubTemp < 25):
            self.assertEqual(PWMVariiable, 0)
        if (SubTemp > 75):
            self.assertEqual(PWMVariiable, 100)
        else:
            self.assertEqual(PWMVariiable, (SubTemp - 25) * 2)
if __name__ == '__main__':
    unittest.main()
