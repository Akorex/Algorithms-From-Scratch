"""
Solution to Leetcode problem #27 - Remove Elements

"""
from typing import List

# follows the code instruction but doesn't solve issue as intended
def removeElement(nums: List[int], val: int) -> int:
    de = []
        
    for num in nums:
        if num != val:
            de.append(num)

    return len(de)


# don't do this - O(n^2) solution
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for _ in range(len(nums)):
            nums.remove(val)
        return len(nums)

# better approach
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0

        for num in nums:
            if num != val:
                nums[count] = num
                count += 1
        return count


# even better
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        start, end = 0, len(nums) - 1

        while start <= end:
            if nums[start] == val:
                nums[start], nums[end], end = nums[end], nums[start], end - 1
            else:
                start += 1
        return start
