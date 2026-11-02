# 746. Min Cost Climbing Stairs

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Dynamic_Programming-blue) ![Language](https://img.shields.io/badge/Language-python-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 13 ms |
| Memory | 14.1 MB |
| Submission Date | 2026-11-02T17:30:30.881Z |
| Platform | leetcode |

## Problem Statement

<p>You are given an integer array <code>cost</code> where <code>cost[i]</code> is the cost of <code>i<sup>th</sup></code> step on a staircase.</p>

<p>Once you pay the cost, you can either climb <strong>one</strong> or <strong>two</strong> steps.</p>

<p>You can either start from the step with index 0, or the step with index 1.</p>

<p>Return the <strong>minimum</strong> cost to reach the top of the staircase, which is the position just past the last step (index <code>cost.length</code>).</p>

<p>&nbsp;</p>

## Examples

**Example 1:**

```
Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
```

**Example 2:**

```
Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.
```

## Constraints

- <code>2 &lt;= cost.length &lt;= 1000</code>
- <code>0 &lt;= cost[i] &lt;= 999</code>

## Solution

```py
class Solution(object):
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        dp = [-1 for _ in range(n)]
        def solve(i):
            if i >= n:
                return 0
            if dp[i] != -1:
                return dp[i]
            
            dp[i] = cost[i] + min(solve(i+1), solve(i+2))
            return dp[i]
        return min(solve(0), solve(1))
        
```

[View on LeetCode](https://leetcode.com/problems/min-cost-climbing-stairs/)
