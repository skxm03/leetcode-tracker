# Runtime: 225 ms
# Memory: 14.3 MB

class Solution(object):
    def maxUncrossedLines(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        dp = [[-1] * n for _ in range(m)]

        def solve(i, j):
            if i == m or j == n:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            if nums1[i] == nums2[j]:
                dp[i][j] = 1 + solve(i + 1, j + 1)
            else:
                dp[i][j] = max(
                    solve(i + 1, j),
                    solve(i, j + 1)
                )

            return dp[i][j]

        return solve(0, 0)
        