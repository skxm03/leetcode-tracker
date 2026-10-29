# Runtime: 1186 ms
# Memory: 23.4 MB

import heapq

class Solution(object):
    def halveArray(self, nums):
        total = sum(nums)
        target = total / 2.0

        heap = [-x for x in nums]
        heapq.heapify(heap)

        reduced = 0.0
        ops = 0

        while reduced < target:
            largest = -heapq.heappop(heap)
            half = largest / 2.0

            reduced += half
            heapq.heappush(heap, -half)
            ops += 1

        return ops