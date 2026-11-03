# 63. Unique Paths II

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Dynamic_Programming-blue) ![Topic](https://img.shields.io/badge/Topic-Matrix-blue) ![Language](https://img.shields.io/badge/Language-python-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 1 ms |
| Memory | 12.1 MB |
| Submission Date | 2026-11-03T03:55:09.807Z |
| Platform | leetcode |

## Problem Statement

<p>You are given an <code>m x n</code> integer array <code>grid</code>. There is a robot initially located at the <b>top-left corner</b> (i.e., <code>grid[0][0]</code>). The robot tries to move to the <strong>bottom-right corner</strong> (i.e., <code>grid[m - 1][n - 1]</code>). The robot can only move either down or right at any point in time.</p>

<p>An obstacle and space are marked as <code>1</code> or <code>0</code> respectively in <code>grid</code>. A path that the robot takes cannot include <strong>any</strong> square that is an obstacle.</p>

<p>Return <em>the number of possible unique paths that the robot can take to reach the bottom-right corner</em>.</p>

<p>The testcases are generated so that the answer will be less than or equal to <code>2 * 10<sup>9</sup></code>.</p>

<p>&nbsp;</p>

## Examples

**Example 1:**

```
Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
```

**Example 2:**

```
Input: obstacleGrid = [[0,1],[0,0]]
Output: 1
```

## Constraints

- <code>m == obstacleGrid.length</code>
- <code>n == obstacleGrid[i].length</code>
- <code>1 &lt;= m, n &lt;= 100</code>
- <code>obstacleGrid[i][j]</code> is <code>0</code> or <code>1</code>.

## Solution

```py
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0]*n for _ in range(m)]

        if obstacleGrid[m-1][n-1] == 1:
            return 0

        dp[m-1][n-1] = 1

        for i in range(m-2, -1, -1):
            if obstacleGrid[i][n-1] == 0:
                dp[i][n-1] = dp[i+1][n-1]
            else:
                dp[i][n-1] = 0
        for j in range(n-2, -1, -1):
            if obstacleGrid[m-1][j] == 0:
                dp[m-1][j] = dp[m-1][j+1]
            else:
                dp[m-1][j] = 0
        
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                if obstacleGrid[i][j] != 1:
                    dp[i][j] = dp[i+1][j] + dp[i][j+1]
        
        return dp[0][0]
        
```

[View on LeetCode](https://leetcode.com/problems/unique-paths-ii/)
