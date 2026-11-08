# 189. Rotate Array

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Math-blue) ![Topic](https://img.shields.io/badge/Topic-Two_Pointers-blue) ![Language](https://img.shields.io/badge/Language-python-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 19 ms |
| Memory | 28.1 MB |
| Submission Date | 2026-11-08T17:46:25.155Z |
| Platform | leetcode |

## Problem Statement

<p>Given an integer array <code>nums</code>, rotate the array to the right by <code>k</code> steps, where <code>k</code> is non-negative.</p>

<p>&nbsp;</p>

## Examples

**Example 1:**

```
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
```

**Example 2:**

```
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
```

## Constraints

- <code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code>
- <code>-2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code>
- <code>0 &lt;= k &lt;= 10<sup>5</sup></code>

## Solution

```py
class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k %= n

        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])
```

[View on LeetCode](https://leetcode.com/problems/rotate-array/)
