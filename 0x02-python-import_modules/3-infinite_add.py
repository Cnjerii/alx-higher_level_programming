#!/usr/bin/python3

from sys import argv as args


def inifinite_add():
    return sum([int(x) for x in args[1:]])


if __name__ == "__main__":
    print(inifinite_add())
