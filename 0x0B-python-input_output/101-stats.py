#!/usr/bin/python3
import sys
import signal
from collections import defaultdict


STATUSES = ['200', '301', '400', '401', '403', '404', '405', '500']


def print_statistics(total_size, status_counts):
    print(f'Total file size: {total_size}')
    for status_code in sorted(status_counts):
        print(f'{status_code}: {status_counts[status_code]}')


def compute_metrics():
    total_size = 0
    status_counts = defaultdict(int)
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            if line:
                _, _, _, status_code, file_size = line.split(' ')
                total_size += int(file_size)
                status_counts[status_code] += 1
                line_count += 1

            if line_count % 10 == 0:
                print_statistics(total_size, status_counts)

    except KeyboardInterrupt:
        print_statistics(total_size, status_counts)


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    compute_metrics()
