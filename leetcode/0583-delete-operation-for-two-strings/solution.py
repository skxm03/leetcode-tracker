# Runtime: 181 ms
# Memory: 15.7 MB

class Solution(object):
    def minDistance(self, word1, word2):
        m, n = len(word1), len(word2)
        dp = [[-1] * n for _ in range(m)]

        def solve(i, j):
            if i == m or j == n:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            if word1[i] == word2[j]:
                dp[i][j] = 1 + solve(i + 1, j + 1)
            else:
                dp[i][j] = max(
                    solve(i + 1, j),
                    solve(i, j + 1)
                )

            return dp[i][j]

        return m+n - 2*solve(0, 0)
        