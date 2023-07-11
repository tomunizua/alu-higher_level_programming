#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_val = number % 10
if number < 0:
    last_val = (-1) * ((number * -1) % 10)
if last_val > 5:
    print(f"Last digit of {number:d} is {last_val} and is greater than 5")
elif last_val == 0:
    print(f"Last digit of {number:d} is {last_val} and is 0")
else:
    print(f"Last digit of {number:d} is {last_val} and is \
less than 6 and not 0")
