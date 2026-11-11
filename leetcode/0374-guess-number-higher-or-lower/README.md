# 374. Guess Number Higher or Lower

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen) ![Topic](https://img.shields.io/badge/Topic-Binary_Search-blue) ![Topic](https://img.shields.io/badge/Topic-Interactive-blue) ![Language](https://img.shields.io/badge/Language-python-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 16 ms |
| Memory | 12.1 MB |
| Submission Date | 2026-11-11T19:38:30.857Z |
| Platform | leetcode |

## Problem Statement

<p>We are playing the Guess Game. The game is as follows:</p>

<p>I pick a number from <code>1</code> to <code>n</code>. You have to guess which number I picked (the number I picked stays the same throughout the game).</p>

<p>Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.</p>

<p>You call a pre-defined API <code>int guess(int num)</code>, which returns three possible results:</p>

<ul>
	<li><code>-1</code>: Your guess is higher than the number I picked (i.e. <code>num &gt; pick</code>).</li>
	<li><code>1</code>: Your guess is lower than the number I picked (i.e. <code>num &lt; pick</code>).</li>
	<li><code>0</code>: your guess is equal to the number I picked (i.e. <code>num == pick</code>).</li>
</ul>

<p>Return <em>the number that I picked</em>.</p>

<p>&nbsp;</p>

## Examples

**Example 1:**

```
Input: n = 10, pick = 6
Output: 6
```

**Example 2:**

```
Input: n = 1, pick = 1
Output: 1
```

**Example 3:**

```
Input: n = 2, pick = 1
Output: 1
```

## Constraints

- <code>1 &lt;= n &lt;= 2<sup>31</sup> - 1</code>
- <code>1 &lt;= pick &lt;= n</code>

## Solution

```py
class Solution(object):
    def guessNumber(self, n):
        start = 1
        end = n

        while start <= end:
            mid = (start + end) // 2

            res = guess(mid)

            if res == 0:
                return mid

            elif res == -1:
                end = mid - 1

            else:
                start = mid + 1

        return -1
```

[View on LeetCode](https://leetcode.com/problems/guess-number-higher-or-lower/)
