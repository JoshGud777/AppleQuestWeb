import cgi
import platform
import sqlite3
import sys
import os
import unittest
import time
from webapp import library as lib


def main():
    print('''
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Jenkins Test File: ''' + os.path.basename(sys.argv[0]) + '''
**************************************************
Test File(s):
Library.py
''')


class VarsTestCase(unittest.TestCase):

    def test_HTML_DIR(self):
        self.assertEqual(lib.HTML_DIR, 'html\\')

    def test_DB_DIR(self):
        last2 = lib.DB_DIR[-3:]
        first2 = lib.DB_DIR[0:2]
        backandfrount = first2 + last2
        self.assertEqual(backandfrount, 'dbdb\\')

    def test_REDIRECT_DIR(self):
        self.assertEqual(lib.REDIRECT_DIR, 'redirect\\')


class ConnTestCase(unittest.TestCase):

    def test_open_conn(self):
        global conn
        global c
        lib.open_conn('db.db')
        self.assertEqual(os.path.isfile('db.db'), True)
        self.assertEqual(type(lib.conn), sqlite3.Connection)
        self.assertEqual(type(lib.c), sqlite3.Cursor)
        lib.close_conn()
        os.remove('db.db')
        self.assert

if __name__ == "__main__":
    main()
    unittest.main()
