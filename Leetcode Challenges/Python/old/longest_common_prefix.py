"""
Solution to Leetcode problem #14 - Longest common prefix
https://leetcode.com/problems/longest-common-prefix/

"""
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ''
        lst = sorted(strs)

        first = lst[0]
        last = lst[-1]

        for i in range(min(len(first), len(last))):
            if (first[i] != last[i]):
                return ans
            ans += first[i]

        return ans