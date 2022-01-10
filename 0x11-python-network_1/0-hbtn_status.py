#!/usr/bin/python3
"""Fetch
https://intranet.hbtn.io/status
using urlib package
"""

if __name__ == '__main__':
    import urllib.request

    url = 'https://intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as request:
        response = request.read()
        print ("Body response:")
        print("\t- type: {}".format(type(response)))
        print("\t- content: {}".format(response))
        print("\t- utf8 content: {}".format(response.decode('utf-8')))
