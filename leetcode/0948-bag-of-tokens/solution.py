# Runtime: 6 ms
# Memory: 12.2 MB

class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        tokens.sort()
        i, j = 0, len(tokens)-1
        score = 0
        maxi = 0

        while i <= j:
            if tokens[i] <= power:
                power -= tokens[i]
                score += 1
                i += 1
            elif score > 0:
                power += tokens[j]
                score -= 1
                j -= 1
            else:
                i += 1
            maxi = max(score, maxi)
        return maxi
        