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
