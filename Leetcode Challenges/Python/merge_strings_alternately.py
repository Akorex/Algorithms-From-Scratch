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
    

class Solutionn:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []

        for i, j in zip(word1, word2):
            merged.append(i)
            merged.append(j)

        merged.append(word1[len(word2):])
        merged.append(word2[len(word1):])
        return "".join(merged)
    
    
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        i, j = 0, 0
        
        while i < len(word1) and j < len(word2):
            result.append(word1[i])
            result.append(word2[j])
            i += 1
            j += 1
        
        result.extend(word1[i:])
        result.extend(word2[j:])
        
        return "".join(result)