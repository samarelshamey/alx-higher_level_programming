#!/usr/bin/python3
# Write a Python script that fetches url
import urllib.request

url = 'https://alx-intranet.hbtn.io/status'
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    html = response.read()
print('Body response:')
print('\t- type:', type(html))
print('\t- content:', html)
print('\t- utf8 content:', html.decode('utf-8'))
