# Runtime: 21 ms
# Memory: 12.4 MB

class Solution(object):
    def minFlips(self, target):
        ans = 0
        prev = '0'

        for ch in target:
            if ch != prev:
                ans += 1
                prev = ch

        return ans
        