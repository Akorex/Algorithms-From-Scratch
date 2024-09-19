""""
Solution to Leetcode problem #9 - Palindrome Number

https://leetcode.com/problems/palindrome-number/description/

"""

# initial (but trivial attempt) 

class Solution:
    def isPalindrome(self, x: int) -> bool:
        xx = str(x)

        return xx[:] == xx[::-1]
    


# solution with more steps
class Solutionn:
    def isPalindrome(self, x:int) -> bool:
        # edge cases
        if x < 0:
            return False
        if x == 0:
            return True
        
        strg_x = str(x)

        if int(strg_x[-1]) == 0:
            return False
        
        reverse = strg_x[::-1]
        if int(reverse) == x:
            return True
        else: 
            return False