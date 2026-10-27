# 56. Merge Intervals

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Sorting-blue) ![Topic](https://img.shields.io/badge/Topic-Quicksort-blue) ![Language](https://img.shields.io/badge/Language-python-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 13 ms |
| Memory | 16.7 MB |
| Submission Date | 2026-10-27T03:57:33.537Z |
| Platform | leetcode |

## Problem Statement

<p>Given an array&nbsp;of <code>intervals</code>&nbsp;where <code>intervals[i] = [start<sub>i</sub>, end<sub>i</sub>]</code>, merge all overlapping intervals, and return <em>an array of the non-overlapping intervals that cover all the intervals in the input</em>.</p>

<p>&nbsp;</p>

## Examples

**Example 1:**

```
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
```

**Example 2:**

```
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
```

**Example 3:**

```
Input: intervals = [[4,7],[1,4]]
Output: [[1,7]]
Explanation: Intervals [1,4] and [4,7] are considered overlapping.
```

## Constraints

- <code>1 &lt;= intervals.length &lt;= 10<sup>4</sup></code>
- <code>intervals[i].length == 2</code>
- <code>0 &lt;= start<sub>i</sub> &lt;= end<sub>i</sub> &lt;= 10<sup>4</sup></code>

## Solution

```py
class Solution(object):
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])

        output = []
        st = intervals[0][0]
        e = intervals[0][1]

        for start, end in intervals[1:]:
            if start <= e:
                st = min(st, start)
                e = max(e, end)
            else:
                output.append([st, e])
                st = start
                e = end

        output.append([st, e])
        return output
```

[View on LeetCode](https://leetcode.com/problems/merge-intervals/)
