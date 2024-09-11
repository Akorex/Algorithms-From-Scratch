"""
One Away: There are three types of edits that can be performed on strings: insert a character, 
remove a character, or replace a character. Given two strings, write a function to check if they are 
one edit (or zero edits) away.

EXAMPLE 
pale, ple -> true 
pales, pale -> true 
pale, bale -> true 
pale, bae -> false 

"""

import time
import unittest

def one_edit_replace(s1, s2):
    edited = False

    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            if edited:
                return False
            edited = True
    return True


def one_edit_insert(s1, s2):
    edited = False

    i, j = 0, 0

    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            if edited:
                return False
            edited = True
            j += 1

        else:
            i += 1
            j += 1
    return True

def one_edit_away(s1, s2):
    """Checks if one string can be converted to another string by one edit"""
    if len(s1) == len(s2):
        return one_edit_replace(s1, s2)
    
    if len(s1) + 1 == len(s2):
        return one_edit_insert(s1, s2)

    if len(s1) - 1 == len(s2):
        return one_edit_insert(s2, s1)

    return False

class Test(unittest.TestCase):
    test_cases = [
        ("pale", "pale", True),
        ("", "", True), 

        ("pale", "ple", True),
        ("ple", "pale", True),
        ("pales", "pale", True), 
        ("ples", "pales", True), 
        
        ("bale", "pales", False), 
    ]

    testable_functions = [one_edit_away]

    def test_one_away(self):
        for f in self.testable_functions:
            start = time.perf_counter()

            for _ in range(100):
                for [text_a, text_b, expected] in self.test_cases:
                    assert f(text_a, text_b) == expected
            duration = time.perf_counter() - start
            print(f"{f.__name__} {duration * 1000:.1f} ms")

if __name__ == '__main__':
    unittest.main()