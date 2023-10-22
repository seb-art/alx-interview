#!/usr/bin/python3
'''A script for parsing HTTP request logs.
'''
import re

def extract_input(input_line):
    '''Extracts sections of a line of an HTTP request log.
    
    Args:
        input_line (str): A line of the HTTP request log.

    Returns:
        dict: A dictionary containing 'status_code' and 'file_size' extracted from the input line.
    '''
    log_format = r'\s*(?P<ip>\S+)\s*\[(?P<date>\S+)] "(?P<request>[^"]*)" (?P<status_code>\d+) (?P<file_size>\d+)'
    match = re.match(log_format, input_line)
    if match:
        return {
            'status_code': match.group('status_code'),
            'file_size': int(match.group('file_size'))
        }
    return None

def print_statistics(total_file_size, status_codes_stats):
    '''Prints the accumulated statistics of the HTTP request log.
    
    Args:
        total_file_size (int): The total file size accumulated so far.
        status_codes_stats (dict): A dictionary with status code counts.
    '''
    print(f'File size: {total_file_size}')
    for status_code, count in sorted(status_codes_stats.items()):
        if count > 0:
            print(f'{status_code}: {count}')

def update_metrics(line, total_file_size, status_codes_stats):
    '''Updates the metrics from a given HTTP request log.
    
    Args:
        line (str): The line of input from which to retrieve the metrics.
        total_file_size (int): The current total file size.
        status_codes_stats (dict): A dictionary with status code counts.

    Returns:
        int: The new total file size.
    '''
    line_info = extract_input(line)
    if line_info:
        status_code = line_info['status_code']
        if status_code in status_codes_stats:
            status_codes_stats[status_code] += 1
        total_file_size += line_info['file_size']
    return total_file_size

def run():
    '''Starts the log parser.
    '''
    line_num = 0
    total_file_size = 0
    status_codes_stats = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0,
    }
    try:
        while True:
            line = input()
            total_file_size = update_metrics(line, total_file_size, status_codes_stats)
            line_num += 1
            if line_num % 10 == 0:
                print_statistics(total_file_size, status_codes_stats)
    except (KeyboardInterrupt, EOFError):
        print_statistics(total_file_size, status_codes_stats)

if __name__ == '__main__':
    run()
