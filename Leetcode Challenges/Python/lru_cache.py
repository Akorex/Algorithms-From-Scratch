"""
Solution to Leetcode problem #146 - LRU Cache

https://leetcode.com/problems/lru-cache/description/
"""



class LRUCache:

    def __init__(self, capacity: int):
        self.root = [None, None, None, None]
        self.prev = 0
        self.next = 1
        self.key = 2
        self.value = 3
        self.root[self.prev] = self.root
        self.root[self.next] = self.root
        self.capacity = capacity
        self.key_to_node = {}
        

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1
        node = self.key_to_node[key]
        self._pop(node)
        self._append(node)
        return node[self.value]

        

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            node = self.key_to_node[key]
            node[self.value] = value
            self._pop(node)

        else:
            node = [None, None, key, value]
            self.key_to_node[key] = node
            if len(self.key_to_node) > self.capacity:
                lru = self.root[self.next]
                self._pop(lru)
                del self.key_to_node[lru[self.key]]
        self._append(node)


    def _pop(self, node):
        prev_node = node[self.prev]
        next_node = node[self.next]

        prev_node[self.next] = next_node
        next_node[self.prev] = prev_node

        node[self.prev] = None
        node[self.next] = None

        return node

    def _append(self, node):
        prev_node = self.root[self.prev]
        next_node = self.root

        prev_node[self.next] = node
        next_node[self.prev] = node

        node[self.prev] = prev_node
        node[self.next] = next_node

        return node
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


#alt

class LRUCache:

    def __init__(self, capacity: int):
        self.root = []
        self.root[:] = [self.root, self.root, None, None]
        #self.root = [None, None, None, None]
        self.prev = 0
        self.next = 1
        self.key = 2
        self.value = 3
        #self.root[self.prev] = self.root
        #self.root[self.next] = self.root
        self.capacity = capacity
        self.key_to_node = {}
        

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1
        node = self.key_to_node[key]
        self._pop(node)
        self._append(node)
        return node[self.value]

        

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            node = self.key_to_node[key]
            node[self.value] = value
            self._pop(node)

        else:
            node = [None, None, key, value]
            self.key_to_node[key] = node
            if len(self.key_to_node) > self.capacity:
                lru = self.root[self.next]
                self._pop(lru)
                del self.key_to_node[lru[self.key]]
        self._append(node)


    def _pop(self, node):
        prev_node = node[self.prev]
        next_node = node[self.next]

        prev_node[self.next] = next_node
        next_node[self.prev] = prev_node

        node[self.prev] = None
        node[self.next] = None

        return node

    def _append(self, node):
        prev_node = self.root[self.prev]
        next_node = self.root

        prev_node[self.next] = node
        next_node[self.prev] = node

        node[self.prev] = prev_node
        node[self.next] = next_node

        return node
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)