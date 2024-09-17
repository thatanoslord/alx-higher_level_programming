#!/usr/bin/python3
def no_c(my_string: str):
    return "".join(i for i in my_string if i not in "cC")
