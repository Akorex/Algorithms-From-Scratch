"""
Solution to Leetcode problem # 460 - LFU Cache

https://leetcode.com/problems/lfu-cache/description/

"""

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def append(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def pop_tail(self):
        if self.size > 0:
            lru = self.tail.prev
            self.remove(lru)
            return lru
        return None

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.freq_map = {}
        self.min_freq = 0
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._update_freq(node)
        return node.value
                  
    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._update_freq(node)
        else:
            if len(self.cache) == self.capacity:
                self._evict()
            new_node = Node(key, value)
            self.cache[key] = new_node
            self.min_freq = 1

            if 1 not in self.freq_map:
                self.freq_map[1] = DoublyLinkedList()
            self.freq_map[1].append(new_node)

    def _update_freq(self, node):
        freq = node.freq
        self.freq_map[freq].remove(node)
        if self.freq_map[freq].size == 0:
            del self.freq_map[freq]
            if self.min_freq == freq:
                self.min_freq += 1

        node.freq += 1
        if node.freq not in self.freq_map:
            self.freq_map[node.freq] = DoublyLinkedList()
        self.freq_map[node.freq].append(node)

    def _evict(self):
        if self.min_freq in self.freq_map:
            lfu_node = self.freq_map[self.min_freq].pop_tail()
            
            if lfu_node:
                del self.cache[lfu_node.key]
                if self.freq_map[self.min_freq].size == 0:
                    del self.freq_map[self.min_freq]



# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)