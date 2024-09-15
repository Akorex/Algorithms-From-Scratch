"""
Solution to Leetcode problem #509 - Fibonacci Number

https://leetcode.com/problems/fibonacci-number/description/
"""


class Solution:
    def __init__(self):
        self.ans = {0: 0, 1:1}
    
    def fib(self, n: int) -> int:
        if n not in self.ans:
            self.ans[n] = self.fib(n-1) + self.fib(n-2)
        return self.ans[n]