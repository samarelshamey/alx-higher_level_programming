#!/usr/bin/python3
"""
script that takes your GitHub credentials
uses the GitHub API to display your id
"""
if __name__ == "__main__":
    from requests import get
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"
    req = get(url, auth=(username, password))
    json = req.json()
    print(json.get('id'))
