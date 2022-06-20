#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    y = 0
    try:
        for i in my_list:
            if (isinstance(i, int)):
                if y < x:
                    print("{:d}".format(i), end="")
                    y += 1
        print()
        return (y)
    except IndexError:
        for i in my_list:
            if (isinstance(i, int)):
                print("{:d}".format(i), end="")
                y += 1
        print()
        return (y)
