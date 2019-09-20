# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        while l1 and l2:
            temp = l1.val + l2.val + carry
            carry = temp // 10
            curr.next = ListNode(temp%10)
            curr = curr.next
            l1, l2 = l1.next, l2.next
        while l1:
            temp = l1.val + carry
            carry = temp // 10
            curr.next = ListNode(temp%10)
            curr = curr.next
            l1 = l1.next
        while l2:
            temp = l2.val + carry
            carry = temp // 10
            curr.next = ListNode(temp%10)
            curr = curr.next
            l2 = l2.next
        if carry:
            curr.next = ListNode(1)
        return dummy.next

"""
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""
