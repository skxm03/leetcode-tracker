# 70. Climbing Stairs

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen) ![Topic](https://img.shields.io/badge/Topic-Math-blue) ![Topic](https://img.shields.io/badge/Topic-Dynamic_Programming-blue) ![Topic](https://img.shields.io/badge/Topic-Memoization-blue) ![Language](https://img.shields.io/badge/Language-python-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 0 ms |
| Memory | 12.2 MB |
| Submission Date | 2026-11-02T17:22:17.763Z |
| Platform | leetcode |

## Problem Statement

<p>You are climbing a staircase. It takes <code>n</code> steps to reach the top.</p>

<p>Each time you can either climb <code>1</code> or <code>2</code> steps. In how many distinct ways can you climb to the top?</p>

<p>&nbsp;</p>

## Examples

**Example 1:**

```
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
```

**Example 2:**

```
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
```

## Constraints

- <code>1 &lt;= n &lt;= 45</code>

## Solution

```py
class Solution(object):
    def climbStairs(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        a, b = 1, 2
        for i in range(n-2):
            a, b = b, a+b
        return b
```

[View on LeetCode](https://leetcode.com/problems/climbing-stairs/)
