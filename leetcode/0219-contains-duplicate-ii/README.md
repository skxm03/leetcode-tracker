# 219. Contains Duplicate II

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Hash_Table-blue) ![Topic](https://img.shields.io/badge/Topic-Sliding_Window-blue) ![Language](https://img.shields.io/badge/Language-python-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 94 ms |
| Memory | 26.5 MB |
| Submission Date | 2026-11-09T17:24:35.264Z |
| Platform | leetcode |

## Problem Statement

<p>Given an integer array <code>nums</code> and an integer <code>k</code>, return <code>true</code> <em>if there are two <strong>distinct indices</strong> </em><code>i</code><em> and </em><code>j</code><em> in the array such that </em><code>nums[i] == nums[j]</code><em> and </em><code>abs(i - j) &lt;= k</code>.</p>

<p>&nbsp;</p>

## Examples

**Example 1:**

```
Input: nums = [1,2,3,1], k = 3
Output: true
```

**Example 2:**

```
Input: nums = [1,0,1,1], k = 1
Output: true
```

**Example 3:**

```
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
```

## Constraints

- <code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code>
- <code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code>
- <code>0 &lt;= k &lt;= 10<sup>5</sup></code>

## Solution

```py
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        window = set()

        for i in range(len(nums)):
            if nums[i] in window:
                return True

            window.add(nums[i])

            if len(window) > k:
                window.remove(nums[i - k])

        return False
```

[View on LeetCode](https://leetcode.com/problems/contains-duplicate-ii/)
