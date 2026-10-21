# Runtime: 1219 ms
# Memory: 47.4 MB

class Solution(object):
    def change(self, amount, coins):
        N = len(coins)

        dp = [[-1]*(amount+1) for _ in range(N+1)]

        def solve(i, sum):
            if sum > amount:
                return 0
            if sum == amount:
                return 1
            if i >= N:
                return 0
            if dp[i][sum] != -1:
                return dp[i][sum]
            
            take = solve(i, sum + coins[i])
            notTake = solve(i+1, sum)
            dp[i][sum] = take + notTake

            return dp[i][sum]

        return solve(0, 0)