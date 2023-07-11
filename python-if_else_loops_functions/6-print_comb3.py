#!/usr/bin/python3
for first in range(0, 10):
    for last in range(0, 10):
        if first == 8 and last == 9:
            print("{:d}{:d}".format(first, last), end="\n")
        elif first < last:
            print("{:d}{:d}".format(first, last), end=", ")
