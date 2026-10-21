# Runtime: 2319 ms
# Memory: 52.8 MB

class Solution(object):
    def coinChange(self, coins, amount):
        n = len(coins)
        dp = [[0]*(amount+1) for _ in range(n+1)]

        def solve(i, sum):
            if sum == amount:
                return 0
            if i >= n:
                return float('inf')

            if dp[i][sum] != 0:
                return dp[i][sum]

            take = float('inf')
            if sum + coins[i] <= amount:
                take = 1 + solve(i, sum + coins[i])

            not_take = solve(i + 1, sum)

            dp[i][sum] += min(take, not_take)
            return dp[i][sum]

        ans = solve(0, 0)
        return ans if ans != float('inf') else -1