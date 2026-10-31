# 135. Candy

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Greedy-blue) ![Language](https://img.shields.io/badge/Language-python-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 75 ms |
| Memory | 17.4 MB |
| Submission Date | 2026-10-31T13:50:21.162Z |
| Platform | leetcode |

## Problem Statement

<p>There are <code>n</code> children standing in a line.</p>

<p>Each child is assigned a rating value given in the integer array <code>ratings</code>.</p>

<p>You are giving candies to these children subjected to the following requirements:</p>

<ul>
	<li>Each child must have <strong>at least</strong> one candy.</li>
	<li>Children with a <strong>higher</strong> rating get more candies than their neighbors.</li>
</ul>

<p>Return the <strong>minimum</strong> number of candies you need to have to distribute the candies to the children.</p>

<p>&nbsp;</p>

## Examples

**Example 1:**

```
Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
```

**Example 2:**

```
Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.
```

## Constraints

- <code>1 &lt;= n == ratings.length &lt;= 5 * 10<sup>4</sup></code>
- <code>0 &lt;= ratings[i] &lt;= 5 * 10<sup>4</sup></code>

## Solution

```py
class Solution(object):
    def candy(self, ratings):
        n = len(ratings)
        candies = [1] * n

        # Left to right
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # Right to left
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(
                    candies[i],
                    candies[i + 1] + 1
                )

        return sum(candies)
        
```

[View on LeetCode](https://leetcode.com/problems/candy/)
