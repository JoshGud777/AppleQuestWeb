def print_me(filename):
    f = open(filename, 'r')

    for line in f:
        print(line, end=' ')
    f.close

def main():
    print("Content-type: text/html")
    print()
    print('GAME.HTML')
    
if __name__ == '__main__':
    main()



def delete_session(sessionid, username):
    username = username.lower()
    c.execute("SELECT * FROM sessions WHERE username = ? OR id = ?", [username, sessionid])
    dbdata = c.fetchone()
    if dbdata == None:
        return True

    c.execute("DELETE FROM sessions WHERE username = ? OR id = ?", [username, sessionid])
    return True


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
    


def cookie_wright(sessionid, exp, username):
    headder()
    cookie = http.cookies.BaseCookie()
    cookie['id'] = sessionid
    cookie['exp'] = exp
    cookie['username'] = username
    print(cookie)
    print()