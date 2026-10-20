# Runtime: 1238 ms
# Memory: 21.2 MB

class Solution(object):
    def sortArray(self, nums):
        def MergeSort(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2
            left = MergeSort(arr[:mid])
            right = MergeSort(arr[mid:])

            return Merge(left, right)

        def Merge(left, right):
            i = j = 0
            res = []

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1

            while i < len(left):
                res.append(left[i])
                i += 1

            while j < len(right):
                res.append(right[j])
                j += 1

            return res

        return MergeSort(nums)