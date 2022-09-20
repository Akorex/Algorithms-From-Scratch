# implementing a Stack ADT with a singly-linked list
from stack import Empty

class LinkedStack:
    """LIFO Stack implementation using a singly linked list for storage"""
    #-----------nested _Node class-------------------------
    class _Node:
        """Lightweight non-public class for storing a singly linked node"""
        __slots__ = '_element', '_next'
        
        def __init__(self, element, next):
            self._element = element
            self._next = next

    #-----------------stack methods ---------------------------
    def __init__(self):
        """Create an empty stack"""
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        """Adds element e to the top of the stack"""
        self._head = self._Node(e, self._head) # create and link a new node
        self._size += 1

    def pop(self):
        """Removes and returns the last element from the top of the stack
        Raises Empty if the stack is empty
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer

    def top(self):
        """Returns but do not remove the element at the top of the stack
        
        Rasies Empty exception if the stack is empty
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        answer = self._head._element
        return answer

# implementation of a Queue ADT using a singly-linked list
class LinkedQueue:
    """FIFO implementation using a singly-linked list as underlying storage"""

    #-------------nested class --------------------
    class _Node:
        """Lightweight, nonpublic utility class for storing a singly linked node"""
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    #-------------------- Queue methods-----------------------------

    def __init__(self):
        """Create an empty queue"""
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def enqueue(self, e):
        """Adds an element at the back of the queue"""
        newest = self._Node(e, None) # create a node
        if self.is_empty():
            self._head = newest # if empty, node is the head
        else:
            self._tail._next = newest # else, link the node to the next of the list's tail
        self._tail = newest # update the reference
        self._size += 1

    def first(self):
        """Returns but do not remove the element at the front of the queue
        Raise Empty exception if the queue is empty
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._head._element
        return answer

    def dequeue(self):
        """Returns and removes the element at the front of the queue
        Raise Empty exception if the queue is empty
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty(): # special case if queue is empty
            self._tail = None # removed head had been tail
        return answer

class CircularQueue:
    """FIFO implementation using a circular linked list for underlying storage"""
    #---------------nested class----------------------------
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    #----------------------Queue methods---------------------------
    
    def __init__(self):
        """Create an empty Queue"""
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        """Return but do not remove the element at the front of the queue
        Raise Empty exception if the queue is empty
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._tail._next._element
        return answer

    def enqueue(self, e):
        """Adds element e at the back of the queue"""
        newest = self._Node(e, None) # create a node
        if self.is_empty():
            newest._next = newest # circularly point to itself
        else:
            newest._next = self._tail._next # points to head
            self._tail._next = newest # old tail points to new node
        self._tail = newest
        self._size += 1

    def dequeue(self):
        """Return and remove the element at the front of the queue
        Raise Empty Exception if the queue is empty
        """
        if self.is_empty():
            return Empty('Queue is empty')
        oldhead = self._tail._next
        if self._size == 1: # queue only contains 1 element
            self._tail = None # queue becomes empty
        else:
            self._tail._next = oldhead._next # bypass the oldhead
        self._size -= 1
        return oldhead._element

    def rotate(self):
        """Rotate front element to the back of the queue"""
        if self._size > 0:
            self._tail = self._tail._next


# nonpublic class offerring support for doubly-linked lists
class _DoublyLinkedBase:
    """A base class providing doubly-linked list representation"""
    
    #-----------------nested class----------------------------
    class _Node:
        """Lightweight, nonpublic class for storing a doubly-linked node"""
        __slots__ = '_element', '_next', '_prev'
        
        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next

    #--------------------class methods----------------------------
    def __init__(self):
        """Create an empty list"""
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._trailer._prev = self._header # header is before trailer
        self._header._next = self._trailer # traier is after header
        self._size = 0 # counts the number of elements

    def __len__(self):
        return self._size

    def is_empty(self):
        """Return True if the list is empty"""
        return self._size == 0

    def _insert_betweeen(self, e, predecessor, successor):
        """Add element e in between two nodes and return new node"""
        newest = self._Node(e, predecessor, successor) # create and link
        predecessor._next = newest 
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        """Delete nonsentinel node from the list and return its element"""
        predecessor = node._prev
        successor = node._next
        
        # bypass current node
        predecessor._next = successor
        successor._prev = predecessor

        element = node._element
        self._size -= 1
        node._prev = node._next = node._element = None # deprecate the node
        return element

# implementation of a Deque ADT using doubly-linked lists as underlying storage

class LinkedDeque(_DoublyLinkedBase): #inherited class

    def first(self):
        """Returns but do not remove the element at the front of the deque
        Raise Empty exception if the deque is empty
        """
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._header._next._element

    def last(self):
        """Returns but do not remove the element at the back of the deque
        Raise Empty exception if the deque is empty
        """
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._trailer._prev._element

    def add_first(self, e):
        """Adds an element e to the front of the deque"""
        self._insert_betweeen(e, self._header, self._header._next)

    def add_last(self, e):
        """Adds an element e to the back of the deque"""
        self._insert_betweeen(e, self._trailer._prev, self._trailer)

    def delete_first(self):
        """Return and remove the element at the front of the deque
        Raise Empty Exception if the deque is empty
        """
        if self.is_empty():
            return Empty('Deque is empty')
        return self._delete_node(self._header._next)

    def delete_last(self):
        """Remove and return the element at the back of the deque
        Raise Empty Exception if the deque is empty
        """
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._delete_node(self._trailer._prev)


if __name__ == '__main__':
    print('Stack')
    s = LinkedStack()
    print(s.is_empty())
    s.push(2)
    s.push(3)
    print(s.top())
    print(s.is_empty())
    print(len(s))
    s.pop()
    print(s.top())

    print('\nQueue')
    q = LinkedQueue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print(len(q))
    q.dequeue()
    print(q.is_empty())
    print(q.first())
    print(len(q))

    print('\nCircular Queue')
    q = CircularQueue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print(len(q))
    q.dequeue()
    print(q.is_empty())
    print(q.first())
    print(len(q))

    print('\nDeque')
    d = LinkedDeque()
    d.add_first(5)
    d.add_last(6)
    print(d.is_empty())
    d.add_first(6)
    d.add_last(2)
    print(d.last())
    d.delete_last()
    print(d.last())
    print(d.first())
    print(len(d))