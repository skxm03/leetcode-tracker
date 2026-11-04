# 583. Delete Operation for Two Strings

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-String-blue) ![Topic](https://img.shields.io/badge/Topic-Dynamic_Programming-blue) ![Topic](https://img.shields.io/badge/Topic-Longest_Common_Subsequence-blue) ![Language](https://img.shields.io/badge/Language-python-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 181 ms |
| Memory | 15.7 MB |
| Submission Date | 2026-11-04T04:44:30.385Z |
| Platform | leetcode |

## Problem Statement

<p>Given two strings <code>word1</code> and <code>word2</code>, return <em>the minimum number of <strong>steps</strong> required to make</em> <code>word1</code> <em>and</em> <code>word2</code> <em>the same</em>.</p>

<p>In one <strong>step</strong>, you can delete exactly one character in either string.</p>

<p>&nbsp;</p>

## Examples

**Example 1:**

```
Input: word1 = "sea", word2 = "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
```

**Example 2:**

```
Input: word1 = "leetcode", word2 = "etco"
Output: 4
```

## Constraints

- <code>1 &lt;= word1.length, word2.length &lt;= 500</code>
- <code>word1</code> and <code>word2</code> consist of only lowercase English letters.

## Solution

```py
class Solution(object):
    def minDistance(self, word1, word2):
        m, n = len(word1), len(word2)
        dp = [[-1] * n for _ in range(m)]

        def solve(i, j):
            if i == m or j == n:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            if word1[i] == word2[j]:
                dp[i][j] = 1 + solve(i + 1, j + 1)
            else:
                dp[i][j] = max(
                    solve(i + 1, j),
                    solve(i, j + 1)
                )

            return dp[i][j]

        return m+n - 2*solve(0, 0)
        
```

[View on LeetCode](https://leetcode.com/problems/delete-operation-for-two-strings/)
