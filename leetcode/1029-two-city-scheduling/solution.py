# Runtime: 1 ms
# Memory: 12.3 MB

class Solution(object):
    def twoCitySchedCost(self, costs):
        costs.sort(key=lambda x: x[0] - x[1])

        n = len(costs)
        ans = 0

        for i in range(n // 2):
            ans += costs[i][0]

        for i in range(n // 2, n):
            ans += costs[i][1]

        return ans
