#!/usr/bin/python3
''' fetches https://alx-intranet.hbtn.io/status #1 '''

import requests


if __name__ == "__main__":
    request = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(request.text)))
    print("\t- content: {}".format(request.text))
