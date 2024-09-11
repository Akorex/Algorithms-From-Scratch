"""
Solution to Leetcode problem # 228 -Summary Ranges

https://leetcode.com/problems/summary-ranges/description/
"""
from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [f"{nums[0]}"]

        ans = []
        left = start = nums[0]

        for num in nums[1:]:
            if num - left != 1:
                ans.append(f"{start}->{left}" if left - start > 0 else f"{left}")
                start = num
            left = num
        ans.append(f"{start}->{left}" if left - start > 0 else f"{left}")
        return ans
    
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        idx, ans = 0, []

        while idx < len(nums):
            start = nums[idx]
            while idx < len(nums) - 1 and nums[idx] == nums[idx + 1] - 1:
                idx += 1
            stop = nums[idx]

            if start != stop:
                ans.append(f"{str(start)} -> {str(stop)}")
            else:
                ans.append(str(stop))
            
            idx += 1
        return ans