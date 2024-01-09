#!/usr/bin/python3
"""module for write_file"""


def write_file(filename="", text=""):
    """write  a string to a text file"""
    with open(filename, 'w', encoding='UTF-8') as f:
        return f.write(text)
