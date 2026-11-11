# Runtime: 2 ms
# Memory: 12.2 MB

class Solution(object):
    def mySqrt(self, x):
        start = 0
        end = x
        ans = 0

        while start <= end:
            mid = (start + end) // 2

            if mid * mid == x:
                return mid

            elif mid * mid < x:
                ans = mid
                start = mid + 1

            else:
                end = mid - 1

        return ans