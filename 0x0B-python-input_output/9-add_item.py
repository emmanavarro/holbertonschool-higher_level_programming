#!/usr/bin/python3
"""
script that adds all arguments to a Python
list, and then save them to a file
"""


import sys


save_to_json = __import__("7-save_to_json_file").save_to_json_file
load_from_json = __import__("8-load_from_json_file").load_from_json_file


arguments = sys.argv[1:]
try:
    my_list = load_from_json("add_item.json")
except IOError:
    my_list = []
save_to_json(my_list + arguments, "add_item.json")
