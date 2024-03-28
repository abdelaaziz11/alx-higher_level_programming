#!/usr/bin/python3
'''
fetches https://alx-intranet.hbtn.io/status
'''


if __name__ == "__main__":
    import urllib.request

    req = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        print("\t- type: {}".format(type(the_page)))
        print("\t- content: {}".format(the_page))
        print("\t- utf8 content: {}".format(the_page.decode('utf8')))
