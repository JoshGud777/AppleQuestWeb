import cgi


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
    print_me('index1.html')

if __name__ == '__main__':
    main()
