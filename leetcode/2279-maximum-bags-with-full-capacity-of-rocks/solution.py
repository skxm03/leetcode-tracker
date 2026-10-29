# Runtime: 89 ms
# Memory: 20 MB

class Solution(object):
    def maximumBags(self, capacity, rocks, additionalRocks):
        remaining = sorted(capacity[i] - rocks[i] for i in range(len(capacity)))

        count = 0

        for space in remaining:
            if additionalRocks >= space:
                additionalRocks -= space
                count += 1
            else:
                break

        return count