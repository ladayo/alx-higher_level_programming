#!/usr/bin/python3

import sys

if __name__ == "__main__":
    n = len(sys.argv)
    total = 0
    for i in range(1, n):
        j = int(sys.argv[i])
        total += j
    print("{:d}".format(total))
