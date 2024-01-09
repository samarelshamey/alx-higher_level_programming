#!/usr/bin/python3
"""module for read_file"""


def read_file(filename=""):
    """read file and print it to stdout"""
    with open(filename, encoding = 'UTF-8', 'r') as filee:
        print(filee.read(), end="")
