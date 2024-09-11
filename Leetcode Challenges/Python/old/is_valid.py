"""
Solution to Leetcode problem #20 - Valid Parentheses

https://leetcode.com/problems/valid-parentheses/
"""
class Solution:
    def isValid(self, s: str) -> bool:
        while "()" in s or "{}" in s or "[]" in s:
            s = s.replace("()", "").replace("{}", "").replace("[]", "")
        return s == ""

# using a stack implementation
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2:
            return False
        
        stack = []
        d = {'(':')', '{':'}','[':']'}
        
        for char in s:
            if char in d:
                stack.append(char)
            elif len(stack) == 0 or d[stack.pop()] != char:
                return False
        return len(stack) == 0