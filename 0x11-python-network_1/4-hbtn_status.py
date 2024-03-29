#!/usr/bin/python3
""" fetches https://intranet.hbtn.io/status """
import requests


if __name__ == '__main__':
    url = "https://intranet.hbtn.io/status"
    r = requests.get(url)
    txt = r.text
    print("Body response:")
    print("\t- type: {}".format(type(txt)))
    print("\t- content: {}".format(txt))
