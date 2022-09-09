# define the empty exception class
class Empty(Exception):
    pass

class ArrayStack:
    """A LIFO ADT implementatation using python list as underlying storage"""

    def __init__(self):
        """Create an empty stack"""
        self._data = []
    
    def __len__(self):
        return len(self._data)
    
    def is_empty(self):
        """Returns True if no element in the stack"""
        return len(self._data) == 0

    def push(self, e):
        """Adds an element e to the top of the stack"""
        self._data.append(e)

    def pop(self):
        """Returns and remove the element at the top of the stack
        
        Returns Empty Exception if the stack is empty
        """
        if self.is_empty():
            raise Empty("The stack is empty.")
        return self._data.pop()

    def top(self):
        """Returns but does not remove the element at the top of the stack.
        
        Returns Empty Exception is the stack is empty
        """
        if self.is_empty():
            raise Empty("The stack is empty.")
        return self._data[-1]

    def __str__(self):
        """Returns a string representation of the current stack in memory"""
        return f"Stack: {self._data}"

class LinkedStack:
    """A LIFO ADT implementation using a singly-linked list as underlying storage"""

#--------------non-public utility-------------------------------------------
    class _Node:
        """Non-public class for storing a node"""
        __slots__ = '_element', '_next'
        def __init__(self, element, next):
            self._element = element
            self._next = next

#--------------------stack methods------------------------------------------------
    def __init__(self):
        """Initializes the stack"""
        self._head = None
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    def push(self, e):
        """Add an element e to the top of the stack"""
        self._head = self._Node(e, self._head)
        self._size += 1

    def pop(self):
        """Return and remove an element from the top of the stack. 
        
        Returns Empty exception if the stack is empty
        """
        if self.is_empty():
            raise Empty("The stack is empty.")
        ans = self._head._element
        self._head = self._head._next
        self._size -= 1
        return ans

    def top(self):
        """Return (but do not remove) an element from the top of the stack.
        
        Returns Empty exception if the stack is empty
        """
        if self.is_empty():
            raise Empty("The stack is empty.")
        return self._head._element

if __name__ == '__main__':
    s = ArrayStack()
    print(s.is_empty())
    s.push(2)
    s.push(3)
    print(s.top())
    print(s.is_empty())
    print(len(s))
    print(str(s))

    s = LinkedStack()
    print(s.is_empty())
    s.push(2)
    s.push(3)
    print(s.top())
    print(s.is_empty())
    print(len(s))