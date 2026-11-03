# 64. Minimum Path Sum

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Dynamic_Programming-blue) ![Topic](https://img.shields.io/badge/Topic-Matrix-blue) ![Language](https://img.shields.io/badge/Language-python-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 14 ms |
| Memory | 14 MB |
| Submission Date | 2026-11-03T04:03:55.662Z |
| Platform | leetcode |

## Problem Statement

<p>Given a <code>m x n</code> <code>grid</code> filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.</p>

<p><strong>Note:</strong> You can only move either down or right at any point in time.</p>

<p>&nbsp;</p>

## Examples

**Example 1:**

```
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 &rarr; 3 &rarr; 1 &rarr; 1 &rarr; 1 minimizes the sum.
```

**Example 2:**

```
Input: grid = [[1,2,3],[4,5,6]]
Output: 12
```

## Constraints

- <code>m == grid.length</code>
- <code>n == grid[i].length</code>
- <code>1 &lt;= m, n &lt;= 200</code>
- <code>0 &lt;= grid[i][j] &lt;= 200</code>

## Solution

```py
class Solution(object):
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        dp = [[0]*n for _ in range(m)]

        dp[m-1][n-1] = grid[m-1][n-1]

        for i in range(m-2, -1, -1):
            dp[i][n-1] = grid[i][n-1] + dp[i+1][n-1]
        for j in range(n-2, -1, -1):
            dp[m-1][j] = grid[m-1][j] + dp[m-1][j+1]
        
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                dp[i][j] = grid[i][j] + min(dp[i+1][j], dp[i][j+1])
        
        return dp[0][0]
        
```

[View on LeetCode](https://leetcode.com/problems/minimum-path-sum/)
