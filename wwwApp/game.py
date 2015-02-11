def print_me(filename):
    f = open(filename, 'r')

    for line in f:
        print(line, end=' ')
    f.close

def main():
    print("Content-type: text/html")
    print()
    print('GAME.HTML')
    
if __name__ == '__main__':
    main()
