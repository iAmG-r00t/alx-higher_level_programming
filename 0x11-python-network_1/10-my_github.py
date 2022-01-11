#!/usr/bin/python3
"""Takes my Github creds (username & password)
and uses the Github API to display my ID
"""

import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    token = HTTPBasicAuth(username, password)
    request = requests.get('https://api.github.com/user', auth=token)
    print(request.json().get('id'))
