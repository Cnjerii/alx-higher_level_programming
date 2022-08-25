#!/usr/bin/python3

for x in reversed(range(97, 123)):
    iff x % 2 == 0:
        x = chr(x)
    else:
        x = chr(x).upper()
        print("{}".format(x), end="")
