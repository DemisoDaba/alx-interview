#!/usr/bin/python3
"""This script reads lines from stdin in a specific format
and prints total file size and status code count after 
every 10 lines or keyboard interruption"""

import sys
import re


def display_stats(log: dict) -> None:
    """
    Helper function to display statistics
    """
    print(f"File size: {log['file_size']}")
    for code in sorted(log['code_frequency']):
        if log['code_frequency'][code]:
            print(f"{code}: {log['code_frequency'][code]}")


if __name__ == "__main__":
    regex_pattern = re.compile(
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d+\] "GET /projects/260 HTTP/1.1" (.{3}) (\d+)'
    )

    line_count = 0
    log = {
        "file_size": 0,
        "code_frequency": {str(code): 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]},
    }

    try:
        for line in sys.stdin:
            line = line.strip()
            match = regex_pattern.fullmatch(line)
            if match:
                line_count += 1
                code = match.group(1)
                file_size = int(match.group(2))

                # File size
                log["file_size"] += file_size

                # Status code
                if code.isdecimal():
                    log["code_frequency"][code] += 1

                if line_count % 10 == 0:
                    display_stats(log)
    finally:
        display_stats(log)
