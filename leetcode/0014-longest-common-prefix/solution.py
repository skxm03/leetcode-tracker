# Runtime: 0 ms
# Memory: 12.3 MB

class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) < 0:
            return ""

        prefix = strs[0]

        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]

                if not prefix:
                    return ""

        return prefix
