#!/usr/bin/python3
# script that takes in a URL, sends a request to it
import urllib.request
import sys


url = sys.argv[1]
with urllib.request.urlopen(url) as response:
    print(response.headers['X-Request-Id'])
