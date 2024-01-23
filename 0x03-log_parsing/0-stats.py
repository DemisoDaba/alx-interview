#!/usr/bin/python3
'''A script for parsing HTTP request logs.
'''
import re

def extract_input(line):
    fp = r'\s*(?P<ip>\S+)\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]\s*"(?P<request>[^"]*)"\s*(?P<status_code>\S+)\s*(?P<file_size>\d+)'
    info = {'status_code': 0, 'file_size': 0}
    resp_match = re.fullmatch(fp, line)
    if resp_match: info['status_code'], info['file_size'] = resp_match.group('status_code'), int(resp_match.group('file_size'))
    return info

def print_statistics(total_file_size, status_codes_stats):
    print(f'File size: {total_file_size}', flush=True)
    for status_code, num in sorted(status_codes_stats.items()):
        if num: print(f'{status_code}: {num}', flush=True)

def update_metrics(line, total_file_size, status_codes_stats):
    line_info = extract_input(line)
    status_codes_stats[line_info.get('status_code', '0')] += 1
    return total_file_size + line_info['file_size']

def run():
    line_num, total_file_size = 0, 0
    status_codes_stats = {str(i): 0 for i in [200, 301, 400, 401, 403, 404, 405, 500]}

    try:
        while True:
            line = input()
            total_file_size = update_metrics(line, total_file_size, status_codes_stats)
            line_num += 1
            if line_num % 10 == 0: print_statistics(total_file_size, status_codes_stats)
    except (KeyboardInterrupt, EOFError): print_statistics(total_file_size, status_codes_stats)

if __name__ == '__main__':
    run()
