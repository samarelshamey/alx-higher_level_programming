#!/usr/bin/python3
"""module for all args"""


import sys
from os.path import exists
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_items_to_list(items):
    if exists("add_item.json"):
        existing_data = load_from_json_file('add_item.json')
        existing_data.extend(items)
        save_to_json_file(existing_data, "add_item.json")
    else:
        new_data = items
        save_to_json_file(new_data, "add_item.json")


argslst = sys.argv[1:]
add_items_to_list(argslst)
