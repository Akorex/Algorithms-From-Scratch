"""
Solution to Leetcode problem #989 - Add to Array-Form of Integer

https://leetcode.com/problems/add-to-array-form-of-integer/description/
"""


from typing import List
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        st = int(''.join(map(str, num))) + k
        return [int(i) for i in str(st)]