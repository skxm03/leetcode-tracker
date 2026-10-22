# Runtime: 0 ms
# Memory: 12.1 MB

class Solution(object):
    def sortColors(self, nums):
        # def partition(low, high):
        #     pivot = nums[high]
        #     i = low - 1

        #     for j in range(low, high):
        #         if nums[j] <= pivot:
        #             i += 1
        #             nums[i], nums[j] = nums[j], nums[i]

        #     nums[i + 1], nums[high] = nums[high], nums[i + 1]
        #     return i + 1

        # def quickSort(low, high):
        #     if low < high:
        #         p = partition(low, high)
        #         quickSort(low, p - 1)
        #         quickSort(p + 1, high)

        # quickSort(0, len(nums) - 1)

        # DUTCH NATIONAL FLAG APPROACH:

        low = mid = 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1