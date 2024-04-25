#!/usr/bin/python3
"""module contain fin_peak method"""
def find_peak(list_of_integers):
    """method to find a peak in unsorted integers"""
    lst = list_of_integers
    if lst:
        lst.sort(reverse=True)
        return lst[0]
