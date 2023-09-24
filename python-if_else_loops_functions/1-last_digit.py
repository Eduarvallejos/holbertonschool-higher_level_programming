#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
d = abs(number) % 10
sign = "-" if number < 0 else ""
condition = ""

if d > 5:
    condition = "and is greater than 5"
elif d == 0:
    condition = "and is 0"
else:
    condition = "and is less than 6 and not 0"

print(f"Last digit of {number} is {sign}{d} {condition}")

