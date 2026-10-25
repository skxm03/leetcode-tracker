# Runtime: 36 ms
# Memory: 12.5 MB

class Solution(object):
    def validPalindrome(self, s):
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                a = s[l+1:r+1]
                b = s[l:r]
                return a == a[::-1] or b == b[::-1]

            l += 1
            r -= 1

        return True