#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request to the URL
displays the value of the variable X-Request-Id in the response header
"""
if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    req = requests.get(url)
    req_id = req.headers.get('X-Request-Id')
    print(req_id)
