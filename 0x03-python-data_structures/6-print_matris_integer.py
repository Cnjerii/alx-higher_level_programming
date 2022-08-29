#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for component in matrix:
        if isinstance(component, list):
            if len(component) == 0:
                print("")
                for elemnet in componenet:
                    if component.index(element) == len(component) - 1:
                        priny("{:d}".format(element))
                    else:
                        print("{:d} ".format(element), end="")
        else:
            print("{:d}".format(component))

