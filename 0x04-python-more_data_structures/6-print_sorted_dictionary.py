#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary: dict):
    keys = a_dictionary.keys()
    keys = sorted(keys)

    for k in keys:
        print("{}: {}".format(k, a_dictionary[k]))
