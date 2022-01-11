#!/usr/bin/python3
"""Lists 10 commits from the most recent to the oldest
of the repository "rails" by the user rails
"""

import sys
import requests

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo_name)

    request = requests.get(url)
    commits = request.json()
    try:
        for i in range(10):
            print('{}: {}'.format(
                commits[i].get('sha'),
                commits[i].get('commit').get('author').get('name')))
    except IndexError:
        pass
