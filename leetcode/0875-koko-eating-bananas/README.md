# 875. Koko Eating Bananas

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Binary_Search-blue) ![Language](https://img.shields.io/badge/Language-python-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 153 ms |
| Memory | 13.6 MB |
| Submission Date | 2026-11-12T17:39:27.643Z |
| Platform | leetcode |

## Problem Statement

<p>Koko loves to eat bananas. There are <code>n</code> piles of bananas, the <code>i<sup>th</sup></code> pile has <code>piles[i]</code> bananas. The guards have gone and will come back in <code>h</code> hours.</p>

<p>Koko can decide her bananas-per-hour eating speed of <code>k</code>. Each hour, she chooses some pile of bananas and eats <code>k</code> bananas from that pile. If the pile has less than <code>k</code> bananas, she eats all of them instead and will not eat any more bananas during this hour.</p>

<p>Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.</p>

<p>Return the <strong>minimum</strong> integer <code>k</code> such that she can eat all the bananas <strong>within</strong> <code>h</code> hours.</p>

<p>&nbsp;</p>

## Examples

**Example 1:**

```
Input: piles = [3,6,7,11], h = 8

Output: 4

Explanation:

At a speed of 4 bananas per hour, Koko takes 1, 2, 2, and 3 hours to finish the respective piles, totaling 8 hours.
```

**Example 2:**

```
Input: piles = [30,11,23,4,20], h = 5

Output: 30

Explanation:

Koko must finish each pile in exactly 1 hour, so her minimum eating speed must be 30 bananas per hour.
```

**Example 3:**

```
Input: piles = [30,11,23,4,20], h = 6

Output: 23

Explanation:

At a speed of 23 bananas per hour, Koko takes 2 hours for the first pile and 1 hour for each remaining pile, totaling 6 hours.
```

## Constraints

- <code>1 &lt;= piles.length &lt;= 10<sup>4</sup></code>
- <code>piles.length &lt;= h &lt;= 10<sup>9</sup></code>
- <code>1 &lt;= piles[i] &lt;= 10<sup>9</sup></code>

## Solution

```py
class Solution(object):
    def minEatingSpeed(self, piles, h):
        start = 1
        end = max(piles)
        ans = end

        while start <= end:
            mid = (start + end) // 2

            hours = 0

            for pile in piles:
                hours += (pile + mid - 1) // mid

            if hours <= h:
                ans = mid
                end = mid - 1
            else:
                start = mid + 1

        return ans
```

[View on LeetCode](https://leetcode.com/problems/koko-eating-bananas/)
