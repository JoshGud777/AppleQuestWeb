'''game.py for applequest.fallenofftheedge.com'''
import library as lib
import cgitb
cgitb.enable()


def html(value='', print_data=''):
    '''Prints the HTML to the client with varibals'''
    html = lib.get_html(lib.HTML_DIR + 'game.html')
    if print_data != '':
        print_data = '<p>' + print_data + '</p>'
    else:
        print_data = '<!--Print data goes here, if there is any-->'

    print(html)


def cookie_read():
    '''Reads the cookies sent in the request headers and prints the back
    to the client'''
    cookie = lib.get_cookies()
    if cookie is None:
        print('<!-- No Cookies -->')
    else:
        print('<!-- ', end="")
        print(cookie, end="")
        print('-->')


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
    html(command, print_data)

if __name__ == '__main__':
    main()