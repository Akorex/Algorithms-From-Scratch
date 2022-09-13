"""Solution to Leetcode #136 - Single Number"""
def singleNumber(nums):
    # the approach is to use a dictionary to store the counts
    dic = {}
    for num in nums:
        dic[num] = dic.get(num, 0) + 1

    for key, val in dic.items():
        if val == 1:
            return key