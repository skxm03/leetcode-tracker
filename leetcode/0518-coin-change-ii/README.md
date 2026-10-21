# 518. Coin Change II

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Dynamic_Programming-blue) ![Topic](https://img.shields.io/badge/Topic-Knapsack_Problem-blue) ![Topic](https://img.shields.io/badge/Topic-Complete_Knapsack-blue) ![Language](https://img.shields.io/badge/Language-python-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 1219 ms |
| Memory | 47.4 MB |
| Submission Date | 2026-10-21T04:44:16.045Z |
| Platform | leetcode |

## Problem Statement

<p>You are given an integer array <code>coins</code> representing coins of different denominations and an integer <code>amount</code> representing a total amount of money.</p>

<p>Return <em>the number of combinations that make up that amount</em>. If that amount of money cannot be made up by any combination of the coins, return <code>0</code>.</p>

<p>You may assume that you have an infinite number of each kind of coin.</p>

<p>The <strong>final</strong> answer is <strong>guaranteed</strong> to fit into a signed <strong>32-bit</strong> integer.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<pre>
<strong>Input:</strong> amount = 5, coins = [1,2,5]
<strong>Output:</strong> 4
<strong>Explanation:</strong> there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
</pre>

<p>
```

**Example 2:**

```
</p>

<pre>
<strong>Input:</strong> amount = 3, coins = [2]
<strong>Output:</strong> 0
<strong>Explanation:</strong> the amount of 3 cannot be made up just with coins of 2.
</pre>

<p>
```

**Example 3:**

```
</p>

<pre>
<strong>Input:</strong> amount = 10, coins = [10]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>1 &lt;= coins.length &lt;= 300</code>
- <code>1 &lt;= coins[i] &lt;= 5000</code>
- All the values of <code>coins</code> are <strong>unique</strong>.
- <code>0 &lt;= amount &lt;= 5000</code>

## Solution

```py
class Solution(object):
    def change(self, amount, coins):
        N = len(coins)

        dp = [[-1]*(amount+1) for _ in range(N+1)]

        def solve(i, sum):
            if sum > amount:
                return 0
            if sum == amount:
                return 1
            if i >= N:
                return 0
            if dp[i][sum] != -1:
                return dp[i][sum]
            
            take = solve(i, sum + coins[i])
            notTake = solve(i+1, sum)
            dp[i][sum] = take + notTake

            return dp[i][sum]

        return solve(0, 0)
```

[View on LeetCode](https://leetcode.com/problems/coin-change-ii/)
