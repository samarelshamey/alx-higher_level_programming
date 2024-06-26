#!/usr/bin/python3
"""
sends a request to the URL and displays the body of the response
"""
if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    req = requests.get(url)
    code = req.status_code
    if code >= 400:
        print('Error code:', code)
    else:
        print(req.text)
