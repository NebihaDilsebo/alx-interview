#!/usr/bin/env python3

import sys
import re


# Initialize variables to store metrics
total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    for line in sys.stdin:
        line = line.strip()
        # Use regex to parse the line
        match = re.match(r'(\d+\.\d+\.\d+\.\d+) - \[.+\] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)', line)
        if match:
            ip, status_code, file_size = match.groups()
            status_code = int(status_code)
            file_size = int(file_size)

            # Update metrics
            total_file_size += file_size
            status_code_counts[status_code] += 1
            line_count += 1

        # Print metrics every 10 lines
        if line_count % 10 == 0:
            print("Total file size: File size: {}".format(total_file_size))
            for code, count in sorted(status_code_counts.items()):
                if count > 0:
                    print("{}: {}".format(code, count))
            print()

except KeyboardInterrupt:
    pass

# Print final metrics
print("Total file size: File size: {}".format(total_file_size))
for code, count in sorted(status_code_counts.items()):
    if count > 0:
        print("{}: {}".format(code, count))
