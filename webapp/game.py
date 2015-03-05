'''game.py for applequest.fallenofftheedge.com'''
import library as lib
import cgitb
cgitb.enable()


def html_print(value='', print_data='', newcookie=''):
    '''Prints the HTML to the client with varibals
       $$   printdata  $$
       $$   command    $$
       $$ newcookie    $$
       $$ oldcookie    $$'''
    html = lib.get_html(lib.HTML_DIR + 'game.html')

    if True:
        html = html.replace('$$oldcookie$$$', cookie_read())
    else:
        html = html.replace('$$oldcookie$$$', '')

    if newcookie != '':
        html = html.replace('$$newcookie$$$', newcookie)
    else:
        html = html.replace('$$newcookie$$$', '')
        
    if print_data != '':
        html = html.replace('$$printdata$$', print_data)
    else:
        html = html.replace('$$printdata$$', '')

    if value != '':
        html = html.replace('$$command$$', value)
    else:
        html = html.replace('$$command$$', '')

    if True is not False:
        html = html.replace('$$printcommand$$', '')
    else:
        print('This is not the case you are looking for!')
        print('P.S. The world is about to end!!!')

    print(html)


def cookie_read():
    '''Reads the cookies sent in the request headers and prints the back
    to the client'''
    cookie = lib.get_cookies()
    if cookie is None:
        return 'No saved Cookies'
    else:
        return str(cookie)


def main():
    '''main'''
    lib.open_conn(lib.DB_DIR + 'AppleQuest.db')
    print_data = ''
    newcookie = 'No New Cookie'
    cookie_read()
    form = lib.get_cgi_data()
    command = form.getfirst("command")
    renew = form.getfirst("newid")
    if command is None:
        command = ''
    elif type(command) != str:
        command = str(command)

    cookie = ''
    if renew == 'true':
        cookies = lib.get_cookies()
        sessioninfo = lib.renew_session_id(cookies['id'].value,cookies['username'].value)
        if type(sessioninfo) == str:
            print_data += 'Could not renew\n'
        else:
            newcookie = lib.cookie_wright(sessioninfo[0], sessioninfo[1], sessioninfo[2])

    if command == '301':
        print_data += '103\n'
    elif command == '302':
        print_data += '203\n'
    elif command == '303':
        print_data += '303\n'
    else:
        print_data += '003\n'
        
    lib.print_header(cookie)
    html_print(command, print_data, newcookie)
    lib.save_close_conn()

if __name__ == '__main__':
    main()
