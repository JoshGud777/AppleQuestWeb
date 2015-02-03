import cgi
import elo


def print_header():
    print("Content-type: text/html")
    print()


def print_me(filename):
    f = open(filename, 'r')

    for line in f:
        print(line, end=' ')
    f.close


def get_form():
    form = cgi.FieldStorage()
    return form


def main():
    print_header()
    print_me('index0.html')
    form = get_form()

    try:
        intError = 0
        player_a = int(form.getvalue('player_a'))
        player_b = int(form.getvalue('player_b'))
        k = int(form.getvalue('k'))
    except (ValueError, TypeError, NameError) as intError:
        pass

    if 'k' in form:
        if 'player_a' or 'player_b' in form is False:
            print("<h1>ERROR:</h1><p>Please enter a score for both "
                  "Player A and Player B </p>")
        elif intError is False:
            try:
                prob = elo.est(player_a, player_b)
                awin = elo.cal(player_a, player_b, 1, k=k)
                bwin = elo.cal(player_a, player_b, (1 - 1), k=k)
                draw = elo.cal(player_a, player_b, 0.5, k=k)
            except OverflowError:
                prob = awin = bwin = draw = ("[VALUES ARE TO LARGE]",
                                             "[VALUES ARE TO LARGE]")
            print('''<br><h1>RESULTS::</h1>
                  <p>Player A Win Prob = {}%<br>
                  Player B Win Prob = {}%<br>
                  <br>
                  Player A: Wins<br>
                  New Player A score = {}<br>
                  New Player B score = {}<br>
                  <br>
                  Player B: Wins<br>
                  New Player A score = {}<br>
                  New Player B score = {}<br>
                  <br>
                  Player A & Player B: Draw<br>
                  New Player A score = {}<br>
                  New Player B score = {}</p>'''.format(str(prob[0]),
                                                        str(prob[1]),
                                                        str(awin[0]),
                                                        str(awin[1]),
                                                        str(bwin[0]),
                                                        str(bwin[1]),
                                                        str(draw[0]),
                                                        str(draw[1])))

        elif intError is True:
            print("<h1>ERROR:</h1><p>Please enter a <b>'number'</b> for both "
                  "Player A and Player B </p>")
        else:
            print("<h1>ERROR:</h1><p>Other Error!</p>")
    print_me('index1.html')


if __name__ == '__main__':
    main()
