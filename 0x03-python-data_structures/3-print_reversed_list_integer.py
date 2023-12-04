#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    revList = my_list.sort(reverse=True)
    for i in revList:
        print("{:d}".format(i))
