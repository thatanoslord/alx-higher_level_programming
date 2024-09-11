#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number_str = str(number)  
last_digit = int(number_str[-1])
if last_digit > 5:
    result = "and is greater than 5"
elif last_digit == 0:
    result = "and is 0"
else:
    result = "and is less than 6 and not 0"

print(f"Last digit of {number} is {result}")

