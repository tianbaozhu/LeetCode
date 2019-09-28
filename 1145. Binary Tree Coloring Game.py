# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def btreeGameWinningMove(self, root, n, x):
        """
        :type root: TreeNode
        :type n: int
        :type x: int
        :rtype: bool
        """
        start_node = None
        parent = left = right = 0
        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node.val == x:
                start_node = node
            else:
                parent += 1
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        if start_node.left:
            queue.append(start_node.left)
            while queue:
                node = queue.popleft()
                left += 1
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        if start_node.right:
            queue.append(start_node.right)
            while queue:
                node = queue.popleft()
                right += 1
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        if left+right+1 < parent or left+parent+1 < right or right+parent+1 < left:
            return True
        else:
            return False
            
"""
Input: root = [1,2,3,4,5,6,7,8,9,10,11], n = 11, x = 3
Output: true
Explanation: The second player can choose the node with value 2.
"""
