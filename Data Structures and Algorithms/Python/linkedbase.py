class _DoublyLinkedBase:
    """A nonpublic base class providing linked list representation"""
    class _Node:
        """Lightweight, nonpublic class for storing a node"""
        __slots__ = '_element', '_next', '_prev'
        def __init__(self, element, prev, next):
            self._element = element
            self._next = next
            self._prev = prev

    def __init__(self):
        """Initializes an empty doubly linked list"""
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        """Add an element between two existing nodes and return new node"""
        newest = self._Node(e, predecessor._next, successor._prev)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        """Delete a nonsentinel node and return its element"""
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        element = node._element
        node._prev = node._next = node._element = None
        self._size -= 1
        return element