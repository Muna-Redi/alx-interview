#!/usr/bin/python3
""" Solution to Isand Perimeter question"""


def check_val(x):
    """checks value

    """
    if (x == 0):
        return 1
    return 0


def island_perimeter(grid):
    """returns the perimeter of the given island
    """

    row = len(grid)
    col = len(grid[0])
    assert (1 <= row and col <= 100), "checks if  its between 1 an 100"

    x = 0
    for i in range(row):
        for j in range(col):
            assert (grid[i][j] == 0) or (grid[i][j] == 1),\
                "checks if grid numbers is 0 or 1"
            if grid[i][j] == 1:
                if i-1 < 0:
                    x += 1
                else:
                    x += check_val(grid[i-1][j])
                if j-1 < 0:
                    x += 1
                else:
                    x += check_val(grid[i][j-1])

                try:
                    x += check_val(grid[i+1][j])
                except IndexError:
                    x += 1
                try:
                    x += check_val(grid[i][j+1])
                except IndexError:
                    x += 1

    return x
