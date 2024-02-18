#!/usr/bin/python3
"""
This code prints the sum of 1 + 2

using the "import" module.
"""
if __name__ == "__main__":
    from add_0 import add
    a = 1
    b = 2

    print("{} + {} = {}".format(a, b, add(a, b)))
