# Runtime: 0 ms
# Memory: 12.2 MB

class Solution(object):
    def removeElement(self, nums, val):

        i = 0

        while i != len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1

        return len(nums)
        