# 451. Sort Characters By Frequency

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-Hash_Table-blue) ![Topic](https://img.shields.io/badge/Topic-String-blue) ![Topic](https://img.shields.io/badge/Topic-Sorting-blue) ![Topic](https://img.shields.io/badge/Topic-Heap_(Priority_Queue)-blue) ![Topic](https://img.shields.io/badge/Topic-Bucket_Sort-blue) ![Topic](https://img.shields.io/badge/Topic-Counting-blue) ![Language](https://img.shields.io/badge/Language-python-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 16 ms |
| Memory | 13.2 MB |
| Submission Date | 2026-10-28T04:07:04.884Z |
| Platform | leetcode |

## Problem Statement

<p>Given a string <code>s</code>, sort it in <strong>decreasing order</strong> based on the <strong>frequency</strong> of the characters. The <strong>frequency</strong> of a character is the number of times it appears in the string.</p>

<p>Return <em>the sorted string</em>. If there are multiple answers, return <em>any of them</em>.</p>

<p>&nbsp;</p>

## Examples

**Example 1:**

```
Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
```

**Example 2:**

```
Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.
```

**Example 3:**

```
Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
```

## Constraints

- <code>1 &lt;= s.length &lt;= 5 * 10<sup>5</sup></code>
- <code>s</code> consists of uppercase and lowercase English letters and digits.

## Solution

```py
class Solution(object):
    def frequencySort(self, s):
        d = {}

        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        
        x = sorted(d, key = lambda x: d[x], reverse = True)
        s = ''
        for i in x:
            s += i*d[i]
        return s
        
```

[View on LeetCode](https://leetcode.com/problems/sort-characters-by-frequency/)
