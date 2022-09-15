"""Solution to Leetcode problem #70 - Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

The intuition to express the code as a Fibonacci sequence starting with 1, 2 (opposed to 1, 1)
was given by https://leetcode.com/problems/climbing-stairs/discuss/25299/Basically-it's-a-fibonacci.
"""

# accepted solution
class Solution:
    def __init__(self):
        self.dic = {1: 1, 2: 2}
    
    def climbStairs(self, n: int) -> int:
        if n not in self.dic:
            self.dic[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.dic[n]


# another method - for n < 35

def climbStairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        return climbStairs(n - 1) + climbStairs(n - 2)