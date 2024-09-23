"""
Solution to Leetcode problem #844 - Backspace string compare

https://leetcode.com/problems/backspace-string-compare/
"""

# using the stack approach
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def process_string(string):
            stack = []

            for char in string:
                if char != '#':
                    stack.append(char)
                elif stack:
                    stack.pop()
            return stack
        return process_string(s) == process_string(t)
    

# using two-pointer approach
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def process_string(string):
            k = 0

            for i in range(len(string)):
                if string[i] != '#':
                    string[k] = string[i]
                    k += 1
                else:
                    k = max(k-1, 0)
            return k
        
        s, t = list(s), list(t)

        # effective lengths
        k = process_string(s)
        p = process_string(t)

        if k != p:
            return False

        for i in range(k):
            if s[i] != t[i]:
                return False
        return True