# Runtime: 153 ms
# Memory: 45.2 MB

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key = lambda x:x[1])
        count = 0
        time = intervals[0][1]
        for start, end in intervals[1:]:
            if start < time:
                count += 1
            else:
                time = end
        return count
        