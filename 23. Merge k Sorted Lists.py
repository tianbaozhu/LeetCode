# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        dummy = ListNode(0)
        curr = dummy
        for node in lists:
            while node:
                heapq.heappush(heap, (node.val, node))
                node = node.next
        while heap:
            curr.next = heapq.heappop(heap)[1]
            curr = curr.next
        curr.next = None
        return dummy.next

"""
Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""
