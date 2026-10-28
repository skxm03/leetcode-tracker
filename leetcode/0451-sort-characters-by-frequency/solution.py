# Runtime: 16 ms
# Memory: 13.2 MB

class Solution(object):
    def frequencySort(self, s):
        d = {}

        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        
        x = sorted(d, key = lambda x: d[x], reverse = True)
        s = ''
        for i in x:
            s += i*d[i]
        return s
        