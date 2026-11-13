# Runtime: 0 ms
# Memory: 12.4 MB

class Solution(object):
    def findMin(self, nums):
        start, end = 0, len(nums) - 1

        while start < end:
            mid = (start + end) // 2

            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid

        return nums[start]