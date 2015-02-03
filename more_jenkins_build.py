import cgi
import platform
import sys, os
import unittest

# import ChessWWW.cgi as cgi
import wwwApp.elo as elo
# import ChessWWW.index as index

def main():
    print()
    print('Test:')
    print('**************************************************')
    print("Jenkins Build File: " + os.path.basename(sys.argv[0]))
    print("Elo.py, FIX - TESTS NO LONGER VALID")
    print()
    
    print("sys.version: \n" + sys.version)
    print()
    
    print("Python Playform \n" + platform.python_version())
    print('**************************************************')


'''class TestEloFunctions(unittest.TestCase):
Remake Tests!
    def test_elo_cal0(self):
        self.assertEqual(elo.cal(1, 1, 1), 0.1)

    def test_elo_cal1(self):
        self.assertEqual(elo.cal(15, 99, 75, k=100), 85.5)

    def test_elo_cal2(self):
        self.assertEqual(elo.cal(50, 82, 79), 521.4)
        
    def test_elo_cal3(self):
        self.assertEqual(elo.cal(1000, 1200, 99, k=8947), 24.34335531463060243)

    def test_elo_cal4(self):
        self.assertRaises(ZeroDivisionError, elo.cal, 12, 12, 3, k=0)

    def test_elo_est5(self):
        self.assertEqual(elo.est(1, 1), (50, 50))
        
    def test_elo_est6(self):
        self.assertEqual(elo.est(1000, 1200), (24.025, 75.975))
        
    def test_elo_est7(self):
        self.assertEqual(elo.est(1325, 4655), (0, 100))
        
    def test_elo_est8(self):
        self.assertEqual(elo.est(1200, 1300),(35.994, 64.006))
        
    def test_elo_est9(self):
        self.assertEqual(elo.est(1254, 1321), (elo.est(1254, 1321)[0],
                                           elo.est(1254, 1321)[1]))'''

if __name__ == "__main__":
    main()
    unittest.main()
