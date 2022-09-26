class Node:
    def __init__(self, element, next):
        self._element = element
        self._next = next

class LinkedList:
    """Implementation of a singly-linked list that removes duplicates"""

    def __init__(self):
        self.head = None

    def remove_dups(self):
        ptr1 = None
        ptr2 = None
        dup = None
        ptr1 = self.head

        while ptr1 != None and ptr1.next != None :
            ptr2 = ptr1

            # compare the picked element with the rest
            while ptr2.next = 
