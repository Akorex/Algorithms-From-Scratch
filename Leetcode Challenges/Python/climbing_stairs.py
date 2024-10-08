"""
solution to leetcode problem #70 - Climbing stairs
https://leetcode.com/problems/climbing-stairs/

"""

class Solution:
    def __init__(self):
        self.dic = {1:1, 2:2}
    def climbStairs(self, n: int) -> int:
        if n not in self.dic:
            self.dic[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.dic[n]