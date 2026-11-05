# Runtime: 5876 ms
# Memory: 67.4 MB

class Solution:
    def uniquePaths(self, grid):
        m, n = len(grid), len(grid[0])
        MOD = 10**9 + 7

        dp = [[[-1] * 3 for _ in range(n)] for _ in range(m)]

        def solve(i, j, d):
            if i >= m or j >= n:
                return 0

            if i == m - 1 and j == n - 1:
                return 1

            if dp[i][j][d] != -1:
                return dp[i][j][d]

            ans = 0

            if grid[i][j] == 0:
                ans += solve(i, j + 1, 0)
                ans += solve(i + 1, j, 1)

            else:
                if d == 0:
                    ans += solve(i + 1, j, 1)
                elif d == 1:
                    ans += solve(i, j + 1, 0)

            dp[i][j][d] = ans % MOD
            return dp[i][j][d]

        return solve(0, 0, 2)