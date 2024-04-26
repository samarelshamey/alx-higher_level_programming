#!/usr/bin/python3
# Python script that takes in a URL, sends a request to the URL
import sys
import urllib.request


url = sys.argv[1]
with urllib.request.urlopen(url) as response:
    print(response.headers['X-Request-Id'])
