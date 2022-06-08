#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list:
        new_list = list({i for i in my_list})
        add = 0
        for i in new_list:
            add = add + i
        return add
