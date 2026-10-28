# 1338. Reduce Array Size to The Half

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Hash_Table-blue) ![Topic](https://img.shields.io/badge/Topic-Greedy-blue) ![Topic](https://img.shields.io/badge/Topic-Sorting-blue) ![Topic](https://img.shields.io/badge/Topic-Heap_(Priority_Queue)-blue) ![Language](https://img.shields.io/badge/Language-python-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 56 ms |
| Memory | 23 MB |
| Submission Date | 2026-10-28T03:59:45.107Z |
| Platform | leetcode |

## Problem Statement

<p>You are given an integer array <code>arr</code>. You can choose a set of integers and remove all the occurrences of these integers in the array.</p>

<p>Return <em>the minimum size of the set so that <strong>at least</strong> half of the integers of the array are removed</em>.</p>

<p>&nbsp;</p>

## Examples

**Example 1:**

```
Input: arr = [3,3,3,3,5,5,5,2,2,7]
Output: 2
Explanation: Choosing {3,7} will make the new array [5,5,5,2,2] which has size 5 (i.e equal to half of the size of the old array).
Possible sets of size 2 are {3,5},{3,2},{5,2}.
Choosing set {2,7} is not possible as it will make the new array [3,3,3,3,5,5,5] which has a size greater than half of the size of the old array.
```

**Example 2:**

```
Input: arr = [7,7,7,7,7,7]
Output: 1
Explanation: The only possible set you can choose is {7}. This will make the new array empty.
```

## Constraints

- <code>2 &lt;= arr.length &lt;= 10<sup>5</sup></code>
- <code>arr.length</code> is even.
- <code>1 &lt;= arr[i] &lt;= 10<sup>5</sup></code>

## Solution

```py

class Solution(object):
    def minSetSize(self, arr):
        d = {}

        for num in arr:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1

        freq = sorted(d.values(), reverse=True)

        removed = 0
        for i, count in enumerate(freq):
            removed += count

            if removed >= len(arr) // 2:
                return i + 1

```

[View on LeetCode](https://leetcode.com/problems/reduce-array-size-to-the-half/)
