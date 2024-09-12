#!/usr/bin/python3
for i in range(-122, -96):
    print("{}".format(chr(abs(i)) if i % 2 == 0 else chr(abs(i)-32)), end="")
