"""
Solution to Leetcode problem #387 - First Unique Character in a string

https://leetcode.com/problems/first-unique-character-in-a-string/description/

"""

# initial solution

class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = {}

        # count occurences
        for ch in s:
            seen[ch] = seen.get(ch, 0) + 1

        for i in range(len(s)):
            if seen[s[i]] == 1:
                return i

        return -1
    
## alt solution using LRUCache

class LRUCache:
    def __init__(self):
        self.root = []
        self.root[:] = [self.root, self.root, None, None]
        self.PREV = 0
        self.NEXT = 1
        self.KEY = 2
        self.VALUE = 3
        self.key_to_node = {}
    
    def get(self, key):
        if key not in self.key_to_node:
            return -1
        node = self.key_to_node[key]
        self._pop(node)
        self._append(node)
        return node[self.VALUE]
    
    def put(self, key, value):
        if key in self.key_to_node:
            node = self.key_to_node[key]
            node[self.VALUE] = value
            self._pop(node)
        else:
            node = [None, None, key, value]
            self.key_to_node[key] = node
        self._append(node)

    def evict(self):
        if not self.key_to_node:
            return None
        least_recently_used_node = self.root[self.NEXT]
        self._pop(least_recently_used_node)
        del self.key_to_node[least_recently_used_node[self.KEY]]
        return least_recently_used_node[self.VALUE]
    
    def remove(self, key):
        if key not in self.key_to_node:
            return
        node = self.key_to_node[key]
        self._pop(node)
        del self.key_to_node[key]

    def _pop(self, node):
        prev_node = node[self.PREV]
        next_node = node[self.NEXT]

        prev_node[self.NEXT] = next_node
        next_node[self.PREV] = prev_node
        node[self.NEXT] = None
        node[self.PREV] = None

        return node
    
    def _append(self, node):
        prev_node = self.root[self.PREV]
        next_node = self.root

        prev_node[self.NEXT] = node
        next_node[self.PREV] = node
        node[self.PREV] = prev_node
        node[self.NEXT] = next_node


class Solution:
    def firstUniqChar(self, s: str) -> int:
        non_repeating_char_to_index = LRUCache()
        repeated_chars = set()
        for index, character in enumerate(s):
            if character in repeated_chars:
                continue
            if non_repeating_char_to_index.get(character) != -1:
                non_repeating_char_to_index.remove(character)
                repeated_chars.add(character)
                continue
            non_repeating_char_to_index.put(character, index)
        first_non_repeating_index = non_repeating_char_to_index.evict()
        if first_non_repeating_index is None:
            return -1
        return first_non_repeating_index
        