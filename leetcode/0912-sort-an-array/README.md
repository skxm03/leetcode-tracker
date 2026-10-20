# 912. Sort an Array

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Divide_and_Conquer-blue) ![Topic](https://img.shields.io/badge/Topic-Sorting-blue) ![Topic](https://img.shields.io/badge/Topic-Heap_(Priority_Queue)-blue) ![Topic](https://img.shields.io/badge/Topic-Merge_Sort-blue) ![Topic](https://img.shields.io/badge/Topic-Bucket_Sort-blue) ![Topic](https://img.shields.io/badge/Topic-Radix_Sort-blue) ![Topic](https://img.shields.io/badge/Topic-Counting_Sort-blue) ![Language](https://img.shields.io/badge/Language-python-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 1238 ms |
| Memory | 21.2 MB |
| Submission Date | 2026-10-20T18:22:56.295Z |
| Platform | leetcode |

## Problem Statement

<p>Given an array of integers <code>nums</code>, sort the array in ascending order and return it.</p>

<p>You must solve the problem <strong>without using any built-in</strong> functions in <code>O(nlog(n))</code> time complexity and with the smallest space complexity possible.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<pre>
<strong>Input:</strong> nums = [5,2,3,1]
<strong>Output:</strong> [1,2,3,5]
<strong>Explanation:</strong> After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
</pre>

<p>
```

**Example 2:**

```
</p>

<pre>
<strong>Input:</strong> nums = [5,1,1,2,0,0]
<strong>Output:</strong> [0,0,1,1,2,5]
<strong>Explanation:</strong> Note that the values of nums are not necessarily unique.
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>1 &lt;= nums.length &lt;= 5 * 10<sup>4</sup></code>
- <code>-5 * 10<sup>4</sup> &lt;= nums[i] &lt;= 5 * 10<sup>4</sup></code>

## Solution

```py
class Solution(object):
    def sortArray(self, nums):
        def MergeSort(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2
            left = MergeSort(arr[:mid])
            right = MergeSort(arr[mid:])

            return Merge(left, right)

        def Merge(left, right):
            i = j = 0
            res = []

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1

            while i < len(left):
                res.append(left[i])
                i += 1

            while j < len(right):
                res.append(right[j])
                j += 1

            return res

        return MergeSort(nums)
```

[View on LeetCode](https://leetcode.com/problems/sort-an-array/)
