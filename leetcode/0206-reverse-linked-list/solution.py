# Runtime: 0 ms
# Memory: 14.3 MB

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