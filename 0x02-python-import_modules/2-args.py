#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    leng = len(sys.argv) - 1
    if leng == 1:
        print("1 argument:")
    elif leng == 0:
        print("0 arguments.")
    else:
        print("{} arguments:".format(leng))
    for n in range(leng):
        print("{}: {}".format(n + 1, sys.argv[n + 1]))
