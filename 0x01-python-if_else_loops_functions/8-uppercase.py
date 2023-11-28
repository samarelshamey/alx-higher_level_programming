#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        if ord('z') >= ord(ch) >= ord('a'):
            ch = chr(ord(ch)-32)
        print("{:s}".format(ch), end="")
    print()
