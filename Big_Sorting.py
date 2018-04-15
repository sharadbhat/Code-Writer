# HACKERRANK
# https://www.hackerrank.com/challenges/big-sorting/problem

import os
import sys

def bigSorting(unsorted):
    unsorted.sort(key=int)
    return unsorted

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    unsorted = []

    for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)

    result = bigSorting(unsorted)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
