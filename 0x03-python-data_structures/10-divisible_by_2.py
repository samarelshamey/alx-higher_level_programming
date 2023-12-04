#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        my_list == []
    new_list = []
    else:
        for i in my_list:
            new_list.append(False if i % 2 else True)
        return new_list
