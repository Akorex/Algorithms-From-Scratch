"""
Solution to Leetcode problem #876 - Middle of the Linked List
https://leetcode.com/problems/middle-of-the-linked-list/

Helpful soln - https://leetcode.com/problems/middle-of-the-linked-list/discuss/1651600/PythonJavaC%2B%2B-Simple-Solution-oror-One-Pass-oror-Beginner-Friendly-oror-Detailed-Explanation

"""
import math
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


# preferred approach
def middleNode(head):
    # While slow moves one step forward, fast moves two steps forward.
    # Finally, when fast reaches the end, slow happens to be in the middle of the linked list.
    slow = fast = head 
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

# bruteforce
def middleNode(head):
    length = 0
    count = 0
    curr = head

    while curr:
        length += 1
        curr = curr.next

    if length == 1:
        return head

    mid = int(math.floor(length / 2))

    while head:
        count += 1
        head = head.next
        if count == mid:
            return head

    return None