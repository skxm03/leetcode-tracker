# 1529. Minimum Suffix Flips

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-String-blue) ![Topic](https://img.shields.io/badge/Topic-Greedy-blue) ![Language](https://img.shields.io/badge/Language-python-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 21 ms |
| Memory | 12.4 MB |
| Submission Date | 2026-10-31T13:51:59.562Z |
| Platform | leetcode |

## Problem Statement

<p>You are given a <strong>0-indexed</strong> binary string <code>target</code> of length <code>n</code>. You have another binary string <code>s</code> of length <code>n</code> that is initially set to all zeros. You want to make <code>s</code> equal to <code>target</code>.</p>

<p>In one operation, you can pick an index <code>i</code> where <code>0 &lt;= i &lt; n</code> and flip all bits in the <strong>inclusive</strong> range <code>[i, n - 1]</code>. Flip means changing <code>&#39;0&#39;</code> to <code>&#39;1&#39;</code> and <code>&#39;1&#39;</code> to <code>&#39;0&#39;</code>.</p>

<p>Return <em>the minimum number of operations needed to make </em><code>s</code><em> equal to </em><code>target</code>.</p>

<p>&nbsp;</p>

## Examples

**Example 1:**

```
Input: target = "10111"
Output: 3
Explanation: Initially, s = "00000".
Choose index i = 2: "00000" -> "00111"
Choose index i = 0: "00111" -> "11000"
Choose index i = 1: "11000" -> "10111"
We need at least 3 flip operations to form target.
```

**Example 2:**

```
Input: target = "101"
Output: 3
Explanation: Initially, s = "000".
Choose index i = 0: "000" -> "111"
Choose index i = 1: "111" -> "100"
Choose index i = 2: "100" -> "101"
We need at least 3 flip operations to form target.
```

**Example 3:**

```
Input: target = "00000"
Output: 0
Explanation: We do not need any operations since the initial s already equals target.
```

## Constraints

- <code>n == target.length</code>
- <code>1 &lt;= n &lt;= 10<sup>5</sup></code>
- <code>target[i]</code> is either <code>&#39;0&#39;</code> or <code>&#39;1&#39;</code>.

## Solution

```py
class Solution(object):
    def minFlips(self, target):
        ans = 0
        prev = '0'

        for ch in target:
            if ch != prev:
                ans += 1
                prev = ch

        return ans
        
```

[View on LeetCode](https://leetcode.com/problems/minimum-suffix-flips/)
