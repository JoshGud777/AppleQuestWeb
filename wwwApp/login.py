import binascii
import cgi
import hashlib
import http.cookies
import os
import sqlite3
import time

HTML_DIR = 'html\\'
DIR_REDIRECT = 'html\\redirect\\'

def open_conn(db):
    global conn, c
    conn = sqlite3.connect(db)
    c = conn.cursor()

def issue_session_id(username, pword):
    username = username.lower()
    authuser = check_user(username, pword)
    if authuser == True:

        sqlretry = 0
        sqlgood = False
        while sqlgood == False:
            c.execute("SELECT * FROM logon WHERE username = ?", [username])
            dbdata = c.fetchone()
            db_username = dbdata[0]
            db_display = dbdata[1]

            exp = int(time.time()) + 300 # seconds till this is expired | 300 = 5 min | 1 = 1 sec
            sessionid = binascii.hexlify(os.urandom(16)).decode("utf-8")

            try:
                c.execute("DELETE FROM sessions WHERE username = ?", [username])
                c.execute("INSERT INTO sessions VALUES (?, ?, ?)", [sessionid, exp, username])
                sqlgood = True
            except:
                sqlretry += 1
                if sqlretry == 10:
                    return ('sqlerror, sqlerror')
                
        return (sessionid, exp, username)
    
    return ('noauth', 'noauth')

def check_user(username, pword):
    username = username.lower()
    c.execute("SELECT username, password, salt FROM logon WHERE username = ?", [username])
    dbdata = c.fetchone()

    if dbdata == None:
          return None
        
    enchexpassdb = dbdata[1]
    
    salt = dbdata[2]
    utf8pword = pword.encode('utf8')
    utf8pword_salt = utf8pword + salt

    hashed_salted_password = hashlib.sha512(utf8pword_salt)
    enchexpass = hashed_salted_password.hexdigest()

    
    if slow_equal(enchexpassdb, enchexpass):
        return True
    else:
        return False

def slow_equal(a, b):
    length = 0
    equal = 0
    
    if len(a) == len(b):
        length = len(a)
        equal = 0
    else:
        time.sleep(1)
        length = 0
        equal = 1000
 
    for i in range(length):
        if a[i] != b[i]:
            equal += 1

        if equal == 0:
            return True
        else:
            return False

def close():
    conn.close()

def cookie_wright(sessionid, exp, username):
    headder()
    cookie = http.cookies.BaseCookie()
    cookie['id'] = sessionid
    cookie['exp'] = exp
    cookie['username'] = username
    print(cookie)
    print()

def print_me(filename):
    f = open(filename, 'r')

    for line in f:
        print(line, end=' ')
    f.close

def print_header():
    print('Content-type: text/html\n')

def get_cgi_data():
    cgidata = cgi.FieldStorage()
    return cgidata

def main():
    print_header()
    form = get_cgi_data()
    if form.getvalue('key') == 'send_login':
        print_me(DIR_REDIRECT + 'to_game.html')
    else:
        print_me(HTML_DIR + 'login0.html')
        print_me(HTML_DIR + 'login1.html')
                
if __name__ == '__main__':
    main()
