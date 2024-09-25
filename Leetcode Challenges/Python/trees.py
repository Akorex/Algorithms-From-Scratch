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