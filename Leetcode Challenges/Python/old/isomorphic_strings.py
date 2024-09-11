"""Solution to Leetcode problem #205 - isomorphic strings

https://leetcode.com/problems/isomorphic-strings/
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_1 = []
        map_2 = []

        for e in s:
            map_1.append(s.index(e))

        for e in t:
            map_2.append(t.index(e))

        return map_1 == map_2
    
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t) or len(set(s)) != len(set(t)):
            return False
        mapped = {}

        for i in range(len(s)):
            if s[i] not in mapped:
                mapped[s[i]] = t[i]

            if mapped[s[i]] != t[i]:
                return False
        return True