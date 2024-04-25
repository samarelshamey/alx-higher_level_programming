#!/usr/bin/python3
"""module contain fin_peak method"""
def find_peak(list_of_integers):
    """method to find a peak in unsorted integers"""
    if list_of_integers:
        list_of_integers.sort(reverse=True)
        return list_of_integers[0]
