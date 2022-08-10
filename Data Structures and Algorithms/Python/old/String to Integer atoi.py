"""
The question and testing for this code is available at:
 https://leetcode.com/problems/string-to-integer-atoi/
"""

class Solution:
    def myAtoi(self, s: str) -> int:
        if (s == ""):
            return 0
        else:
            while (s[0] == " "):
                s = s[1:len(s)]
                if (s == ""):
                    return 0

        sign = 1
        if s[0] == "-":
            sign = -1
            s = s[1:len(s)]
        else:
            if s[0] == "+":
                s = s[1:len(s)]

        Number = ""
        i = 0
        while (i < len(s)):
            if s[i].isdigit() == False:
                break
            Number += s[i]
            i += 1

        if Number == "":
            return 0
        else:
            Number = sign * int(Number)

            if (Number > 2 ** 31 - 1):
                return 2 ** 31 - 1
            if (Number < -2 ** 31):
                return -2 ** 31
            else:
                return Number
