"""Solution to Leetcode problem #448 - Find all numbers that disappeared in an array

"""

# initial approach - not working
def findMissingNumbers(nums):
    ans = []
    nums = set(nums)

    for i in range(1, len(nums) + 1):
        if i not in nums:
            ans.append(i)
    return ans


def findDisappearedNumbers(nums):
    for i in range(len(nums)):
        temp = abs(nums[i]) - 1
        if nums[temp] > 0:
            nums[temp] *= -1

    ans = []
    for i, num in enumerate(nums):
        if num > 0:
            ans.append(i + 1)
    return ans

if __name__ == '__main__':
    lis = [1, 2, 3, 5]
    print(findDisappearedNumbers(lis))