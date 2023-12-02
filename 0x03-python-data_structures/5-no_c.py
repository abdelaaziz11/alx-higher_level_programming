#!/usr/bin/env python3
def no_c(my_string):
    new = ""
    for item in my_string:
        if item.lower() != 'c':
            new += item
    return new
