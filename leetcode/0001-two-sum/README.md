# 1. Two Sum

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Hash_Table-blue) ![Language](https://img.shields.io/badge/Language-python-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 2153 ms |
| Memory | 13 MB |
| Submission Date | 2026-10-25T16:10:18.819Z |
| Platform | leetcode |

## Problem Statement

<p>You are given an array of integers <code>nums</code>&nbsp;and an integer <code>target</code>, return <em>indices of the two numbers such that they add up to <code>target</code></em>.</p>

<p>You may assume that each input would have <strong><em>exactly</em> one solution</strong>, and you may not use the <em>same</em> element twice.</p>

<p>You can return the answer in any order.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<p><strong>Input:</strong> <code>nums = [2,7,11,15], target = 9</code></p>

<p><strong>Output:</strong> <code>[0,1]</code></p>

<p><strong>Explanation:</strong></p>

<p>The sum of <code>nums[0]</code> and <code>nums[1]</code> is <code>2 + 7 = 9</code>, which equals the target. Therefore, the indices <code>[0, 1]</code> are returned.</p>

<p><strong>Example 2:</strong></p>

<p><strong>Input:</strong> <code>nums = [3,2,4], target = 6</code></p>

<p><strong>Output:</strong> <code>[1,2]</code></p>

<p><strong>Explanation:</strong></p>

<p>The sum of <code>nums[1]</code> and <code>nums[2]</code> is <code>2 + 4 = 6</code>, which equals the target. Therefore, the indices <code>[1, 2]</code> are returned.</p>

<p><strong>Example 3:</strong></p>

<p><strong>Input:</strong> <code>nums = [3,3], target = 6</code></p>

<p><strong>Output:</strong> <code>[0,1]</code></p>

<p><strong>Explanation:</strong></p>

<p>The sum of <code>nums[0]</code> and <code>nums[1]</code> is <code>3 + 3 = 6</code>, which equals the target. Therefore, the indices <code>[0, 1]</code> are returned.</p>

<p>&nbsp;</p>

## Examples

_No examples provided._

## Constraints

- <code>2 &lt;= nums.length &lt;= 10<sup>4</sup></code>
- <code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code>
- <code>-10<sup>9</sup> &lt;= target &lt;= 10<sup>9</sup></code>
- <strong>Only one valid answer exists.</strong>

## Solution

```py
class Solution(object):
    def twoSum(self, nums, target):
        k = True
        for i in range(0, len(nums)):
            if k == False:
                break
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return [i, j]
                    k = False
                    break
                else:
                    continue
        
        
```

[View on LeetCode](https://leetcode.com/problems/two-sum/)
