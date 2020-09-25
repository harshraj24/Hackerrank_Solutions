# Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum.

# Solution

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    max_sum=0

    

