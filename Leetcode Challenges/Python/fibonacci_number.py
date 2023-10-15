"""
Solution to Leetcode problem #509 - Fibonacci Number

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, 
such that each number is the sum of the two preceding ones, starting from 0 and 1. 

"""

# first approach - O(2^n) time complexity, O(n) space 
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        else:
            return self.fib(n - 1) + self.fib(n - 2)

# better approach
class Solution:
    def __init__(self):
        self.dic = {0: 0, 1:1}
        
    def fib(self, n: int) -> int:
        if n not in self.dic:
            self.dic[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.dic[n]
