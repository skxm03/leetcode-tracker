# 21. Merge Two Sorted Lists

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen) ![Topic](https://img.shields.io/badge/Topic-Linked_List-blue) ![Topic](https://img.shields.io/badge/Topic-Recursion-blue) ![Language](https://img.shields.io/badge/Language-python-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 0 ms |
| Memory | 12.4 MB |
| Submission Date | 2026-11-15T17:00:59.641Z |
| Platform | leetcode |

## Problem Statement

<p>You are given the heads of two sorted linked lists <code>list1</code> and <code>list2</code>.</p>

<p>Merge the two lists into one <strong>sorted</strong> list. The list should be made by splicing together the nodes of the first two lists.</p>

<p>Return <em>the head of the merged linked list</em>.</p>

<p>&nbsp;</p>

## Examples

**Example 1:**

```
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
```

**Example 2:**

```
Input: list1 = [], list2 = []
Output: []
```

**Example 3:**

```
Input: list1 = [], list2 = [0]
Output: [0]
```

## Constraints

- The number of nodes in both lists is in the range <code>[0, 50]</code>.
- <code>-100 &lt;= Node.val &lt;= 100</code>
- Both <code>list1</code> and <code>list2</code> are sorted in <strong>non-decreasing</strong> order.

## Solution

```py
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(-1)
        curr = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next

            curr = curr.next

        if list1:
            curr.next = list1
        else:
            curr.next = list2

        return dummy.next
```

[View on LeetCode](https://leetcode.com/problems/merge-two-sorted-lists/)
