"""Solution to Leetcode problem #286 - Missing Number

Given an array nums containing n distinct numbers in the range [0, n], 
return the only number in the range that is missing from the array.

"""

# naive solution 
def missingNumber(nums):
    for i in range(len(nums) + 1):
        if i not in nums:
            return i


## alternative approach
def missingNumber(nums):
    return sum(range(len(nums) + 1)) - sum(nums)