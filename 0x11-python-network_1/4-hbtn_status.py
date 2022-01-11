#!/usr/bin/python3
"""
Same as Task 0 but using request package
"""

import requests


if __name__ == "__main__":
    r = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- type: {}".format(r.text))
