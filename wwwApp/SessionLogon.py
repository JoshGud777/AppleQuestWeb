import binascii
import cgi
import hashlib
import http.cookies
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
                    
        return (sessionid, exp, username)
    

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

def cookie_read():
    
    if "HTTP_COOKIE" in os.environ:
        cookies = http.cookies.BaseCookie()
        cookies.load(os.environ["HTTP_COOKIE"])
        y = cookies['id'].value
        x = cookies['exp'].value
        z = cookies['username'].value
        print('<br>')
        print('<br>')
        print('Your Cookie data:')
        print('<p>old session id: ' + y +'</p>')
        print('old exp: ' + x)
        print('<br>')
        print('old userename: ' + z)
        print('<br>')
    else:
        print ("HTTP_COOKIE not set!")

def cookie_wright(sessionid, exp, username):
    headder()
    cookie = http.cookies.BaseCookie()
    cookie['id'] = sessionid
    cookie['exp'] = exp
    cookie['username'] = username
    print(cookie)
    print()

def get_cgi_data():
    cgidata = cgi.FieldStorage()
    return cgidata

def headder():
    print("Content-type: text/html")
    

def print_html_start():
    print('''
          <html>
          <form action="SessionLogon.py" method="POST">
          Username 0:<br>
          <input type="text" name="username0">
          <br>
          Password 1:<br>
          <input type="password" name="password1">
          <br>
          <input type="hidden" name="key" value="send">
          <input type="submit" value="Submit">
          </form>
          ''')
    
def print_html_end(x):
    print("</html>")
          
def main():
    form = get_cgi_data()
    username = form.getvalue('username0')
    pword = form.getvalue('password1')
    if username == None:
        username = 'None'
    if pword == None:
        pword = 'None'
    open_conn('AppleQuest.db')
    
    try:
        data = issue_session_id(username, pword)
        x, y, z = data
    except:
        x = data[0]
        y = data[1]
        z = 'error'
    save_close()
    if form.getvalue('key') == 'send':
        cookie_wright(x, y, z)
    print_html_start()
    print('Session ID: ' + x)
    print('<br>')
    print('Expiry: ' + str(y))
    
    cookie_read()
    print_html_end(x)

if __name__ == '__main__':
   main()
    #open_conn('AppleQuest.db')
    #print('OPENED CONNECTION TO \'AppleQuest.db\'',)
    
