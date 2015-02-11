import os, binascii
def main():
    print("Content-type: text/plain\n")
    x = 0
    while x < 1000:
        y = binascii.hexlify(os.urandom(16)).decode('utf8')
        if y[0] == 'd' and y[1] == 'b' and y[-2]== 'd' and y[-1] == 'b':
            print(str(x+1) + ': ' + y)
            x += 1
main()
