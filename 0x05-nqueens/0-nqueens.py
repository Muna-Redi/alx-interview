#!/usr/bin/python3
""" Module For Nqueens problem """
import sys


class NQueens:
    """ Taking an Nqueen class """

    def __init__(self, n):
        """ instantiates """
        self.n = n
        self.x = [0 for x in range(n + 1)]
        self.result = []

    def place(self, k, i):
        """ Checks if k number of  Queen can be placed in i 
            column without being threatebed or another queen
            in same diagonal
        """

        # j checks from 1 to k - 1 (Up to previous queen)
        for j in range(1, k):
            # If There is already a queen in column in same diagonal
            if self.x[j] == i or \
               abs(self.x[j] - i) == abs(j - k):
                return 0
        return 1

    def nQueen(self, k):
        """  possiblity of placing every queen in the board
        """
        # moving from column 1 to column n (1st column is 1st index)
        for i in range(1, self.n + 1):
            if self.place(k, i):
                # Queen can be placed in i column
                self.x[k] = i
                if k == self.n:
                    # All 4 Queens placed (A solution was found)
                    result = []
                    for i in range(1, self.n + 1):
                        result.append([i - 1, self.x[i] - 1])
                    self.result.append(result)
                else:
                    # recursion to place more Queens
                    self.nQueen(k + 1)
        return self.result


# Runs program
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

N = sys.argv[1]

try:
    N = int(N)
except ValueError:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)

queen = NQueen(N)
result = queen.nQueen(1)

for i in result:
    print(i)
