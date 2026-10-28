# Runtime: 1123 ms
# Memory: 24.6 MB

class Solution(object):
    def minPairSum(self, nums):
        nums.sort()
        max = float("-inf")
        i, j = 0, len(nums)-1
        while i < j:
            if nums[i] + nums[j] > max:
                max = nums[i] + nums[j]
            i += 1
            j -= 1
        return max



        