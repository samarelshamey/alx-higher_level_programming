#!/usr/bin/python3
"""module for read_file"""


def read_file(filename=""):
    """read file and print it to stdout"""
    with open(filename, encoding='utf-8') as filee:
        print(filee.read(), end="")
