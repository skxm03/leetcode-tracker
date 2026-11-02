# Runtime: 4 ms
# Memory: 12.3 MB

class Solution(object):
    def uniquePaths(self, m, n):
        dp = [[-1]*n for _ in range(m)]

        def solve(i, j):
            if i >= m or j >= n:
                return 0
            if i == m-1 and j == n-1:
                return 1
            if dp[i][j] != -1:
                return dp[i][j]
            
            dp[i][j] = solve(i+1, j) + solve(i, j+1)

            return dp[i][j]
        return solve(0, 0)
        