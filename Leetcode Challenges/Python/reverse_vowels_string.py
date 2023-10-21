class Solution:
    def reverseVowels(self, s: str) -> str:
        l = list(s)
        left = 0
        right = len(l) - 1

        vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
        while left < right:
            while left < right and l[left] not in vowels:
                left += 1
            while left < right and l[right] not in vowels:
                right -=1
            l[left], l[right] = l[right], l[left]
            left += 1
            right -= 1
        s = ''.join(l)
        return s