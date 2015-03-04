'''game.py for applequest.fallenofftheedge.com'''
import library as lib
import cgitb
cgitb.enable()


def html_print(value='', print_data=''):
    '''Prints the HTML to the client with varibals
       $$   printdata  $$
       $$   command    $$
       $$ printcommand $$'''
    html = lib.get_html(lib.HTML_DIR + 'game.html')

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

    print(cookie_read())
    print(html)


def cookie_read():
    '''Reads the cookies sent in the request headers and prints the back
    to the client'''
    cookie = lib.get_cookies()
    if cookie is None:
        return '<!-- No Cookies -->'
    else:
        returndata = '<!--\n'
        returndata += str(cookie)
        retundata += '-->'

    return returndata


def main():
    '''main'''
    lib.print_header()
    cookie_read()
    form = lib.get_cgi_data()
    command = form.getfirst("command")
    print_data = form.getfirst("print")
    if command is None:
        command = ''
    elif type(command) != str:
        command = str(command)

    if print_data is None:
        print_data = ''
    elif type(print_data) != str:
        print_data = str(print_data)
    html_print(command, print_data)

if __name__ == '__main__':
    main()
