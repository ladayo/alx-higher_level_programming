#!/usr/bin/pyton3
def max_integer(my_list=[]):
    if my_list:
        max = 0
        for i in my_list:
            if i > max:
                max = i
    else:
        max = None
    return max