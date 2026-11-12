# Runtime: 212 ms
# Memory: 14.9 MB

class Solution(object):
    def shipWithinDays(self, weights, days):
        start = max(weights)
        end = sum(weights)
        ans = end

        while start <= end:
            mid = (start + end) // 2

            days_needed = 1
            current_load = 0

            for weight in weights:
                if current_load + weight > mid:
                    days_needed += 1
                    current_load = weight
                else:
                    current_load += weight

            if days_needed <= days:
                ans = mid
                end = mid - 1
            else:
                start = mid + 1

        return ans