# Runtime: 0 ms
# Memory: 12.6 MB

class Solution(object):
    def search(self, nums, target):
        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == target:
                return True

            # Ambiguous because of duplicates
            if nums[start] == nums[mid] == nums[end]:
                start += 1
                end -= 1

            # Left half is sorted
            elif nums[start] <= nums[mid]:
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1

            # Right half is sorted
            else:
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1

        return False