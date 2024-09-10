#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number_str = str(number)
last_number = int(number_str[-1])
if last_number > 5:
    str = "and is greater than 5"
elif last_number = 0:
    str  = "and is 0"
else:
    str = "and is less than 6 and not 0"
print(f"Last digit of {number} is {str}")
