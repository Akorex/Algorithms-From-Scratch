"""
Solution to Leetcode problem 1768 - Merge Strings Alternately
https://leetcode.com/problems/merge-strings-alternately/description/

"""




class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        left = len(word1)
        right = len(word2)
        marker = max([left, right])

        for i in range(marker):
            if i < left:
                merged += word1[i]
            if i < right:
                merged += word2[i]
        return merged