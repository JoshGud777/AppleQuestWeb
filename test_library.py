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


class VarsTestCase(unittest.TestCase): # Global Varibales

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

    def test_open_conn_and_close_conn(self):  # Function 1 & 4
        lib.open_conn('db.db')
        self.assertEqual(os.path.isfile('db.db'), True, 'Could not create and connect to database')
        self.assertEqual(type(lib.conn), sqlite3.Connection, 'Is not sqlite3.Connection obj')
        self.assertEqual(type(lib.c), sqlite3.Cursor, 'Is not sqlite3.Cursor obj')
        lib.close_conn()
        os.remove('db.db')
        self.assertEqual(os.path.isfile('db.db'), False, 'Could not delete file')

    def test_get_cgi_data(self):
        os.environ["REQUEST_METHOD"] = "GET"
        os.environ["QUERY_STRING"] = "key0=data0&key1=data1&key2=data2"

        form = lib.get_cgi_data()
        key0data, key1data, key2data = form['key0'].value, form['key1'].value, form['key2'].value

        self.assertEqual(key0data, 'data0')
        self.assertEqual(key1data, 'data1')
        self.assertEqual(key2data, 'data2')
        
if __name__ == "__main__":
    main()
    unittest.main()
