# 860. Lemonade Change

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Greedy-blue) ![Language](https://img.shields.io/badge/Language-python-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 7 ms |
| Memory | 15 MB |
| Submission Date | 2026-10-30T08:25:46.782Z |
| Platform | leetcode |

## Problem Statement

<p>At a lemonade stand, each lemonade costs <code>$5</code>. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a <code>$5</code>, <code>$10</code>, or <code>$20</code> bill. You must provide the correct change to each customer so that the net transaction is that the customer pays <code>$5</code>.</p>

<p>Note that you do not have any change in hand at first.</p>

<p>Given an integer array <code>bills</code> where <code>bills[i]</code> is the bill the <code>i<sup>th</sup></code> customer pays, return <code>true</code> <em>if you can provide every customer with the correct change, or</em> <code>false</code> <em>otherwise</em>.</p>

<p>&nbsp;</p>

## Examples

**Example 1:**

```
Input: bills = [5,5,5,10,20]
Output: true
Explanation: 
From the first 3 customers, we collect three $5 bills in order.
From the fourth customer, we collect a $10 bill and give back a $5.
From the fifth customer, we give a $10 bill and a $5 bill.
Since all customers got correct change, we output true.
```

**Example 2:**

```
Input: bills = [5,5,10,10,20]
Output: false
Explanation: 
From the first two customers in order, we collect two $5 bills.
For the next two customers in order, we collect a $10 bill and give back a $5 bill.
For the last customer, we can not give the change of $15 back because we only have two $10 bills.
Since not every customer received the correct change, the answer is false.
```

## Constraints

- <code>1 &lt;= bills.length &lt;= 10<sup>5</sup></code>
- <code>bills[i]</code> is either <code>5</code>, <code>10</code>, or <code>20</code>.

## Solution

```py
class Solution(object):
    def lemonadeChange(self, bills):
        bank = {5: 0, 10: 0, 20: 0}

        for i in bills:
            if i == 5:
                bank[5] += 1

            elif i == 10:
                if bank[5] < 1:
                    return False

                bank[5] -= 1
                bank[10] += 1

            elif i == 20:
                if bank[5] >= 1 and bank[10] >= 1:
                    bank[5] -= 1
                    bank[10] -= 1

                elif bank[5] >= 3:
                    bank[5] -= 3

                else:
                    return False

                bank[20] += 1

        return True
```

[View on LeetCode](https://leetcode.com/problems/lemonade-change/)
