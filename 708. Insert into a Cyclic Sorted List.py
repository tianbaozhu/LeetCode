"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next):
        self.val = val
        self.next = next
"""
class Solution(object):
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        if head is None:
            new = Node(insertVal)
            new.next = new
            return new

        curr = head
        flag = False
        
        while curr: # find start point
            if curr.next.val < curr.val or (flag == True and curr == head):
                break
            if flag == False and curr == head:
                flag = True
            curr = curr.next

        if curr.val <= insertVal or insertVal <= curr.next.val:
            temp = Node(insertVal)
            temp.next = curr.next
            curr.next = temp
            return head

        while curr:
            if curr.next.val >= insertVal:
                temp = Node(insertVal)
                temp.next = curr.next
                curr.next = temp
                return head
            curr = curr.next
