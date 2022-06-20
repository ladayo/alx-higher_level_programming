#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    y = 0
    try:
        for i in my_list:
            if y < x:
                print(i, end="")
                y += 1
        print()
        return (y)
    except IndexError:
        for i in my_list:
            print(i, end="")
            y += 1
        print()
        return (y)
