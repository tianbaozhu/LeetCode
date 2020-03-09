# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # time complexity O(n)
        # space complexity O(1)
        if head is None or k == 0:
            return head
        total = 0
        old_head = head
        while head:
            total += 1
            head = head.next

        shift = k % total
        if shift == 0:
            return old_head

        curr = old_head
        for i in range(total-shift-1):
            curr = curr.next
        new_head = curr.next
        curr.next = None
        curr = new_head
        while curr.next:
            curr = curr.next
        curr.next = old_head

        return new_head
