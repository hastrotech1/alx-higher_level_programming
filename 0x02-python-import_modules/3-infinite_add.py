#!/usr/bin/python3

if __name__ == "__main__":

    import sys

   arg_count = 0
    arg_len = len(sys.argv) - 1
    for j in range(arg_len):
        arg_count += int(sys.argv[j + 1])
    print("{}".format(arg_count))
