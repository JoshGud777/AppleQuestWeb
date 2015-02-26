'''
Login script
'''
import library as lib
import cgitb
cgitb.enable()


def html(error=''):
    '''Prints all the HTML for the page.'''
    html = lib.get_html(lib.HTML_DIR + 'login.html')
    if error != '':
        error = str(error)
        html = html.replace('$$ERROR', error)
    else:
        html = html.replace('$$ERROR$$', '')
    print(html)

def main():
    '''main - takes imput from user and issues session id for that user'''
    lib.open_conn(lib.DB_DIR + 'AppleQuest.db')
    form = lib.get_cgi_data()
    if form.getvalue('key') == 'send_login':
        username = form['username'].value
        password = form['password'].value

        session_info = lib.issue_session_id(username, password)
        if session_info[0] == 'noauth':
            lib.print_header()
            error = '!!! Invalid Username OR Password !!!'
            html(error)
            
        elif session_info[0] == 'sqlerror':
            lib.print_header()
            error = 'Internal SQL error. </br> Please e-mail servgud777@gmail.com!'
            html(error)
            
        elif username == session_info[2]:
            sessionid, exp, username = session_info
            cookie = lib.cookie_wright(sessionid, exp, username)
            lib.print_header(cookie=cookie)
            lib.print_me(lib.REDIRECT_DIR + 'to_game.html')
        else:
            lib.print_header()
            error = 'Internal SERVER error. </br> Please e-mail servgud777@gmail.com!'
            html(error)
            
    else:
        lib.print_header()
        html()

    lib.close_conn()


if __name__ == '__main__':
    main()
