#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new = []
    for i in my_list:
        new_list = i % 2 == 0
        new.append(new_list)
    return new
