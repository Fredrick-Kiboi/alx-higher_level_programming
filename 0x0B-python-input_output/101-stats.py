#!/usr/bin/python3
"""Reads stdin line by line and computes metrics"""

import sys

total_file_size = 0
status_code_counts = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
line_count = 0

try:
    for line in sys.stdin:
        tokens = line.split()
        if len(tokens) >= 2:
            previous_line_count = line_count
            if tokens[-2] in status_code_counts:
                status_code_counts[tokens[-2]] += 1
                line_count += 1
            try:
                total_file_size += int(tokens[-1])
                if previous_line_count == line_count:
                    line_count += 1
            except Exception:
                if previous_line_count == line_count:
                    continue
        if line_count % 10 == 0:
            print("Total file size: {:d}".format(total_file_size))
            for status_code, count in sorted(status_code_counts.items()):
                if count:
                    print("{:s}: {:d}".format(status_code, count))
    print("Total file size: {:d}".format(total_file_size))
    for status_code, count in sorted(status_code_counts.items()):
        if count:
            print("{:s}: {:d}".format(status_code, count))

except KeyboardInterrupt:
    print("Total file size: {:d}".format(total_file_size))
    for status_code, count in sorted(status_code_counts.items()):
        if count:
            print("{:s}: {:d}".format(status_code, count))
