#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for idx, ele in enumerate(row):
            if idx == len(row) - 1:
                print("{:d}".format(ele), end="")
            else:
                print("{:d}".format(ele), end=" ")
        print()
