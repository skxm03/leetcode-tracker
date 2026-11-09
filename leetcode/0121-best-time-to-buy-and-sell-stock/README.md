# 121. Best Time to Buy and Sell Stock

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Dynamic_Programming-blue) ![Language](https://img.shields.io/badge/Language-python-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 81 ms |
| Memory | 18.7 MB |
| Submission Date | 2026-11-09T17:18:45.153Z |
| Platform | leetcode |

## Problem Statement

<p>You are given an array <code>prices</code> where <code>prices[i]</code> is the price of a given stock on the <code>i<sup>th</sup></code> day.</p>

<p>You want to maximize your profit by choosing a <strong>single day</strong> to buy one stock and choosing a <strong>different day in the future</strong> to sell that stock.</p>

<p>Return <em>the maximum profit you can achieve from this transaction</em>. If you cannot achieve any profit, return <code>0</code>.</p>

<p>&nbsp;</p>

## Examples

**Example 1:**

```
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
```

**Example 2:**

```
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
```

## Constraints

- <code>1 &lt;= prices.length &lt;= 10<sup>5</sup></code>
- <code>0 &lt;= prices[i] &lt;= 10<sup>4</sup></code>

## Solution

```py
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
        
        
```

[View on LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
