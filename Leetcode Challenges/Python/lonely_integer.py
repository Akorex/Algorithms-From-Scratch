"""
Solution to HackerRank problem

"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    seen = {}
    
    for num in a:
        seen[num] = seen.get(num, 0) + 1
        
    for key, value in seen.items():
        if value == 1:
            return key