"""
Solution to Leetcode problem #387 - First Unique Character in a string

https://leetcode.com/problems/first-unique-character-in-a-string/description/

"""

# initial solution

class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = {}

        # count occurences
        for ch in s:
            seen[ch] = seen.get(ch, 0) + 1

        for i in range(len(s)):
            if seen[s[i]] == 1:
                return i

        return -1