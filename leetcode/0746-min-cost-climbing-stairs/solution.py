# Runtime: 13 ms
# Memory: 14.1 MB

class Solution(object):
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        dp = [-1 for _ in range(n)]
        def solve(i):
            if i >= n:
                return 0
            if dp[i] != -1:
                return dp[i]
            
            dp[i] = cost[i] + min(solve(i+1), solve(i+2))
            return dp[i]
        return min(solve(0), solve(1))
        