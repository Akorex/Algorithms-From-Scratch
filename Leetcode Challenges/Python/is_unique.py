"""
This is a solution of a problem from the book - Cracking the Coding Interview

Implement an algorithm to determine if a string has all unique characters. What if you 
cannot use additional data structures? 

"""
import unittest


def unique(string : str) -> bool:
    # assumning the input string is ASCII 
    if len(string) > 128:
        return False

    char_set = [False] * 128

    for char in string:
        val = ord(char)

        if char_set[val]:
            return False
        char_set[val] = True

    return True

class Test(unittest.TestCase):
    dataT = [('abcd'), ('s4fad'), ('')]
    dataF = [('23ds2'), ('hb 627jh=j ()')]

    def test_unique(self):
        # true check
        for test_string in self.dataT:
            actual = unique(test_string)
            self.assertTrue(actual)

        # false check
        for test_string in self.dataF:
            actual = unique(test_string)
            self.assertFalse(actual)


if __name__ == '__main__':
    unittest.main()