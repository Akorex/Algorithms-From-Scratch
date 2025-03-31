"""
Solution to Leetcode problem #445 - Add two numbers II

https://leetcode.com/problems/add-two-numbers-ii/description/

"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        r1 = self.reverse(l1)
        r2 = self.reverse(l2)

        result = ListNode(0)
        curr = result
        carry = 0

        while r1 is not None or r2 is not None or carry != 0:
            r1_val = r1.val if r1 else 0
            r2_val = r2.val if r2 else 0
            col_sum = r1_val + r2_val + carry

            carry, rem = divmod(col_sum, 10)

            remNode = ListNode(rem)
            curr.next = remNode
            curr = remNode

            r1 = r1.next if r1 else None
            r2 = r2.next if r2 else None
        ans = self.reverse(result.next)
        return ans



        



    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            
            curr.next = prev
            
            prev = curr
            curr = next_node
        return prev

        
      