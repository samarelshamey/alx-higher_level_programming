#!/usr/bin/python3
"""module for class_to_json"""


def class_to_json(obj):
    """ function that returns dictionary"""
    return obj.__dict__
