# 881. Boats to Save People

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Two_Pointers-blue) ![Topic](https://img.shields.io/badge/Topic-Greedy-blue) ![Topic](https://img.shields.io/badge/Topic-Sorting-blue) ![Topic](https://img.shields.io/badge/Topic-Timsort-blue) ![Language](https://img.shields.io/badge/Language-python-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 66 ms |
| Memory | 16.4 MB |
| Submission Date | 2026-10-30T09:00:25.163Z |
| Platform | leetcode |

## Problem Statement

<p>You are given an array <code>people</code> where <code>people[i]</code> is the weight of the <code>i<sup>th</sup></code> person, and an <strong>infinite number of boats</strong> where each boat can carry a maximum weight of <code>limit</code>. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most <code>limit</code>.</p>

<p>Return <em>the minimum number of boats to carry every given person</em>.</p>

<p>&nbsp;</p>

## Examples

**Example 1:**

```
Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)
```

**Example 2:**

```
Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)
```

**Example 3:**

```
Input: people = [3,5,3,4], limit = 5
Output: 4
Explanation: 4 boats (3), (3), (4), (5)
```

## Constraints

- <code>1 &lt;= people.length &lt;= 5 * 10<sup>4</sup></code>
- <code>1 &lt;= people[i] &lt;= limit &lt;= 3 * 10<sup>4</sup></code>

## Solution

```py

class Solution(object):
    def numRescueBoats(self, people, limit):
        people.sort()

        i, j = 0, len(people) - 1
        boats = 0

        while i <= j:
            if people[i] + people[j] <= limit:
                i += 1

            j -= 1
            boats += 1

        return boats

```

[View on LeetCode](https://leetcode.com/problems/boats-to-save-people/)
