#!/usr/bin/env python3
def uppercase(str):
    for ch in str:
        if ord('z') >= ord(ch) >= ord('a'):
           ch = chr(ord(ch) - 32)
        print("{:c}".format(ch), end="")
    print()
