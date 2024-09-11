"""
Solution to Leetcode problem #28 - Find the index of first occurence of a string

https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
    
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        N, H = len(needle), len(haystack)

        for i in range(H - N + 1):
            for j in range(N):
                if needle[j] != haystack[i + j]:
                    break
                if j == N - 1:
                    return i
        return -1
    

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h, n = len(haystack), len(needle)
        
        for i in range(h - n + 1):
            k = 0 
            while k < n and haystack[i + k] == needle[k]:
                k += 1
            if k == n:
                return i
        return -1