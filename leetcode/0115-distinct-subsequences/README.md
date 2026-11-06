# 115. Distinct Subsequences

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red) ![Topic](https://img.shields.io/badge/Topic-String-blue) ![Topic](https://img.shields.io/badge/Topic-Dynamic_Programming-blue) ![Language](https://img.shields.io/badge/Language-python-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 668 ms |
| Memory | 29.4 MB |
| Submission Date | 2026-11-06T17:54:33.533Z |
| Platform | leetcode |

## Problem Statement

<p>Given two strings s and t, return <i>the number of distinct</i> <b><i>subsequences</i></b><i> of </i>s<i> which equals </i>t.</p>

<p>The test cases are generated so that the answer fits on a 32-bit signed integer.</p>

<p>&nbsp;</p>

## Examples

**Example 1:**

```
Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from s.
rabbbit
rabbbit
rabbbit
```

**Example 2:**

```
Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from s.
babgbag
babgbag
babgbag
babgbag
babgbag
```

## Constraints

- <code>1 &lt;= s.length, t.length &lt;= 1000</code>
- <code>s</code> and <code>t</code> consist of English letters.

## Solution

```py
class Solution(object):
    def numDistinct(self, s, t):
        m, n = len(s), len(t)
        dp = [[-1] * n for _ in range(m)]

        def solve(i, j):
            if j == n:
                return 1

            if i == m:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            if s[i] == t[j]:
                dp[i][j] = solve(i + 1, j + 1) + solve(i + 1, j)
            else:
                dp[i][j] = solve(i + 1, j)

            return dp[i][j]

        return solve(0, 0)
```

[View on LeetCode](https://leetcode.com/problems/distinct-subsequences/)
