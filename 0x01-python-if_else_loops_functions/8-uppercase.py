#!/usr/bin/python3
def uppercase(str):
    res_str = ""
    for c in str:
        if ord(c) in range(97, 123):
            c_in_cap = ord(c) - 32
            res_str += chr(c_in_cap)
        else:
            res_str += c

    print("{}".format(res_str))
