#!/usr/bin/python3
def no_c(my_string):
    my_string_new = [x for x in my_string if x not in ['c', 'C']]
    return "".join(my_string_new)
