#!/usr/bin/python3
def no_c(my_string):
    new_str = list(my_string)
    for char in new_str:
        if char == 'c' or char == 'C':
            new_str.remove(char)
    return("".join(new_str))
