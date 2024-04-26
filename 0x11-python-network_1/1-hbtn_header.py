#!/usr/bin/python3
"""
script that takes in a URL, sends a request to it
"""
import urllib.request
import sys


with urllib.request.urlopen(sys.argv[1]) as response:
    print(response.headers['X-Request-Id'])
