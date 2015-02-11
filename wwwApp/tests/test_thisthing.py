import cgi
import platform
import sys, os
import unittest

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

class MyTestCase(unittest.TestCase):

    
    def test_nothing(self):
        pass

    def test_format(self):
        # Tests that work for only a certain version of the library.
        pass

    def test_windows_support(self):
        # windows specific testing code
        pass

if __name__ == "__main__":
    main()
    unittest.main()
