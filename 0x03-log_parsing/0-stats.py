#!/usr/bin/python3
"""This script reads lines from stdin in a specific format
and prints total file size and status code count after 
every 10 lines or keyboard interruption"""

from sys import stdin

def parse_line(line):
    try:
        parts = line.strip().split(" ")
        ip, status, size = parts[0], int(parts[-2]), int(parts[-1])
        return ip, status, size
    except (ValueError, IndexError):
        return None

try:
    total_size, status_count = 0, {200:0, 301:0, 400:0, 401:0, 403:0, 404:0, 405:0, 500:0}

    for i, line in enumerate(stdin, start=1):
        parsed_line = parse_line(line)
        if parsed_line:
            ip, current_status, current_size = parsed_line
            total_size += current_size
            status_count[current_status] = status_count.get(current_status, 0) + 1

            if i % 10 == 0:
                print(f"Total file size: {total_size}")
                for code in sorted(status_count):
                    if status_count[code] > 0:
                        print(f"{code}: {status_count[code]}")

except KeyboardInterrupt:
    print(f"Total file size: {total_size}")
    for code in sorted(status_count):
        if status_count[code] > 0:
            print(f"{code}: {status_count[code]}")
