# Runtime: 0 ms
# Memory: 12.1 MB

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1[m:m+n] = nums2  # Insert nums2 elements into nums1's extra space
        nums1.sort()          # Sort the final list
