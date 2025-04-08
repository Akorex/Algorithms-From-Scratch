"""
Solution to Leetcode problem #144 - Binary Tree Preorder Traversal

https://leetcode.com/problems/binary-tree-preorder-traversal/description/


"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.result = []

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        self.result.append(root.val)

        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)

        return self.result
    


# better rewritten

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def traverse(node):
            if not node:
                return
            
            result.append(node.val)
            traverse(node.left)
            traverse(node.right)

        traverse(root)
        return result