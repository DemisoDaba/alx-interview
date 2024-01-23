#!/usr/bin/python3
"""This script reads lines from stdin in a specific format
and prints total file size and status code count after 
every 10 lines or keyboard interruption"""

from sys import stdin

try:
    my_dict = {}
    total_size = 0
    for i, line in enumerate(stdin, start=1):
        parts = line.strip().split(" ")
        total_size += int(parts[-1])
        if parts[-2] not in my_dict:
            my_dict[parts[-2]] = 1
        else:
            my_dict[parts[-2]] += 1
        my_dict = dict(sorted(my_dict.items()))
        if i % 10 == 0:
            print("File size: {}".format(total_size))
            for key, val in my_dict.items():
                print("{}: {}".format(key, val))
            total_size = 0
            my_dict = {}
except KeyboardInterrupt:
    print("File size: {}".format(total_size))
    for key, val in my_dict.items():
        print("{}: {}".format(key, val))
