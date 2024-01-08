#!/usr/bin/python3
"""module for class MyList"""


class MyList(list):
    """inherit of list superclass"""

    def print_sorted(self):
        """print list in sorted way"""
        print(sorted(self))
