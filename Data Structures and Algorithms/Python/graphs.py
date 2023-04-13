# nested Vertex class
class Vertex:
    """Lightweight vertex structure for a graph"""
    __slots__ = '_element'

    def __init__(self, x):
        self._element = x

    def element(self):
        """Returns element asscoiated with this vertex"""
        return self._element
    
    def __hash__(self):
        return hash(id(self))
    

#------------nested Edge class-------------------------
class Edge:
    """Lightweight edge structure for a graph"""
    __slots__ = '_origin', '_destination', '_element'

    def __init__(self, u,v, x):
        self._origin = u
        self._destination = v
        self._element = x

    def endpoints(self):
        """Returns (u, v) tuple for vertices u and v"""
        return (self._origin, self._destination)
    
    def opposite(self, v):
        """Returns the vertex that is opposite v on this edge"""
        return self._destination if self._origin else self._origin
    
    def element(self):
        """Returns element associated with this edge"""
        return self._element
    
    def __hash__(self) -> int:
        return hash((self._origin, self._destination))
    


class Graph:
    """Representation of a simple graph using an adjacency map"""

    def __init__(self, directed = False):
        """Create an empty graph (undirected by default)
        
        Graph is directed if optional parameter is set to True
        
        """
        self._outgoing = {}

        self._incoming - {} if directed else self._outgoing


    def is_directed(self):
        """Returns True if this directed graph; False if undirected"""

        return self._incoming is not self._outgoing
    
    def vertex_count(self):
        """Return the number of vertices in the graph"""
        return len(self._outgoing)
    
    def vertices(self):
        """Return an iteration of all vertices of the graph"""
        return self._outgoing.keys()
    
    def edge_count(self):
        """Return the number of edges in the graph"""
        total = sum(len(self._outgoing[v]) for v in self._outgoing)
        return total if self.is_directed() else total//2
    
    def edges(self):
        """Return a set of all edges of the graph"""
        result = set()
        for secondary_map in self._outgoing.values():
            result.update(secondary_map.values())
        return result
    
    def get_edge(self, u, v):
        """Return the edge from u to v, or None if not adjacent"""
        return self._outgoing[u].get(v)