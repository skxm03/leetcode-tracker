# Runtime: 56 ms
# Memory: 23 MB


class Solution(object):
    def minSetSize(self, arr):
        d = {}

        for num in arr:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1

        freq = sorted(d.values(), reverse=True)

        removed = 0
        for i, count in enumerate(freq):
            removed += count

            if removed >= len(arr) // 2:
                return i + 1
