#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv)-1
    nArgMsg = "argument"

    if argc != 1:
        nArgMsg += 's'

    if argc == 0:
        nArgMsg += "."
    else:
        nArgMsg += ":"

    print("{:d} ".format(argc) + nArgMsg)

    for arg in range(argc):
        print("{:d}: {}".format(arg+1, sys.argv[arg+1]))
