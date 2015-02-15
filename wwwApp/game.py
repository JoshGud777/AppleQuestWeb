import library as lib
import cgitb
cgitb.enable()

def html(value='', print_data=''):
    if print_data != '':
        print_data = '<p>' + print_data + '</p>'
    else:
        print_data = '<!--Print data goes here, if there is any-->'
        
    print('''<!DOCTYPE HTML>
<html lang="en">
<head>
<meta http-equiv="content-type" content="text/html; charset=utf-8">
<title>AppleQuest - Game</title>
</head>
<body>
''' + print_data + '''
<form action="game.py">
Command: 
<input type="text" name="command" value="''' + value + '''">
<br><br>
<input type="submit" value="Submit">
</form>
</body>
</html>''')

def cookie_read():
    cookie = lib.get_cookies()
    if cookie == None:
        print('<!-- No Cookies -->')
    else:
        print('<!-- ', end="")
        print(cookie + "     |     ", end="")
        print('-->')
        
def main(x):
    lib.print_header()
    cookie_read()
    form = lib.get_cgi_data()
    x = form.getfirst("command")
    if x == None:
        x = ''
    elif type(x) != str:
        x = str(x)
    html(x)
    
if __name__ == '__main__':
    main()
