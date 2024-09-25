class Tree:
    """Abstract base class representing a tree structure"""

    class Position:
        """An abstraction representing the location of a single element"""
        def element(self):
            raise NotImplementedError("must be implemented by subclass")
        
        def __eq__(self, other):
            raise NotImplementedError("must be implemented by subclass")
        
        def __ne__(self, other):
            raise NotImplementedError("must be implemented by subclass")
        
    def root(self):
        """Return Position representing the tree's root or None if empty"""
        raise NotImplementedError("must be implemented by subclass")
    
    def parent(self, p):
        """Return the Position representing the parent of p (or None if p is root)"""
        raise NotImplementedError("must be implemented by subclass")
    
    def num_children(self, p):
        """Return the number of children position p has"""
        raise NotImplementedError("must be implemented by subclass")
    
    def children(self, p):
        """Generate an iteration of Positions representing P's children"""
        raise NotImplementedError("must be implemented by subclass")
    
    def __len__(self):
        """Generate the total number of elements in the tree"""
        raise NotImplementedError("must be implemented by subclass")
    
    def is_root(self, p):
        return self.root() == p
    
    def is_leaf(self, p):
        return self.num_children(p) == 0
    
    def is_empty(self):
        return len(self) == 0
    
    def depth(self, p):
        """Return the number of lebels separating Position p from root"""
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))
    
    def _height(self, p):
        """Return the height of the subtree rooted at Position p"""

        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height(c) for c in self.children(p))
        
    def height(self, p = None):
        if p is None:
            p = self.root()
        return self._height(p)
    
    def __iter__(self):
        """Generate an iteration of the tree's elements"""
        for p in self.positions():
            yield p.element()

    def preorder(self):
        """Generate a preorder iteration of positions in the tree"""
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
                yield p

    def _subtree_preorder(self, p):
        yield p

        for c in self.children(p):
            for other in self._subtree_preorder(c):
                yield other

    def positions(self):
        return self.preorder()
    
    def postorder(self):
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):
                yield p

    def _subtree_postorder(self, p):
        for c in self.children(p):
            for other in self._subtree_postorder(c):
                yield other
        yield p

    def inorder(self):
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p

    def _subtree_inorder(self, p):
        if self.left(p) is not None:
            for other in self._subtree_inorder(self.left(p)):
                yield other
        yield p

        if self.right(p) is not None:
            for other in self._subtree_inorder(self.right(p)):
                yield other
    