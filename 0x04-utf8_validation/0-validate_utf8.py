#!/usr/bin/python3
""" utf8-validation """


def validUTF8(data):
    """ This method determines if a given data set
        represents a valid UTF-8 encoding.

    Args:
            data (list[int]): a list of integers
    """
    continuation_bytes = 0

    # Define bit patterns for UTF-8 encoding
    UTF8_BIT_1 = 1 << 7  # 10000000
    UTF8_BIT_2 = 1 << 6  # 01000000

    for byte in data:
        # this will check for leading 1's in the current byte
        leading_ones = 1 << 7

        # If no continuation bytes is expected
        if continuation_bytes == 0:
            # continuation bytes determined by the
            # number of leading 1's in current byte 
            while leading_ones & byte:
                continuation_bytes += 1
                leading_ones = leading_ones >> 1

            # skip byte if not a multi-byte sequence,
            if continuation_bytes == 0:
                continue

            # checks for invalid continuation byte
            # sequence between 2 and 4
            if continuation_bytes == 1 or\
                    continuation_bytes > 4:
                return False

        # If valid continuation bytes
        else:
            # Check that the byte is prefixed wuth "10"
            # and not an "11" prefix
            if not (byte & UTF8_BIT_1 and not (byte & UTF8_BIT_2)):
                return False

        # number of continuation bytes is decreased here
        continuation_bytes -= 1

    # valid sequence if no more continuation bytes
    if continuation_bytes == 0:
        return True
    else:
        return False
