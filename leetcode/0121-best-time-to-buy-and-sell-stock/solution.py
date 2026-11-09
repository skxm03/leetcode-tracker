# Runtime: 81 ms
# Memory: 18.7 MB

class Solution(object):
    def maxProfit(self, prices):
        buy = prices[0]
        sell = 0
        for i in prices:
            if i < buy:
                buy = i
            else:
                sell = max(i-buy, sell)
        return sell
        
        