#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    num_of_arg = len(sys.argv)

    list_of_arg = list(sys.argv)

    if num_of_arg == 1:
        print("0 arguments.")
    elif num_of_arg == 2:
        print("{} argument:\n{}: {}".format(1, 1, list_of_arg[1]))
    elif num_of_arg > 2:
        print("{} arguments:".format(num_of_arg - 1))  # excluding filename

        for arg in range(1, num_of_arg):

            print("{}: {}".format(arg, list_of_arg[arg]))
