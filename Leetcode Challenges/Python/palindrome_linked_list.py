"""
Solution to Leetcode problem #234 - Palindrome Linked List

https://leetcode.com/problems/palindrome-linked-list/description/

"""



from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
            
        clone = self.clone(head)    
        other = self.reverse(clone)

        while head:
            if head.val != other.val:
                return False
            head = head.next
            other = other.next
        return True
        


    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        last = None
        curr = head
        
        while curr:
            next_node = curr.next

            curr.next, last = last, curr

            curr = next_node
        return last

    def clone(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        clone = None
        clone_tail = None

        while curr:
            new_node = ListNode(curr.val)
            if not clone:
                clone = clone_tail = new_node
            else:
                clone_tail.next = new_node
                clone_tail = clone_tail.next
            curr = curr.next
        return clone
