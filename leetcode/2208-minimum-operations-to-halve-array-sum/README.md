# 2208. Minimum Operations to Halve Array Sum

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Greedy-blue) ![Topic](https://img.shields.io/badge/Topic-Heap_(Priority_Queue)-blue) ![Language](https://img.shields.io/badge/Language-python-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 1186 ms |
| Memory | 23.4 MB |
| Submission Date | 2026-10-29T08:49:51.529Z |
| Platform | leetcode |

## Problem Statement

<p>You are given an array <code>nums</code> of positive integers. In one operation, you can choose <strong>any</strong> number from <code>nums</code> and reduce it to <strong>exactly</strong> half the number. (Note that you may choose this reduced number in future operations.)</p>

<p>Return<em> the <strong>minimum</strong> number of operations to reduce the sum of </em><code>nums</code><em> by <strong>at least</strong> half.</em></p>

<p>&nbsp;</p>

## Examples

**Example 1:**

```
Input: nums = [5,19,8,1]
Output: 3
Explanation: The initial sum of nums is equal to 5 + 19 + 8 + 1 = 33.
The following is one of the ways to reduce the sum by at least half:
Pick the number 19 and reduce it to 9.5.
Pick the number 9.5 and reduce it to 4.75.
Pick the number 8 and reduce it to 4.
The final array is [5, 4.75, 4, 1] with a total sum of 5 + 4.75 + 4 + 1 = 14.75. 
The sum of nums has been reduced by 33 - 14.75 = 18.25, which is at least half of the initial sum, 18.25 >= 33/2 = 16.5.
Overall, 3 operations were used so we return 3.
It can be shown that we cannot reduce the sum by at least half in less than 3 operations.
```

**Example 2:**

```
Input: nums = [3,8,20]
Output: 3
Explanation: The initial sum of nums is equal to 3 + 8 + 20 = 31.
The following is one of the ways to reduce the sum by at least half:
Pick the number 20 and reduce it to 10.
Pick the number 10 and reduce it to 5.
Pick the number 3 and reduce it to 1.5.
The final array is [1.5, 8, 5] with a total sum of 1.5 + 8 + 5 = 14.5. 
The sum of nums has been reduced by 31 - 14.5 = 16.5, which is at least half of the initial sum, 16.5 >= 31/2 = 15.5.
Overall, 3 operations were used so we return 3.
It can be shown that we cannot reduce the sum by at least half in less than 3 operations.
```

## Constraints

- <code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code>
- <code>1 &lt;= nums[i] &lt;= 10<sup>7</sup></code>

## Solution

```py
import heapq

class Solution(object):
    def halveArray(self, nums):
        total = sum(nums)
        target = total / 2.0

        heap = [-x for x in nums]
        heapq.heapify(heap)

        reduced = 0.0
        ops = 0

        while reduced < target:
            largest = -heapq.heappop(heap)
            half = largest / 2.0

            reduced += half
            heapq.heappush(heap, -half)
            ops += 1

        return ops
```

[View on LeetCode](https://leetcode.com/problems/minimum-operations-to-halve-array-sum/)
