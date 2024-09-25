"""
Solution to Leetcode problem #98 - Validate Binary Search Tree

https://leetcode.com/problems/validate-binary-search-tree/description/
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self._validate_bst(root, float("-inf"), float("inf"))
        
    def _validate_bst(self, node, minimum, maximum):
        if not node:
            return True
        
        if not (node.val > minimum and node.val < maximum):
            return False
        
        return self._validate_bst(node.left, minimum, node.val) and self._validate_bst(node.right, node.val, maximum)