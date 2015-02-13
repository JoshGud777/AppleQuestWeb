import library as lib

def main():
    form = lib.get_cgi_data()
    if form.getvalue('key') == 'send_login':
        username = form['username'].value
        password = form['password'].value

        sessionid, exp, username = lib.issue_session_id(username, password)

        cookie = cookie_wright(sessionid, exp, username)

        print_header(cookie=cookie)
        lib.print_me(lib.REDIRECT_DIR + 'to_game.html')
    else:
        lib.print_header()
        lib.print_me(lib.HTML_DIR + 'login0.html')
        lib.print_me(lib.HTML_DIR + 'login1.html')
        
if __name__ == '__main__':
    main()
