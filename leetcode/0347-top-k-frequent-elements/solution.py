# Runtime: 5 ms
# Memory: 13.9 MB

class Solution(object):
    def topKFrequent(self, nums, k):
        d = {}

        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1

        s = sorted(d, key=lambda x:d[x], reverse=True)
        return s[:k]

