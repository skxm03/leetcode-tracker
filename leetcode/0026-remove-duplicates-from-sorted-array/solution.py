# Runtime: 2 ms
# Memory: 13.8 MB

# class Solution(object):
#     def removeDuplicates(self, nums):
#         i = 1
#         while i != len(nums):
#             if nums[i-1] == nums[i]:
#                 nums.pop(i)
#             else:
#                 i += 1
#         return len(nums)


class Solution(object):
    def removeDuplicates(self, nums):
        i = 1

        for j in range(1, len(nums)):
            if nums[j] != nums[i - 1]:
                nums[i] = nums[j]
                i += 1

        return i
