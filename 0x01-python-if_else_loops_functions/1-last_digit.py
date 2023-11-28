#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = abs(number) % 10 if number > 10 else number % -10
if digit < 6 and digit != 0:
    print(f"Last digit of {number} is {digit} and is less than 6 and not 0")
elif digit > 5:
    print(f"Last digit of {number} is {digit} and is greater than 5")
else:
    print(f"Last digit of {number} is {digit} and is 0")
