import sqlite3
import time
import os
import http.cookies as cookie
import hashlib
import binascii

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
                c.execute("INSERT INTO sessions VALUES (?, ?, ?)", (sessionid, exp, username))
                sqlgood = True
            except:
                sqlretry += 1
                if sqlretry == 10:
                    return ('sqlerror, sqlerror')
                
        return (sessionid, exp)
    
    return ('noauth', 'noauth')

def renew_session_id(old_id, username):
    c.execute("SELECT * FROM sessions WHERE username =  ? AND id = ?", [username, old_id])
    dbdata = c.fetchone()

    db_exp = int(dbdata[1])
    if dbdata == None:
        pass
    print(int(time.time()))
    print(db_exp)
    if int(time.time()) > db_exp:
        return ('expired', 'expired')
    if int(time.time()) <= db_exp:
        return ('new_id', 'new_exp')

def delete_session():
    pass

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

if __name__ == '__main__':
    open_conn('ex.db')
    print('OPENED CONNECTION TO \'ex.db\'',)
    
