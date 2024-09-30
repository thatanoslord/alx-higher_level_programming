#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError) as msg:
            sys.stderr.write("Exception: {}\n".format(msg))
            return False
