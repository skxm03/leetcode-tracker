# Runtime: 41 ms
# Memory: 17.8 MB

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        n = len(gas)
        totalgas = 0
        for val in gas:
            totalgas += val
        totalcost = 0
        for val in cost:
            totalcost += val
        if totalcost > totalgas:
            return -1

        station = 0
        capacity = 0

        for i in range(n):
            capacity += gas[i]
            capacity -= cost[i]
            if capacity < 0:
                station = i + 1
                capacity = 0
        return station
        