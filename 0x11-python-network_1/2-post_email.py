#!/usr/bin/python3
'''
takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter
displays the body of the response (decoded in utf-8)
'''

import urllib.request
import sys
import urllib.parse


if __name__ == "__main__":
    url = sys.argv[1]
    email_var = {"email": sys.argv[2]}
    urlData = urllib.parse.urlencode(email_var).encode("ascii")

    with urllib.request.urlopen(url, urlData) as res:
        print(response.read().decode("utf-8"))
