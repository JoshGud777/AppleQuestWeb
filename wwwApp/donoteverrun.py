import binascii
import os

def main():
    print("Content-type: text/plain\n")
    x = 0
    while x < 50:
        y = binascii.hexlify(os.urandom(16)).decode('utf8')
        if y[0] == 'd' and y[1] == 'b' and y[-2] == 'd' and y[-1] == 'b':

            if x < 9:
                z = ' :'
            else:
                z = ':'

            print(str(x+1) + z + y)
            x += 1

if __name__ == '__main__':
    main()