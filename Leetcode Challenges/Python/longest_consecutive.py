"""
Solution to Leetcode problem #

"""

from typing import List


# naive solution; not O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums.sort()
        
        curr_streak = 1
        longest_streak = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            elif nums[i] == nums[i-1] + 1:
                curr_streak += 1
            else:
                longest_streak = max(curr_streak, longest_streak)
                curr_streak = 1
        
        return max(longest_streak, curr_streak)
    

# satisfies in O(1) as required
    
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        num_set = set(nums)
        longest_streak = 0

        for num in num_set:
            # check if start of sequence
            if num-1 not in num_set:
                curr = num
                curr_streak = 1
                
                while curr + 1 in num_set:
                    curr += 1
                    curr_streak += 1
                longest_streak = max(curr_streak, longest_streak)
        
        return longest_streak