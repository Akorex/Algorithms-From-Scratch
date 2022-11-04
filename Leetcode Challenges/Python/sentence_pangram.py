"""
Solution to Leetcode problem #1832 - Check if Sentence is Pangram

https://leetcode.com/problems/check-if-the-sentence-is-pangram/description/

"""

# initial approach
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
        'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        for ch in letters:
            if ch not in sentence:
                return False
        return True


# another approach
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        for i in range(26):
            curr_char = chr(ord('a') + i)

            if sentence.find(curr_char) == -1:
                return False
        return True

# another approach
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        seen = set(sentence)

        return len(seen) == 26

# even another
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # Array 'seen' of size 26.
        seen = [False] * 26

        # For every letter 'currChar', we find its ASCII code, 
        # and update value at the mapped index as true.
        for curr_char in sentence:
            seen[ord(curr_char) - ord('a')] = True
        
        # Once we finish iterating, check if 'seen' contains false.
        for status in seen:
            if not status:
                return False
        return True