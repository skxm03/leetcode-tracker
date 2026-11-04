# 1035. Uncrossed Lines

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Dynamic_Programming-blue) ![Topic](https://img.shields.io/badge/Topic-Longest_Common_Subsequence-blue) ![Language](https://img.shields.io/badge/Language-python-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 225 ms |
| Memory | 14.3 MB |
| Submission Date | 2026-11-04T04:36:59.950Z |
| Platform | leetcode |

## Problem Statement

<p>You are given two integer arrays <code>nums1</code> and <code>nums2</code>. We write the integers of <code>nums1</code> and <code>nums2</code> (in the order they are given) on two separate horizontal lines.</p>

<p>We may draw connecting lines: a straight line connecting two numbers <code>nums1[i]</code> and <code>nums2[j]</code> such that:</p>

<ul>
	<li><code>nums1[i] == nums2[j]</code>, and</li>
	<li>the line we draw does not intersect any other connecting (non-horizontal) line.</li>
</ul>

<p>Note that a connecting line cannot intersect even at the endpoints (i.e., each number can only belong to one connecting line).</p>

<p>Return <em>the maximum number of connecting lines we can draw in this way</em>.</p>

<p>&nbsp;</p>

## Examples

**Example 1:**

```
Input: nums1 = [1,4,2], nums2 = [1,2,4]
Output: 2
Explanation: We can draw 2 uncrossed lines as in the diagram.
We cannot draw 3 uncrossed lines, because the line from nums1[1] = 4 to nums2[2] = 4 will intersect the line from nums1[2]=2 to nums2[1]=2.
```

**Example 2:**

```
Input: nums1 = [2,5,1,2,5], nums2 = [10,5,2,1,5,2]
Output: 3
```

**Example 3:**

```
Input: nums1 = [1,3,7,1,7,5], nums2 = [1,9,2,5,1]
Output: 2
```

## Constraints

- <code>1 &lt;= nums1.length, nums2.length &lt;= 500</code>
- <code>1 &lt;= nums1[i], nums2[j] &lt;= 2000</code>

## Solution

```py
class Solution(object):
    def maxUncrossedLines(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        dp = [[-1] * n for _ in range(m)]

        def solve(i, j):
            if i == m or j == n:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            if nums1[i] == nums2[j]:
                dp[i][j] = 1 + solve(i + 1, j + 1)
            else:
                dp[i][j] = max(
                    solve(i + 1, j),
                    solve(i, j + 1)
                )

            return dp[i][j]

        return solve(0, 0)
        
```

[View on LeetCode](https://leetcode.com/problems/uncrossed-lines/)
