# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # time complexity O(n)
        # space complexity O(n)
        if root is None:
            return 0

        ret = 0
        queue = collections.deque()
        queue.append((root, 0, 0))

        while queue:
            node, level, prev = queue.popleft()
            if node.val == prev + 1:
                level += 1
            else:
                level = 1
            ret = max(ret, level)
            if node.left:
                queue.append((node.left, level, node.val))
            if node.right:
                queue.append((node.right, level, node.val))

        return ret
