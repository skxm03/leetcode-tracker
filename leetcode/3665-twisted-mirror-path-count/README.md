# 3665. Twisted Mirror Path Count

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Dynamic_Programming-blue) ![Topic](https://img.shields.io/badge/Topic-Matrix-blue) ![Language](https://img.shields.io/badge/Language-python-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 5876 ms |
| Memory | 67.4 MB |
| Submission Date | 2026-11-05T17:51:12.888Z |
| Platform | leetcode |

## Problem Statement

<p>Given an <code>m x n</code> binary grid <code>grid</code> where:</p>

<ul>
	<li><code>grid[i][j] == 0</code> represents an empty cell, and</li>
	<li><code>grid[i][j] == 1</code> represents a mirror.</li>
</ul>

<p>A robot starts at the top-left corner of the grid <code>(0, 0)</code> and wants to reach the bottom-right corner <code>(m - 1, n - 1)</code>. It can move only <strong>right</strong> or <strong>down</strong>. If the robot attempts to move into a mirror cell, it is <strong>reflected</strong> before entering that cell:</p>

<ul>
	<li>If it tries to move <strong>right</strong> into a mirror, it is turned <strong>down</strong> and moved into the cell directly below the mirror.</li>
	<li>If it tries to move <strong>down</strong> into a mirror, it is turned <strong>right</strong> and moved into the cell directly to the right of the mirror.</li>
</ul>

<p>If this reflection would cause the robot to move outside the <code>grid</code> boundaries, the path is considered invalid and should not be counted.</p>

<p>Return the number of unique valid paths from <code>(0, 0)</code> to <code>(m - 1, n - 1)</code>.</p>

<p>Since the answer may be very large, return it <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.</p>

<p><strong>Note</strong>: If a reflection moves the robot into a mirror cell, the robot is immediately reflected again based on the direction it used to enter that mirror: if it entered while moving right, it will be turned down; if it entered while moving down, it will be turned right. This process will continue until either the last cell is reached, the robot moves out of bounds or the robot moves to a non-mirror cell.</p>

<p>&nbsp;</p>

## Examples

**Example 1:**

```
Input: grid = [[0,1,0],[0,0,1],[1,0,0]]

Output: 5

Explanation:


	
		
			Number
			Full Path
		
	
	
		
			1
			(0, 0) &rarr; (0, 1) [M] &rarr; (1, 1) &rarr; (1, 2) [M] &rarr; (2, 2)
		
		
			2
			(0, 0) &rarr; (0, 1) [M] &rarr; (1, 1) &rarr; (2, 1) &rarr; (2, 2)
		
		
			3
			(0, 0) &rarr; (1, 0) &rarr; (1, 1) &rarr; (1, 2) [M] &rarr; (2, 2)
		
		
			4
			(0, 0) &rarr; (1, 0) &rarr; (1, 1) &rarr; (2, 1) &rarr; (2, 2)
		
		
			5
			(0, 0) &rarr; (1, 0) &rarr; (2, 0) [M] &rarr; (2, 1) &rarr; (2, 2)
		
	



	
	[M] indicates the robot attempted to enter a mirror cell and instead reflected.
```

**Example 2:**

```
Input: grid = [[0,0],[0,0]]

Output: 2

Explanation:


	
		
			Number
			Full Path
		
	
	
		
			1
			(0, 0) &rarr; (0, 1) &rarr; (1, 1)
		
		
			2
			(0, 0) &rarr; (1, 0) &rarr; (1, 1)
```

**Example 3:**

```
Input: grid = [[0,1,1],[1,1,0]]

Output: 1

Explanation:


	
		
			Number
			Full Path
		
	
	
		
			1
			(0, 0) &rarr; (0, 1) [M] &rarr; (1, 1) [M] &rarr; (1, 2)
		
	

(0, 0) &rarr; (1, 0) [M] &rarr; (1, 1) [M] &rarr; (2, 1) goes out of bounds, so it is invalid.
```

## Constraints

_No constraints provided._

## Solution

```py
class Solution:
    def uniquePaths(self, grid):
        m, n = len(grid), len(grid[0])
        MOD = 10**9 + 7

        dp = [[[-1] * 3 for _ in range(n)] for _ in range(m)]

        def solve(i, j, d):
            if i >= m or j >= n:
                return 0

            if i == m - 1 and j == n - 1:
                return 1

            if dp[i][j][d] != -1:
                return dp[i][j][d]

            ans = 0

            if grid[i][j] == 0:
                ans += solve(i, j + 1, 0)
                ans += solve(i + 1, j, 1)

            else:
                if d == 0:
                    ans += solve(i + 1, j, 1)
                elif d == 1:
                    ans += solve(i, j + 1, 0)

            dp[i][j][d] = ans % MOD
            return dp[i][j][d]

        return solve(0, 0, 2)
```

[View on LeetCode](https://leetcode.com/problems/twisted-mirror-path-count/)
