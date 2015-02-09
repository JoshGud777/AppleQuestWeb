import binascii
import cgi
import hashlib
import http.cookies as cookie
import os
import sqlite3
import time

def open_conn(db):
    global conn, c
    conn = sqlite3.connect(db)
    c = conn.cursor()


def add_user(username, pword, email=None):
    display = username[:]
    username = username.lower()
    
    salt = binascii.hexlify(os.urandom(64)) #64 bytes = 512 bits
    utf8pword = pword.encode("utf-8")
    utf8pword_salt = utf8pword + salt

    hashed_salted_password = hashlib.sha512(utf8pword_salt)
    enchexpass = hashed_salted_password.hexdigest()
    try:
        c.execute("INSERT INTO logon VALUES (?, ?, ?, ?, ?)", (username, display, enchexpass, salt, email))
    except:
        return False
    return True

'''
    c.execute("SELECT username FROM logon WHERE username = ?", [username])
    dbdata = c.fetchone()
    
    if not dbdata == None:
        dbusername = dbdata[0]
        if dbusername == username:
            return False
'''
    

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
            sessionid = binascii.hexlify(os.urandom(512)).decode("utf-8")

            try:
                c.execute("DELETE FROM sessions WHERE username = ?", [username])
                c.execute("INSERT INTO sessions VALUES (?, ?, ?)", [sessionid, exp, username])
                sqlgood = True
            except:
                sqlretry += 1
                if sqlretry == 10:
                    return ('sqlerror, sqlerror')
                
        return (sessionid, exp)
    
    return ('noauth', 'noauth')

def renew_session_id(old_id, username):
    username = username.lower()
    c.execute("SELECT * FROM sessions WHERE username =  ? AND id = ?", [username, old_id])
    dbdata = c.fetchone()
    if dbdata == None:
        return False
    db_exp = int(dbdata[1])
    
    print(int(time.time()))
    print(db_exp)
    if int(time.time()) > db_exp:
        return ('expired', 'expired')
    elif int(time.time()) <= db_exp:
        sqlgood = False
        sqlretry = 0
        while sqlgood == False:
            exp = int(time.time()) + 300 # seconds till this is expired | 300 = 5 min | 1 = 1 sec
            sessionid = binascii.hexlify(os.urandom(512)).decode("utf-8")
            try:
                c.execute("DELETE FROM sessions WHERE username = ?", [username])
                c.execute("INSERT INTO sessions VALUES (?, ?, ?)", [sessionid, exp, username])
                sqlgood = True
            except:
                sqlretry += 1
                if sqlretry == 10:
                    return ('sqlerror, sqlerror')
                    
        return (sessionid, exp)
    

def delete_session(sessionid, username):
    username = username.lower()
    c.execute("SELECT * FROM sessions WHERE username = ? OR id = ?", [username, sessionid])
    dbdata = c.fetchone()
    if dbdata == None:
        return True


    c.execute("DELETE FROM sessions WHERE username = ? OR id = ?", [username, sessionid])

    return True

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

def save():
    conn.commit()

def save_close():
    conn.commit()
    conn.close()

def close():
    conn.close()

def cookie():
    print "Content-type: text/plain\n"

if "HTTP_COOKIE" in os.environ:
    print os.environ["HTTP_COOKIE"]
else:
    print "HTTP_COOKIE not set!"


if __name__ == '__main__':
    cookie()
    #open_conn('AppleQuest.db')
    #print('OPENED CONNECTION TO \'AppleQuest.db\'',)
    
