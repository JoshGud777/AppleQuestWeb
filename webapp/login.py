'''
Login script
'''
import library as lib
import cgitb
cgitb.enable()


def html():
    '''Prints all the HTML for the page.'''
    print('''<!DOCTYPE html>
<html>
<body>
<form action="/login.py" method="POST">
First name:<br>
<input type="text" name="username">
<br>
Last name:<br>
<input type="password" name="password">
<br><br>
<input type="hidden" name="key" value="send_login">
<input type="submit" value="Submit">
</form>
</body>
</html>''')


def main():
    '''main - takes imput from user and issues session id for that user'''
    lib.open_conn(lib.DB_DIR + 'AppleQuest.db')
    form = lib.get_cgi_data()
    if form.getvalue('key') == 'send_login':
        username = form['username'].value
        password = form['password'].value

        sessionid, exp, username = lib.issue_session_id(username, password)

        cookie = lib.cookie_wright(sessionid, exp, username)

        lib.print_header(cookie=cookie)
        lib.print_me(lib.REDIRECT_DIR + 'to_game.html')
    else:
        lib.print_header()
        html()

    lib.close_conn()


if __name__ == '__main__':
    main()
