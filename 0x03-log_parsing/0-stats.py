#!/usr/bin/python3
"""This script reads lines from stdin in a specific format
and prints total file size and status code count after 
every 10 lines or keyboard interruption"""

from sys import stdin

try:
    code_count, size_total = {}, 0
    for i, line in enumerate(stdin, start=1):
        parts = line.strip().split(" ")
        size_total += int(parts[-1])
        code_count[parts[-2]] = code_count.get(parts[-2], 0) + 1
        if i % 10 == 0:
            print(f"File size: {size_total}")
            for key, val in sorted(code_count.items()):
                print(f"{key}: {val}")
            size_total, code_count = 0, {}
except KeyboardInterrupt:
    print(f"File size: {size_total}")
    for key, val in code_count.items():
        print(f"{key}: {val}")
