"""
Solution to problem 1.2 from Cracking the Coding Interview

Given two strings, write a method to decide if one is a permutation of the 
other.

"""

import unittest
from collections import Counter

def check_permutations(str1 : str, str2 : str) -> bool:
    if len(str1) != len(str2):
        return False

    counter = Counter()
    for c in str1:
        counter[c] += 1

    for c in str2:
        if counter[c] == 0:
            return False
        counter[c] -= 1

    return True

class Test(unittest.TestCase):
    dataT = (
        ('abcd', 'bacd'),
        ('3563476', '7334566'),
        ('wef34f', 'wffe34'),
    )
    dataF = (
        ('abcd', 'd2cba'),
        ('2354', '1234'),
        ('dcw4f', 'dcw5f'),
    )

    def test_permutation(self):

        # true check
        for test_strings in self.dataT:
            result = check_permutations(*test_strings)
            self.assertTrue(result)

        # false check
        for test_strings in self.dataF:
            result = check_permutations(*test_strings)
            self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()

    ...