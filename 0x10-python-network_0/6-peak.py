#!/usr/bin/python3
"""module contain fin_peak method"""
def find_peak(list_of_integers):
    """method to find a peak in unsorted integers"""
    lst = list_of_integers
    if not lst:
        return None
    peak = lst[0]
    for num in lst:
        if num > peak:
            peak = num
    return peak
