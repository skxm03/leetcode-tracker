# Runtime: 16 ms
# Memory: 12.1 MB

class Solution(object):
    def guessNumber(self, n):
        start = 1
        end = n

        while start <= end:
            mid = (start + end) // 2

            res = guess(mid)

            if res == 0:
                return mid

            elif res == -1:
                end = mid - 1

            else:
                start = mid + 1

        return -1