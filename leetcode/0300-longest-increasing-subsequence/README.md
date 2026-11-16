# 300. Longest Increasing Subsequence

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Binary_Search-blue) ![Topic](https://img.shields.io/badge/Topic-Dynamic_Programming-blue) ![Topic](https://img.shields.io/badge/Topic-Longest_Increasing_Subsequence-blue) ![Language](https://img.shields.io/badge/Language-python-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 5758 ms |
| Memory | 121.8 MB |
| Submission Date | 2026-11-16T04:33:43.925Z |
| Platform | leetcode |

## Problem Statement

<p>Given an integer array <code>nums</code>, return <em>the length of the longest <strong>strictly increasing </strong></em><span data-keyword="subsequence-array"><em><strong>subsequence</strong></em></span>.</p>

<p>&nbsp;</p>

## Examples

**Example 1:**

```
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
```

**Example 2:**

```
Input: nums = [0,1,0,3,2,3]
Output: 4
```

**Example 3:**

```
Input: nums = [7,7,7,7,7,7,7]
Output: 1
```

## Constraints

- <code>1 &lt;= nums.length &lt;= 2500</code>
- <code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code>

## Solution

```py
class Solution(object):
    def lengthOfLIS(self, nums):
        n = len(nums)
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for prev in range(i - 1, -2, -1):

                take = 0
                if prev == -1 or nums[i] > nums[prev]:
                    take = 1 + dp[i + 1][i + 1]

                not_take = dp[i + 1][prev + 1]

                dp[i][prev + 1] = max(take, not_take)

        return dp[0][0]
```

[View on LeetCode](https://leetcode.com/problems/longest-increasing-subsequence/)
