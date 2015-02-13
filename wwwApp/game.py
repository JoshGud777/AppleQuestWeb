import library as lib

def cookie_read():
    
    cookie = lib.get_cookies()
    if cookie == None:
        print('No Cookies')
    else:
        print(cookie)
        
def main():
    lib.print_header()
    cookie_read()
    
if __name__ == '__main__':
    main()




'''
    c.execute("SELECT username FROM logon WHERE username = ?", [username])
    dbdata = c.fetchone()
    
    if not dbdata == None:
        dbusername = dbdata[0]
        if dbusername == username:
            return False
'''


    


def cookie_wright(sessionid, exp, username):
    headder()
    cookie = http.cookies.BaseCookie()
    cookie['id'] = sessionid
    cookie['exp'] = exp
    cookie['username'] = username
    print(cookie)
    print()
