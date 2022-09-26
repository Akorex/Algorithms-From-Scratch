"""
Solution to Leetcode problem #203 - Remove LinkedList Elements

"""
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

from typing import Optional

# brute force method, doesn't work
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        ll = dummy = head
        data = []
        ans = []
        
        
        # get all the elements of the linked list to a list
        while ll:
            data.append(ll.val)
            ll = ll.next
        
        for i in range(len(data)):
            if data[i] != val:
                ans.append(data[i])
        
        for i in range(len(ans)):
            dummy.val = ans[i]
            dummy = dummy.next
        
        return dummy


# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy_head = ListNode(-1)
        dummy_head.next = head
        
        current_node = dummy_head
        while current_node.next != None:
            if current_node.next.val == val:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next
                
        return dummy_head.next