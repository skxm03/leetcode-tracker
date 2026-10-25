# Runtime: 2153 ms
# Memory: 13 MB

class Solution(object):
    def twoSum(self, nums, target):
        k = True
        for i in range(0, len(nums)):
            if k == False:
                break
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return [i, j]
                    k = False
                    break
                else:
                    continue
        
        