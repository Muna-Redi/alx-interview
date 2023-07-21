#!/usr/bin/python3

""" log parse """

import sys


def print_stat(key, size):
    """ Prints stats info """
    print("File size: {:d}".format(size))
    for i in sorted(key.keys()):
        if key[i] != 0:
            print("{}: {:d}".format(i, key[i]))


stat_codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
               "404": 0, "405": 0, "500": 0}

stat_count = 0
size = 0

try:
    for line in sys.stdin:
        if stat_count != 0 and stat_count % 10 == 0:
            print_stat(stat_codes, size)

        stlist = line.split()
        stat_count += 1

        try:
            size += int(stlist[-1])
        except Exception:
            pass

        try:
            if stlist[-2] in stat_codes:
                stat_codes[stlist[-2]] += 1
        except Exception:
            pass
    print_stat(stat_codes, size)


except KeyboardInterrupt:
    print_stat(stat_codes, size)
    raise
