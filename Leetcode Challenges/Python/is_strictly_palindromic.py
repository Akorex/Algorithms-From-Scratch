"""
Solution to Leetcode problem #2396 - Strictly Palindromic Number 

https://leetcode.com/problems/strictly-palindromic-number/
"""


#There are only two numbers that are palindromes in any base — these are the numbers 0 and 1.

#The number 0 is represented as "0" in all numeral systems, and it is always a palindrome. 
# The number 1 is represented as "1" in all numeral systems, and it is also always a palindrome. 
# For all other numbers, there will be at least one base in which the number is not a palindrome.

class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        return False