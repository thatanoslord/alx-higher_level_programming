#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_dig = abs(number) % 10
if number < 0:
last_dig = -lastDig
if last_dig > 5:
    str = "is greater than 5"
elif last_dig == 0:
    str = "is 0"
elif last_dig < 6 and lastDig != 0:
    str = "is less than 6 and not 0"

print(f"Last digit of {number:d} is {last_dig:d} and {str}")
