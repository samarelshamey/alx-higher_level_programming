#!/usr/bin/python3
"""module for read_file"""


def read_file(filename=""):
    """read file and print it to stdout"""
    with open(filename, 'r') as file:
        filee = filename.read()
        print(filee)