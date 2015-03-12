'''index page of applequest.fallenofftheedge.com'''
if __name__ == '__main__':
    import library as lib
else:
    import webapp.library as lib

import time


def html_p():
    '''Prints the html to the client with any data we want added
        $$unixtime$$'''
    html = lib.get_html(lib.HTML_DIR + 'index.html')
    time_f = str(time.time())
    time_r = time_f[::-1]

    unixtime_r = time_r[:10] + ',' + time_r[10:13] + ',' + time_r[14:18]

    unixtime = unixtime_r[::-1]

    html = html.replace('$$unixtime$$', unixtime)
    print(html)


def main():
    '''Main'''
    lib.print_header()
    html_p()


if __name__ == '__main__':
    main()
