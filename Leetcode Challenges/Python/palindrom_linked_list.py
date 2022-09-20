"""Solution to Leetcode problem #234 - Palindrome Linked List

https://leetcode.com/problems/palindrome-linked-list/

Helpfu link - https://leetcode.com/problems/palindrome-linked-list/discuss/64500/11-lines-12-with-restore-O(n)-time-O(1)-space
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

# initial approach
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        data = []
        link = head
        
        while link:
            data.append(link.val)
            link = link.next
        
        if data == data[::-1]:
            return True
        else:
            return False

# another approach - not very clear yet
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next

        if fast:
            # fast is at the end, move slow one step further for comparison(cross middle one)
            slow = slow.next
        
        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next

        # if equivalent then rev become None, return True; otherwise return False 
        return not rev