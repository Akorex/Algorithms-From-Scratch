"""
Solution to Leetcode problem #138 - Copy List with Random Pointer

https://leetcode.com/problems/copy-list-with-random-pointer/description

"""

# initial solution
from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        old_to_new = {}
        curr = head
        start = head
    
        while curr:
            old_to_new[curr] = Node(x = curr.val, next = None, random = None)
            curr = curr.next
    
        for old_node, new_node in old_to_new.items():
            if old_node.next:
                next_node = old_to_new[old_node.next]
                new_node.next = next_node
    
            if old_node.random:
                random_node = old_to_new[old_node.random]
                new_node.random = random_node
        return old_to_new[start]
    

# second solution

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        hash_map = {}
        curr = head


        # traverse the linked-list and make new nodes
        while curr:
            hash_map[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            copied_node = hash_map[curr]
            copied_node.next = hash_map.get(curr.next)
            copied_node.random = hash_map.get(curr.random)
            curr = curr.next
        
        return hash_map[head]