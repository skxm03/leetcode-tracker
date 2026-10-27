# 1029. Two City Scheduling

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Greedy-blue) ![Topic](https://img.shields.io/badge/Topic-Sorting-blue) ![Topic](https://img.shields.io/badge/Topic-Hungarian_Algorithm-blue) ![Topic](https://img.shields.io/badge/Topic-Successive_Shortest_Path_Algorithm-blue) ![Language](https://img.shields.io/badge/Language-python-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 1 ms |
| Memory | 12.3 MB |
| Submission Date | 2026-10-27T04:02:15.913Z |
| Platform | leetcode |

## Problem Statement

<p>A company is planning to interview <code>2n</code> people. Given the array <code>costs</code> where <code>costs[i] = [aCost<sub>i</sub>, bCost<sub>i</sub>]</code>,&nbsp;the cost of flying the <code>i<sup>th</sup></code> person to city <code>a</code> is <code>aCost<sub>i</sub></code>, and the cost of flying the <code>i<sup>th</sup></code> person to city <code>b</code> is <code>bCost<sub>i</sub></code>.</p>

<p>Return <em>the minimum cost to fly every person to a city</em> such that exactly <code>n</code> people arrive in each city.</p>

<p>&nbsp;</p>

## Examples

**Example 1:**

```
Input: costs = [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation: 
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
```

**Example 2:**

```
Input: costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
Output: 1859
```

**Example 3:**

```
Input: costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]
Output: 3086
```

## Constraints

- <code>2 * n == costs.length</code>
- <code>2 &lt;= costs.length &lt;= 100</code>
- <code>costs.length</code> is even.
- <code>1 &lt;= aCost<sub>i</sub>, bCost<sub>i</sub> &lt;= 1000</code>

## Solution

```py
class Solution(object):
    def twoCitySchedCost(self, costs):
        costs.sort(key=lambda x: x[0] - x[1])

        n = len(costs)
        ans = 0

        for i in range(n // 2):
            ans += costs[i][0]

        for i in range(n // 2, n):
            ans += costs[i][1]

        return ans

```

[View on LeetCode](https://leetcode.com/problems/two-city-scheduling/)
