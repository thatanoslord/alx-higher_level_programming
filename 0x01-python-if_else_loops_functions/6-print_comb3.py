#!/usr/bin/python3
for i in range(0, 10):
    for y in range(i+1, 10):
        if i == 8 and y == 9:
            print('89')
        else:
            print("{}{}, ".format(i, y), end="")
