#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    maxv = 0
    maxk = None
    for k, v in a_dictionary.items():
        if v > maxv:
            maxv = v
            maxk = k
    return maxk
