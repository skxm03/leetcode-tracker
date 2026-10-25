# Runtime: 14 ms
# Memory: 14.5 MB

class Solution(object):
    def isPalindrome(self, s):
        chars = []

        for c in s:
            if c.isalnum():
                chars.append(c.lower())

        return chars == chars[::-1]
        