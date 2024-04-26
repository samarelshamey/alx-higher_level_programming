#!/usr/bin/python3
"""
 Python script that fetches URL
"""
if __name__ == "__main__":
    import requests

    x = requests.get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type:', type(x))
    print('\t- content:', x.text)
