# 516. Longest Palindromic Subsequence

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-String-blue) ![Topic](https://img.shields.io/badge/Topic-Dynamic_Programming-blue) ![Language](https://img.shields.io/badge/Language-python-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 673 ms |
| Memory | 74.7 MB |
| Submission Date | 2026-11-06T18:02:59.420Z |
| Platform | leetcode |

## Problem Statement

<p>Given a string <code>s</code>, find <em>the longest palindromic <strong>subsequence</strong>&#39;s length in</em> <code>s</code>.</p>

<p>A <strong>subsequence</strong> is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.</p>

<p>&nbsp;</p>

## Examples

**Example 1:**

```
Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".
```

**Example 2:**

```
Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".
```

## Constraints

- <code>1 &lt;= s.length &lt;= 1000</code>
- <code>s</code> consists only of lowercase English letters.

## Solution

```py
class Solution(object):
    def longestPalindromeSubseq(self, s):
        n = len(s)
        dp = [[-1] * n for _ in range(n)]

        def solve(i, j):
            if i > j:
                return 0

            if i == j:
                return 1

            if dp[i][j] != -1:
                return dp[i][j]

            if s[i] == s[j]:
                dp[i][j] = 2 + solve(i + 1, j - 1)
            else:
                dp[i][j] = max(
                    solve(i + 1, j),
                    solve(i, j - 1)
                )

            return dp[i][j]

        return solve(0, n - 1)
```

[View on LeetCode](https://leetcode.com/problems/longest-palindromic-subsequence/)
