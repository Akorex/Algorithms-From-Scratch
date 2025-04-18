"""
Solution to Leetcode problem #116 - Populating next right pointers in each node

https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

"""
from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        head = root

        while head.left:
            curr = head
            while curr:
                curr.left.next = curr.right
                if curr.next:
                    curr.right.next = curr.next.left
                curr = curr.next
            head = head.left

        return root