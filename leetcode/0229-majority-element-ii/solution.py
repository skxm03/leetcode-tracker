# Runtime: 10 ms
# Memory: 14.9 MB

class Solution(object):
    def majorityElement(self, nums):
        n = len(nums)
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        
        return [
            i for i in d
            if d[i] > n // 3
        ]
        