#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        res = fct(*args)
    except Exception as e:
        sys.stderr.write("Exception: {}\n".format(e))
        res = None
    finally:
        return res
