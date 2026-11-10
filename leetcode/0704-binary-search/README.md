# 704. Binary Search

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Binary_Search-blue) ![Language](https://img.shields.io/badge/Language-python-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 0 ms |
| Memory | 12.9 MB |
| Submission Date | 2026-11-10T18:39:35.536Z |
| Platform | leetcode |

## Problem Statement

<p>Given an array of integers <code>nums</code> which is sorted in ascending order, and an integer <code>target</code>, write a function to search <code>target</code> in <code>nums</code>. If <code>target</code> exists, then return its index. Otherwise, return <code>-1</code>.</p>

<p>You must write an algorithm with <code>O(log n)</code> runtime complexity.</p>

<p>&nbsp;</p>

## Examples

**Example 1:**

```
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
```

**Example 2:**

```
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
```

## Constraints

- <code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code>
- <code>-10<sup>4</sup> &lt; nums[i], target &lt; 10<sup>4</sup></code>
- All the integers in <code>nums</code> are <strong>unique</strong>.
- <code>nums</code> is sorted in ascending order.

## Solution

```py
class Solution(object):
    def search(self, nums, target):
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                start = mid + 1

            else:
                end = mid - 1

        return -1
```

[View on LeetCode](https://leetcode.com/problems/binary-search/)
