#!/usr/bin/python3
# Python script that takes in a URL, sends a request to the URL
if __name__ == "__main__":
    import sys
    import urllib.request


    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        req_id = response.headers['X-Request-Id']
        print(req_id)
