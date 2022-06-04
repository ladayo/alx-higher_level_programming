#!/usr/bin/python3
def no_c(my_string):
    my_string_new = []
    if my_string:
        for i in my_string:
            if i not in ['c', 'C']:
                my_string_new.append(i)
        return "".join(my_string_new)
