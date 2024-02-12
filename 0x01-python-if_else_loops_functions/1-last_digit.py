#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
theLastDigit = number % 10

if theLastDigit > 5:
    theLastDigit = -1
    print(f"Last digit of {number} is {theLastDigit} and is greater than 5")
elif theLastDigit == 0:
    print(f"Last digit of {number} is {theLastDigit} and is 0")
elif theLastDigit < 6 and theLastDigit != 0:
    print(f"Last digit of {number} is {theLastDigit} and is less than 6 and not 0")
