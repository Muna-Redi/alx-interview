#!/usr/bin/python3
""" log parse """

import sys

""" Globals """
total_size = 0

line_count = 0

stat_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
                     '404': 0, '405': 0, '500': 0}


try:
    for line in sys.stdin:
        line_list = line.split(" ")

        if len(line_list) > 4:
            status_code = line_list[-2]
            file_size = int(line_list[-1])

            if status_code in stat_codes.keys():
                stat_codes[status_code] += 1

            total_size += file_size

            line_count += 1

        if line_count == 10:
            line_count = 0
            print('File size: {}'.format(total_size))

            for key, value in sorted(stat_codes.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))

except Exception as e:
    pass

finally:
    print('File size: {}'.format(total_size))
    for key, value in sorted(stat_codes.items()):
        if value != 0:
            print('{}: {}'.format(key, value))
