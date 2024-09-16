"""
Solution to problem 8.3 - Magic Index from CtCI 

A magic index in an array A [ 0 ••• n -1] is defined to be an index such that A[ i] = 
i. Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in
 array A.

"""

class Solution:
    def magic_index(self, nums):
        for i in range(len(nums)):
            if nums[i] == i:
                return i
        return -1 
    


if __name__ == '__main__':
    lst = [1, 2, 3, 4]
    sol = Solution()
    print(sol.magic_index(lst))           
