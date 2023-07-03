#!/usr/bin/python3
""" This script returns the obtains the pascal triangle"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the 
    Pascal’s triangle of size n
    """
    triangle = []

    # return (trianlgle if n <= 0)
    if n <= 0:
        return triangle
    for i in range(n):
        new_list = []

        for j in range(i+1):
            if j == 0 or j == i:
                new_list.append(1)
            else:
                new_list.append(triangle[i-1][j-1] + triangle[i-1][j])
        triangle.append(new_list)
    return triangle
