""""
Solution to HackerRank problem - Plus Minus


"""


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    count_pos = 0
    count_neg = 0
    count_zero = 0
    
    for num in arr:
        if num == 0:
            count_zero += 1
        elif num > 0:
            count_pos += 1
        else:
            count_neg += 1
    print(count_pos/len(arr))
    print(count_neg/len(arr))
    print(count_zero/len(arr))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
