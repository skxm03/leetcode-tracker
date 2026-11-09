# Runtime: 94 ms
# Memory: 26.5 MB

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        window = set()

        for i in range(len(nums)):
            if nums[i] in window:
                return True

            window.add(nums[i])

            if len(window) > k:
                window.remove(nums[i - k])

        return False