#!/usr/bin/python3
# Python script that takes in a URL, sends a request to the URL
import sys
import urllib.request


url = sys.argv[1]
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    X_Request_Id = response.getheader('X-Request-Id')
print(X_Request_Id)
