# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        if root is None:
            return None

        self.ret = []
        self.to_delete = set(to_delete)
        if root.val not in self.to_delete:
            self.ret.append(root)

        def helper(node):
            if node is None:
                return None
            if node.val in self.to_delete:
                node.left = helper(node.left)
                if node.left:
                    self.ret.append(node.left)
                node.right = helper(node.right)
                if node.right:
                    self.ret.append(node.right)
                return None
            node.left = helper(node.left)
            node.right = helper(node.right)
            return node

        helper(root)
        return self.ret

"""
Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]
"""
