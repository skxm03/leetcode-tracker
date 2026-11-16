# Runtime: 5758 ms
# Memory: 121.8 MB

class Solution(object):
    def lengthOfLIS(self, nums):
        n = len(nums)
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for prev in range(i - 1, -2, -1):

                take = 0
                if prev == -1 or nums[i] > nums[prev]:
                    take = 1 + dp[i + 1][i + 1]

                not_take = dp[i + 1][prev + 1]

                dp[i][prev + 1] = max(take, not_take)

        return dp[0][0]