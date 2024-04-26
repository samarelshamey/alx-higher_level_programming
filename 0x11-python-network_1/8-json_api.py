#!/usr/bin/python3
"""
script that takes in a letter
sends a POST request to http://0.0.0.0:5000/search_user
"""
if __name__ == "__main__":
    import sys
    import requests

    url = 'http://0.0.0.0:5000/search_user'
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    req = requests.post(url, data={'q': q})
    try:
        req_j = req.json()
        if req_j:
            print("[{}] {}".format(req_j.get('id'), req_j.get('name')))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
