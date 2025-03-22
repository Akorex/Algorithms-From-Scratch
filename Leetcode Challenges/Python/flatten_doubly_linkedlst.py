"""
Solution to Leetcode problem #430 - Flatten a multilevel doubly linked list

https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/

"""
from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        curr = head
        while curr:
            # if the list has a child, we need to 
            # do some reordering for flattening. else, we continue
            if curr.child is not None:
                self.merge(curr)
            curr = curr.next
        return head

    def merge(self, curr):
        child = curr.child

        # move to the last child
        while child.next is not None:
            child = child.next

        # make the last child.next come after curr
        if curr.next is not None:
            child.next = curr.next
            curr.next.prev = child
        # let curr.next be the child
        curr.next = curr.child
        curr.child.prev = curr

        # set the child to None to remove it.
        curr.child = None