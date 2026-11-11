# 69. Sqrt(x)

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen) ![Topic](https://img.shields.io/badge/Topic-Math-blue) ![Topic](https://img.shields.io/badge/Topic-Binary_Search-blue) ![Topic](https://img.shields.io/badge/Topic-Newton's_Method-blue) ![Language](https://img.shields.io/badge/Language-python-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 2 ms |
| Memory | 12.2 MB |
| Submission Date | 2026-11-11T19:45:05.209Z |
| Platform | leetcode |

## Problem Statement

<p>Given a non-negative integer <code>x</code>, return <em>the square root of </em><code>x</code><em> rounded down to the nearest integer</em>. The returned integer should be <strong>non-negative</strong> as well.</p>

<p>You <strong>must not use</strong> any built-in exponent function or operator.</p>

<ul>
	<li>For example, do not use <code>pow(x, 0.5)</code> in c++ or <code>x ** 0.5</code> in python.</li>
</ul>

<p>&nbsp;</p>

## Examples

**Example 1:**

```
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
```

**Example 2:**

```
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
```

## Constraints

- <code>0 &lt;= x &lt;= 2<sup>31</sup> - 1</code>

## Solution

```py
class Solution(object):
    def mySqrt(self, x):
        start = 0
        end = x
        ans = 0

        while start <= end:
            mid = (start + end) // 2

            if mid * mid == x:
                return mid

            elif mid * mid < x:
                ans = mid
                start = mid + 1

            else:
                end = mid - 1

        return ans
```

[View on LeetCode](https://leetcode.com/problems/sqrtx/)
