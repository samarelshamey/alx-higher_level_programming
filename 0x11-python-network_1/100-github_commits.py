#!/usr/bin/python3
"""
Python script that takes 2 arguments
"""
if __name__ == "__main__":
    import requests
    import sys

    repo = sys.argv[1]
    owner = sys.argv[2]
    i = 0
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    req = requests.get(url)
    js = req.json()
    for commit in js:
        if i > 9:
            break
        sha = commit.get('sha')
        author = commit.get('commit').get('author').get('name')
        print("{}: {}".format(sha, author))
        i += 1
