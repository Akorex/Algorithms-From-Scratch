"""
Solution to Leetcode problem #209 - Minimum Size Subarray Sum

https://leetcode.com/problems/minimum-size-subarray-sum/description/

"""
from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0

        left = 0 # starting index of window
        right = 0 # ending index of window
        window_sum = 0
        ans = float('inf')

        for right in range(len(nums)):
            window_sum += nums[right]

            while window_sum >= target:
                ans = min(ans, right - left + 1)
                window_sum -= nums[left]
                left += 1
        return ans if ans != float('inf') else 0
    


# alternative approach
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        
        # indices of the window
        start = 0
        end = 0
        window_sum = 0
        ans = len(nums) + 1

        for end in range(len(nums)):
            window_sum += nums[end]

            while window_sum >= target and start <= end:
                ans = min(ans, end - start + 1)
                window_sum -= nums[start]
                start += 1

        return ans
