import cgi
import platform
import sys
import os
import unittest
import time
from wwwApp import library as lib

def main():
    print()
    print('Test:')
    print('**************************************************')
    print("Jenkins Build File: " + os.path.basename(sys.argv[0]))
    print("Library.py")
    print()
    
    print("sys.version: \n" + sys.version)
    print()
    
    print("Python Playform \n" + platform.python_version())
    print('**************************************************')


class VarsTestCase(unittest.TestCase):

    def test_HTML_DIR(self):
        self.assertEqual(lib.HTML_DIR, 'html\\') 
        pass

    def test_DB_DIR(self):
        last2 = lib.DB_DIR[-3:]
        first2 = lib.DB_DIR[0:2]
        backandfrount = first2 + last2
        self.assertEqual(backandfrount, 'dbdb\\')

    def test_REDIRECT_DIR(self):
        self.assertEqual(lib.REDIRECT_DIR, 'redirect\\')

if __name__ == "__main__":
    main()
    unittest.main()
