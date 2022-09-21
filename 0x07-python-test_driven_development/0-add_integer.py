#!/usr/bin/python3
def add_integer(a, b=98):
    '''Adds two integers
    Args: a : the first integer, b: the second integer
    '''

    if type(a) not in(int, float):
        raise TyppeError("a must be an integer")
    if type(b) not in (int, float):
        raise typeError("b must be an integer")

    return int(a) + int(b)
