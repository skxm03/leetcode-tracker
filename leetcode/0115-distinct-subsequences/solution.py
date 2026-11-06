# Runtime: 668 ms
# Memory: 29.4 MB

class Solution(object):
    def numDistinct(self, s, t):
        m, n = len(s), len(t)
        dp = [[-1] * n for _ in range(m)]

        def solve(i, j):
            if j == n:
                return 1

            if i == m:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            if s[i] == t[j]:
                dp[i][j] = solve(i + 1, j + 1) + solve(i + 1, j)
            else:
                dp[i][j] = solve(i + 1, j)

            return dp[i][j]

        return solve(0, 0)