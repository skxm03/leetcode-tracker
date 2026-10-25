# 680. Valid Palindrome II

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen) ![Topic](https://img.shields.io/badge/Topic-Two_Pointers-blue) ![Topic](https://img.shields.io/badge/Topic-String-blue) ![Topic](https://img.shields.io/badge/Topic-Greedy-blue) ![Language](https://img.shields.io/badge/Language-python-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 36 ms |
| Memory | 12.5 MB |
| Submission Date | 2026-10-25T16:21:21.714Z |
| Platform | leetcode |

## Problem Statement

<p>Given a string <code>s</code>, return <code>true</code> <em>if the </em><code>s</code><em> can be palindrome after deleting <strong>at most one</strong> character from it</em>.</p>

<p>&nbsp;</p>

## Examples

**Example 1:**

```
Input: s = "aba"
Output: true
```

**Example 2:**

```
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
```

**Example 3:**

```
Input: s = "abc"
Output: false
```

## Constraints

- <code>1 &lt;= s.length &lt;= 10<sup>5</sup></code>
- <code>s</code> consists of lowercase English letters.

## Solution

```py
class Solution(object):
    def validPalindrome(self, s):
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                a = s[l+1:r+1]
                b = s[l:r]
                return a == a[::-1] or b == b[::-1]

            l += 1
            r -= 1

        return True
```

[View on LeetCode](https://leetcode.com/problems/valid-palindrome-ii/)
