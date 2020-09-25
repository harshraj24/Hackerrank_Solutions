# Hackerrank 30 days challenge day 7 Solution

# Given an array A of N integers, print 's elements in reverse order as a single line of space-separated numbers.

# Solution

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    for i in arr[::-1]:
        print(str(i),end=" ")