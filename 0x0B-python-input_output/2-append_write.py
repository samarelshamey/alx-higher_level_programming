#!/usr/bin/python3
"""module for append_write"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file"""
    with open(filename, 'a', encoding='utf-8') as file_append:
        return file_append.append(text)
