# Runtime: 13 ms
# Memory: 16.7 MB

class Solution(object):
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])

        output = []
        st = intervals[0][0]
        e = intervals[0][1]

        for start, end in intervals[1:]:
            if start <= e:
                st = min(st, start)
                e = max(e, end)
            else:
                output.append([st, e])
                st = start
                e = end

        output.append([st, e])
        return output