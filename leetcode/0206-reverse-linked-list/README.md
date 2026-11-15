# 206. Reverse Linked List

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen) ![Topic](https://img.shields.io/badge/Topic-Linked_List-blue) ![Topic](https://img.shields.io/badge/Topic-Recursion-blue) ![Language](https://img.shields.io/badge/Language-python-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 0 ms |
| Memory | 14.3 MB |
| Submission Date | 2026-11-15T16:58:56.858Z |
| Platform | leetcode |

## Problem Statement

<p>Given the <code>head</code> of a singly linked list, reverse the list, and return <em>the reversed list</em>.</p>

<p>&nbsp;</p>

## Examples

**Example 1:**

```
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
```

**Example 2:**

```
Input: head = [1,2]
Output: [2,1]
```

**Example 3:**

```
Input: head = []
Output: []
```

## Constraints

- The number of nodes in the list is the range <code>[0, 5000]</code>.
- <code>-5000 &lt;= Node.val &lt;= 5000</code>

## Solution

```py
class Solution(object):
    def reverseList(self, head):
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev

            prev = curr
            curr = next_node

        return prev
```

[View on LeetCode](https://leetcode.com/problems/reverse-linked-list/)
