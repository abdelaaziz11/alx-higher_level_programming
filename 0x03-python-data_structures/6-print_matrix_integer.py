#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        length = 1
        for j in i:
            if length == len(i):
                print("{:d}".format(j), end="")
            else:
                print("{:d}".format(j), end=" ")
            length = length + 1
        print()
