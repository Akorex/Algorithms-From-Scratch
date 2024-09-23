#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY strings
#  2. STRING_ARRAY queries
#

def matchingStrings(strings, queries):
    # Write your code here
    ans = []
    
    for i in range(len(queries)):
        count = 0
        for j in range(len(strings)):
            if queries[i] == strings[j]:
                count += 1
            j += 1
        ans.append(count)
        i += 1
    return ans


class Solution:
    def matchingStrings(self, strings, queries):
        def matchingStrings(strings, queries):
            string_counts = {}
            for string in strings:
                string_counts[string] = string_counts.get(string, 0) + 1
                
            # Count the occurrences of each query in the dictionary
            results = []
                
            for query in queries:
                results.append(string_counts.get(query, 0))
            return results
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input().strip())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
