#!/usr/bin/python3
# 8-uppercase.py
# maureen wangui <375@alx.com>

def uppercase(str):
    """Print a string in uppercase."""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            c = chr(ord(c) - 32)
            print("{}".format(c), end="")
    print("")
