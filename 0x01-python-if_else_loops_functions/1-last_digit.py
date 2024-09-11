#!/usr/bin/python3
import random
number = random.randint(-10, 10)
lastDig = abs(number) % 10
if number < 0:
    lastDig = -lastDig
if lastDig > 5:
    str = "is greater than 5"
elif lastDig == 0:
    str = "is 0"
else lastDig < 6 and lastDig != 0:
    str = "is less than 6 and not 0"
print(f"Last digit of {number:d} is {lastDig:d} and {str}")
