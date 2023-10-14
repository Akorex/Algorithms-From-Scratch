"""
Solution to Leetcode problem #202 - Happy Number

https://leetcode.com/problems/happy-number/description/
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1 or n == 7:
            return True            
        elif len(str(n)) == 1:
            return False
        else:
            s = 0
            for i in str(n):
                s += int(i) ** 2
            if s == 1:
                return True
            else:
                return self.isHappy(s)
            
## another approach
class Solutionn:
    def isHappy(self, n):
        hset = set()

        while n!= 1:
            if n in hset:
                return False
            hset.add(n)
            n = sum([int(i) ** 2 for i in str(n)])
        else:
            return True