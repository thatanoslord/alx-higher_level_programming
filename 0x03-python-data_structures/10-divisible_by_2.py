#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    bool_list = []
    for i in my_list:
        bool_list.append(True if not i % 2 else False)
    return bool_list
