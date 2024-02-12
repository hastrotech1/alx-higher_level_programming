#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
LastDig = number % 10
# LastDig still means Last Digit fam
if LastDig > 5:
    print(f"Last digit of {number} is {LastDig} and is greater than 5")
elif LastDig == 0:
    print(f"Last digit of {number} is {LastDig} and is 0")
elif LastDig < 6 and LastDig != 0:
    print(f"Last digit of {number} is {LastDig} and is less than 6 and not 0")
