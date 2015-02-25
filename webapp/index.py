'''index page of applequest.fallenofftheedge.com'''
import cgi


def html():
    '''Prints the html to the client with any data we want added'''
    print('''<html>

<head>
  <title></title>
</head>

<body>
<h1>Elo Calculator!</h1>
<form name="elocal" method="get" action="index.py">
<table width="auto">
<tr>
<td valign="top">
<label for="player_a">Player A Starting Score *</label>
</td>
<td valign="top">
<input type="text" name="player_a" maxlength="50" size="30">
</td>
</tr>

<tr>
<td valign="top">
<label for="player_b">Player B Starting Score *</label>
</td>
<td valign="top">
<input type="text" name="player_b" maxlength="50" size="30">
</td>
</tr>

<tr>
<td>
<label for="win">K value (Game Weight)</label>
  </td>
  <td valign="top">
  <select name="k" value="20">
  <option value="20">Defualt-20</option>
  <option value="40">40</option>
  <option value="30">30</option>
  <option value="20">20</option>
  <option value="15">15</option>
  <option value="10">10</option>
  </select>
  </td>
</tr>

<tr>
<td colspan="2" style="text-align:center">
<input type="submit" value="Submit">
</td>
</tr>
</table>
</form>
</body>
</html>
''')


def print_header():
    '''HTTP Headder for CGI'''
    print("Content-type: text/html")
    print()


def get_form():
    '''gets the cgi data from the client and
    returns it to us'''
    form = cgi.FieldStorage()
    return form


def main():
    '''Main'''
    print_header()
    html()


if __name__ == '__main__':
    main()