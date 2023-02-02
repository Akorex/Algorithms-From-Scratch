"""
Solution to Leetcode problem # 953 - Verifying an alien dictionary

https://leetcode.com/problems/verifying-an-alien-dictionary/
"""

# initial approach - does not work with repeated characters in the word
# & doesn't increase the index of characters seen
from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        index = 0
        for word in words:
            for c in word:
                if word.index(c) != order[index]:
                    return False
        return True

# let's improve on it by using a hash map to store the counts of characters in a dictionary
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mapped = {ch: i for i, ch in enumerate(order)}
        prev = list(mapped[ch] for ch in words[0])

        for i in range(1, len(words)):
            curr = list(mapped[ch] for ch in words[i])
            if curr < prev:
                return False
            prev = curr
        return True