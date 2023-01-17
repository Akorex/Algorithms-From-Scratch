from collections import MutableMapping
from random import randrange

class MapBase(MutableMapping):
    """Abstract base class that includes a nonpublic _Item class"""
    #-----------nested class-------------------------------------------
    class _Item:
        """Lightweoght composite to store key-value pairs as map items"""
        __slots__ = '_key', '_value'

        def __init__(self, key, value):
            self._key = key
            self._value = value

        def __eq__(self, other):
            return self._key == other._key

        def __ne__(self, other):
            return not (self == other)

        def __lt__(self, other):
            return self._key < other._key

        def __gt__(self, other):
            return self._key > other._key

    
class UnsortedTableMap(MapBase):
    """Map implementation using an unordered list"""
    
    def __init__(self):
        """Create an empty map"""
        self._table = []

    def __getitem__(self, k):
        """Return value associated with key k (or raise KeyError if not found)"""
        for item in self._table:
            if k == item._key:
                return item._value
        raise KeyError('Key Error: ' + repr(k))

    def __setitem__(self, k, v):
        """Assign value v to key k, overwriting existing value if present"""
        for item in self._table:
            if k == item._key:
                item._value = v
                return 
        # gets here if k not in the map    
        self._table.append(self._Item(k, v))

    def __delitem__(self, k):
        """Remove item associated with key k (or raise KeyError if not found)"""
        for j in range(len(self._table)):
            if k == self._table[j]._key:
                self._table.pop(j)
                return
        raise KeyError('Key Error: ' + repr(k))

    def __len__(self):
        return len(self._table)

    def __iter__(self):
        """Generate an iteration of the map's keys"""
        for item in self._table:
            yield item._key


class HashMapBase(MapBase):
    """Abstract base class for map using hash-tables with MAD compression"""

    def __init__(self, cap=11, p = 109345121):
        """Create an empty hash-table map"""
        self._table = cap * [None]
        self._n = 0 # number of entries in the mao
        self._prime = p
        self._scale = 1 + randrange(p - 1)
        self._shift = randrange(p)


    def __len__(self):
        return self._n

    def _hash_function(self, k):
        return (hash(k)*self._scale + self._shift)% self._prime % len(self._table)

    def __getitem__(self, k):
        j = self._hash_function(k)
        return self._bucket_getitem(j, k)

    def __setitem__(self, k, v):
        j = self._hash_function(k)
        self._bucket_setitem(j, k, v)
        if self._n > len(self._table) // 2:
            self._resize(2 * len(self._table) - 1)

    def __delitem__(self, k):
        j = self._hash_function(k)
        self._bucket_delitem(j, k)
        self._n -= 1

    def _resize(self, c):
        old = list(self.items())
        self._table = c * [None]
        self._n = 0
        for (k, v) in old:
            self[k] = v


class ChainHashMap(HashMapBase):
    """Hash map implemented with separate chaining for collision resolution"""
    def _bucket_getitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error: ' + repr(k))
        return bucket[k]

    def _bucket_setitem(self, j, k, v):
        if self._table[j] is None:
            self._table[j] = UnsortedTableMap() # bucket is new to the table
        oldsize = len(self._table[j])
        self._table[j][k] = v
        if len(self._table[j]) > oldsize: # key was new to the table
            self._n += 1

    def _bucket_delitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error: ' + repr(k))
        del bucket[k]

    def __iter__(self):
        for bucket in self._table:
            if bucket is not None:
                for key in bucket:
                    yield key

class ProbeHashMap(HashMapBase):
    """Hash map implemented with linear probing for collision resolution"""
    _AVAIL = object()

    def _is_available(self, j):
        """Return True if index j is available in self._table"""
        return self._table[j] is None or self._table[j] is ProbeHashMap._AVAIL

    def _find_slot(self, j, k):
        """Search for key k in bucket at index j
        
        Return (success, index) tuple described as follows:
        if match was found, success is True and index denotes its location
        if no match was found, success is False and index denotes first available slot
        """
        firstAvail = None
        while True:
            if self._is_available(j):
                if firstAvail is None:
                    firstAvail = j
                if self._table[j] is None: # search failed
                    return (False, firstAvail)
            elif k == self._table[j]._key:
                return (True, j)
            j = (j + 1)%len(self._table)

    def _bucket_getitem(self, j, k):
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError('Key Error: ' + repr(k))
        return self._table[s]._value

    def _bucket_setitem(self, j, k, v):
        found, s = self._find_slot(j, k)
        if not found:
            self._table[s] = self._Item(k, v)
            self._n += 1
        else:
            self._table[s]._value = v

    def _bucket_delitem(self, j, k):
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError('Key Error:' + repr(k))
        self._table[s] = ProbeHashMap._AVAIL # mark spot as vacated

    def __iter__(self):
        for j in range(self._table):
            if not self._is_available():
                yield self._table[j]._key