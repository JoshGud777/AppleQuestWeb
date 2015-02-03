import cgi
import platform
import sys, os
import unittest

# import wwwApp.cgi as cgi
import wwwApp.elo as elo
# import wwwApp.index as index


def main():
    print()
    print('Test:')
    print('**************************************************')
    print("Jenkins Build File: " + os.path.basename(sys.argv[0]))
    print("index.py, FIX - NO TESTS")
    print()
    
    print("sys.version: \n" + sys.version)
    print()
    
    print("Python Playform \n" + platform.python_version())
    print('**************************************************')

'''class TestSequenceFunctions(unittest.TestCase):
Remake Tests!
    def test_elo0(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo1(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo2(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo3(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo4(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo5(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo6(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo7(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo8(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo9(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo10(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo11(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo12(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo13(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo14(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo15(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo16(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo17(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo18(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo19(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo20(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo21(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo22(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo23(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo24(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo25(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo26(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo27(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo28(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo29(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo30(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo31(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo32(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo33(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo34(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo35(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo36(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo37(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo38(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo39(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo40(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo41(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo42(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo43(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo44(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo45(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo46(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo47(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo48(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo49(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo50(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo51(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo52(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo53(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo54(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo55(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo56(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo57(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo58(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo59(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo60(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo61(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo62(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo63(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo64(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo65(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo66(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo67(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo68(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo69(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo70(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo71(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo72(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo73(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo74(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo75(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo76(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo77(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo78(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo79(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo80(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo81(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo82(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo83(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo84(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo85(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo86(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo87(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo88(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo89(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo90(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo91(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo92(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo93(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo94(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo95(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo96(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo97(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo98(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
    def test_elo99(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)
        '''
   
if __name__ == "__main__":
    main()
    unittest.main()
