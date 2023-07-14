#!/usr/bin/python3

""" Function Minimum Operations """


def minOperations(n):
    """ This function returns the minimum number
        of operations that can be performed in an         editor that can execute only copy and paste 
        num_operations if a textfile with a single
        character H. is given to produce exactly
        n H characters in the file
        If n is impossible to achieve, 0 is returned
    """
    if not isinstance(n, int):
        return 0

    num_operations = 0
    operations = 2
    while (operations <= n):
        if not (n % operations):
            n = int(n / operations)
            num_operations += operations
            operations = 1
        operations += 1
    return num_operations
