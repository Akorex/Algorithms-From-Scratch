"""
Solution to Leetcode problem #2 - Add two numbers


https://leetcode.com/problems/add-two-numbers/

"""

from typing import Optional

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    result = ListNode(0) # create a node to store result
    curr = result
    carry_next = 0  # initialize carry to 0

    while l1 is not None or l2 is not None or carry_next != 0:
        # perform the addition
        l1_val = l1.val if l1 else 0
        l2_val = l2.val if l2 else 0
        column_sum = l1_val + l2_val + carry_next
        carry_next, rem = divmod(column_sum, 10) # get the quotient & remainder

        # make a new node to hold add_result & pass to next step
        newNode = ListNode(rem)
        curr.next = newNode
        curr = newNode

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return result.next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(0)
        curr = ans
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            col_sum = l1_val + l2_val + carry

            carry, rem = divmod(col_sum, 10)

            remNode = ListNode(rem)
            curr.next = remNode
            curr = remNode

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return ans.next 