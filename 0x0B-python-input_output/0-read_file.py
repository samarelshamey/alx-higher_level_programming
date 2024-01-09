#!/usr/bin/python3
"""module for read_file"""


def read_file(filename=""):
    """read file and print it to stdout"""
    with open('UTF8', 'r') as file:
        filee = file.read()
        print(filee)
