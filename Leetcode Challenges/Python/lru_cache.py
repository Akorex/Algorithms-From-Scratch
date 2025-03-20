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
        


### alt approach

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._move_to_front(node)
        return node.value
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_front(node)
        else:
            if len(self.cache) == self.capacity:
                self._remove_lru()
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_front(new_node)
        

    def _add_to_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def _move_to_front(self, node):
        self._remove_node(node)
        self._add_to_front(node)

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _remove_lru(self):
        if self.head.next != self.tail:
            lru = self.tail.prev
            self._remove_node(lru)
            del self.cache[lru.key]
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)



