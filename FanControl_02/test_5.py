## Change from 0 25 to 25 - 50

import unittest
import Bot as b

class Test_test_Change(unittest.TestCase):

    def test_tempChanged_00_01(self):
        bub_00 = b.Bot('SubSystem_00.json')
        bub_01 = b.Bot('SubSystem_01.json')
        bub_00.LoadSubSystems()
        bub_01.LoadSubSystems()        
        self.assertNotEqual(bub_00.getPMWVariable(),bub_01.getPMWVariable())

    def test_tempChanged_01_02(self):
        bub_00 = b.Bot('SubSystem_01.json')
        bub_01 = b.Bot('SubSystem_02.json')
        bub_00.LoadSubSystems()
        bub_01.LoadSubSystems()        
        self.assertNotEqual(bub_00.getPMWVariable(),bub_01.getPMWVariable())

    def test_tempChanged_02_03(self):
        bub_00 = b.Bot('SubSystem_02.json')
        bub_01 = b.Bot('SubSystem_03.json')
        bub_00.LoadSubSystems()
        bub_01.LoadSubSystems()        
        self.assertNotEqual(bub_00.getPMWVariable(),bub_01.getPMWVariable())

    def test_tempChanged_03_00(self):
        bub_00 = b.Bot('SubSystem_03.json')
        bub_01 = b.Bot('SubSystem_00.json')
        bub_00.LoadSubSystems()
        bub_01.LoadSubSystems()        
        self.assertNotEqual(bub_00.getPMWVariable(),bub_01.getPMWVariable())
if __name__ == '__main__':
    unittest.main()
