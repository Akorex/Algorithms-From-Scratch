from linkedbinarytree import LinkedBinaryTree
from maps import MapBase

class TreeMap(LinkedBinaryTree, MapBase):
    """Sorted map implementation using a binary search tree"""
    
    #-------------nested class-----------------------------
    class Position(LinkedBinaryTree.Position):
        """An abstraction for representing the position of a single element"""
        def key(self):
            """Return key of map's key-value pair"""
            return self.element()._key

        def value(self):
            """Return the value of map's key-value pair"""
            return self.element()._value

    #-------------nonpublic utility methods-------------------
    def _subtree_search(self, p, k):
        """Return Postiion p's subtree having key, k or last node searched"""
        if k == p.key():
            return p
        elif k < p.key():
            if self.left(p) is not None:
                return self._subtree_search(self.left(p), k)
        elif k > p.key():
            if self.right(p) is not None:
                return self._subtree_search(self.right(p), k)
        
        return p

    def _subtree_first_position(self, p):
        """Return position of first item in subtree rooted at p"""
        walk = p
        while self.left(walk) is not None:
            walk = self.left(walk)
        return walk

    def _subtree_last_position(self, p):
        """Return position of last item in subtree rooted at p"""
        walk = p
        while self.right(p) is not None:
            walk = self.right(walk)
        return walk

    
    def first(self):
        """Return first Position in the tree (or None if tree is empty)"""
        return self._subtree_first_position(self.root()) if len(self) > 0 else None

    def last(self):
        """Return last Position in the tree (or None if tree is empty)"""
        if len(self) > 0:
            return self._subtree_last_position(self.root())
        else:
            return None

    def before(self, p):
        """Return the Position just before p in the natural order
        
        Return None if p is the first position
        """
        self._validate(p)
        if self.left(p):
            return self._subtree_last_position(self.left(p))
        else:
            # walk upward
            walk = p
            above = self.parent(p)
            while above is not None and walk == self.left(above):
                walk = above
                above = self.parent(walk)
            return above

    def after(self, p):
        """Return the Position just after p in the natural order
        
        Return None if p is the last position
        """
        self._validate(p)
        if self.right(p):
            return self._subtree_first_position(self.right(p))
        else:
            walk = p
            above = self.parent(p)
            while above is not None and walk == self.right(above):
                walk = above
                above = self.parent(walk)
            return above

    def find_position(self, k):
        """Return Position with key k, or else neighbor or None if empty"""
        if self.is_empty():
            return None
        else:
            p = self._subtree_search(self.root(), k)
            self._rebalance_access(p)
            return p

    def _rebalance_access(self, p):
        """Rebalance tree after access of a position"""
        pass

    def _rebalance_insert(self, p):
        """Rebalance tree after insertion of a position"""
        pass

    def _rebalance_delete(self, p):
        """Rebalance tree after deletion of a position"""
        pass

    def find_min(self):
        """Return (key, value) pair with minimum key (or None if empty)"""
        if self.is_empty():
            return None
        else:
            p = self.first()
            return (p.key(), p.value())

    def find_ge(self, k):
        """Return (key, value) pair with the least key greater than or equal to k"""
        if self.is_empty():
            return None
        else:
            p = self.find_position(k)
            if p.key() < k:
                p = self.after(p)
            return (p.key(), p.value()) if p is not None else None

    def find_gt(self, k):
        """Return (key, value) pair with the least key strictly greater than k"""
        if self.is_empty():
            return None
        else:
            p = self.find_ge(k)
            return (p.key(), p.value()) if p is not None and p.key() != k else None

    def find_le(self, k):
        """Return (key, value) pair with the greatest key less than or equal to k"""
        if self.is_empty():
            return None
        else:
            p = self.find_position(k)
            if p.key() > k:
                p = self.before(p)
            return (p.key(), p.value()) if p is not None else None

    def find_lt(self, k):
        """Return (key, value) pair with the greatest key strictly less than k"""
        if self.is_empty():
            return None
        else:
            p = self.find_le(k)
            return (p.key(), p.value()) if p is not None and p.key() != k else None

    def find_range(self, start, stop):
        """Iterate all (key, value) pairs such that start <= key < stop.
        
        If start is None, iteration begins with minimum key of map.
        If stop is None, iteration comes through the maximum key of map
        """
        if not self.is_empty():
            if start is None:
                p = self.first()

        else:
            p = self.find_position(start)
            if p.key() < start:
                p = self.after(p)
            while p is not None and (stop is None or p.key() < stop):
                yield (p.key(), p.value())
                p = self.after(p)

    def __getitem__(self, k):
        """Return the value associated with key k (or return KeyError if key not found)"""
        if self.is_empty():
            raise KeyError('Key Error: ' + repr(k))
        else:
            p = self._subtree_search(self.root(), k)
            self._rebalance_access(p)
            if k != p.key():
                raise KeyError('Key Error: ' + repr(k))
            return p.value()

    def __setitem__(self, k, v):
        """Assign value v to key k, overwritig existing value if present"""
        if self.is_empty():
            leaf = self._add_root(self._Item(k, v))
        else:
            p = self._subtree_search(self.root(), k)
            if p.key() == k:
                p.element()._value = v
                self._rebalance_access(p)
                return 
            else:
                item = self._Item(k, v)
                if p.key() < k:
                    leaf = self._add_right(p, item)
                else:
                    leaf = self._add_left(p, item)
        self._rebalance_insert(leaf)

    def __iter__(self):
        """Generate an iteration of all keys in the map in order"""
        p = self.first()
        while p is not None:
            yield p.key()
            p = self.after(p)

    def delete(self, p):
        """Remove the item at a given Position"""
        self._validate(p)
        if self.left(p) and self.right(p): # has two children
            replacement = self._subtree_last_position(self.left(p))
            self._replace(p, replacement.element())
            p = replacement
        # now p has at most one child
        parent = self.parent(p)
        self._delete(p)
        self._rebalance_delete(parent)

    def __delitem__(self, k):
        """Remove item associated with key k (or raise KeyError if not found)"""
        if not self.is_empty():
            p = self._subtree_search(self.root(), k)
            if p.key() == k:
                self.delete(p)
                return p
            self._rebalance_access(p)
        raise KeyError('Key Error: ' + repr(k))

    def _relink(self, parent, child, make_left_child):
        """Relink parent node with child node (which may be None)"""
        if make_left_child:
            parent._left = child
        else:
            parent._right = child
        if child is not None:
            child._parent = parent

    def _rotate(self, p):
        """Rotate Position p above its parent"""
        x = p._node
        y = x._parent
        z = y._parent
        if z is None:
            self._root = x
            x._parent = None
        else:
            self._relink(z, x, y == z._left) # x becomes a direct child of z
        # now rotate x and y, including transfer of middle subtree
        if x == y._left:
            self._relink(y, x._right, True) # x._right becomes left child of y
            self._relink(x, y, False) # y becomes right child of x
        else:
            self._relink(y, x._left, False)
            self._relink(x, y, True)

    
    def _restructure(self, x):
        """Perform trinode restructure of Position x with parent/grandparent"""
        y = self.parent(x)
        z = self.parent(y)

        if (x == self.right(y)) == (y == self.right(z)):
            self._rotate(y)
            return y
        else:
            self._rotate(x)
            self._rotate(x)
            return x