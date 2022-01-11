#!/usr/bin/python3
""" Takes in a URL and sends a request to the URL
and displays the body of the response
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    response = request.get(url)
    if request.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(response.text)
