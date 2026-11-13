# 153. Find Minimum in Rotated Sorted Array

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Binary_Search-blue) ![Language](https://img.shields.io/badge/Language-python-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 0 ms |
| Memory | 12.4 MB |
| Submission Date | 2026-11-13T18:24:03.119Z |
| Platform | leetcode |

## Problem Statement

<p>Suppose an array of length <code>n</code> sorted in ascending order is <strong>rotated</strong> between <code>1</code> and <code>n</code> times. For example, the array <code>nums = [0,1,2,4,5,6,7]</code> might become:</p>

<ul>
	<li><code>[4,5,6,7,0,1,2]</code> if it was rotated <code>4</code> times.</li>
	<li><code>[0,1,2,4,5,6,7]</code> if it was rotated <code>7</code> times.</li>
</ul>

<p>Notice that <strong>rotating</strong> an array <code>[a[0], a[1], a[2], ..., a[n-1]]</code> 1 time results in the array <code>[a[n-1], a[0], a[1], a[2], ..., a[n-2]]</code>.</p>

<p>Given the sorted rotated array <code>nums</code> of <strong>unique</strong> elements, return <em>the minimum element of this array</em>.</p>

<p>You must write an algorithm that runs in&nbsp;<code>O(log n) time</code>.</p>

<p>&nbsp;</p>

## Examples

**Example 1:**

```
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
```

**Example 2:**

```
Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
```

**Example 3:**

```
Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times.
```

## Constraints

- <code>n == nums.length</code>
- <code>1 &lt;= n &lt;= 5000</code>
- <code>-5000 &lt;= nums[i] &lt;= 5000</code>
- All the integers of <code>nums</code> are <strong>unique</strong>.
- <code>nums</code> is sorted and rotated between <code>1</code> and <code>n</code> times.

## Solution

```py
class Solution(object):
    def findMin(self, nums):
        start, end = 0, len(nums) - 1

        while start < end:
            mid = (start + end) // 2

            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid

        return nums[start]
```

[View on LeetCode](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)
