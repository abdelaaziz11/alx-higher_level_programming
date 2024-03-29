#!/usr/bin/python3
'''  POST request to the passed URL with the email as a parameter '''

import sys
import requests


if __name__ == "__main__":
    value = {"email": sys.argv[2]}

    req = requests.post(sys.argv[1], data=value)
    print(req.text)
