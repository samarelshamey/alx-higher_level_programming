#!/usr/bin/python3
"""
Python script that takes 2 arguments
"""
if __name__ == "__main__":
    import requests
    import sys

    repo = sys.argv[1]
    owner = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    req = requests.get(url)
    js = req.json()[:10]
    js.reverse()
    for commit in js:
        sha = commit.get('sha')
        author_name = commit.get('commit').get('author').get('name')
        print(f"{sha}: {author_name}")
