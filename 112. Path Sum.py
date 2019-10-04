# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """

        if root is None:
            return False

        def helper(node, curr):
            curr += node.val

            if node.left and node.right:
                return helper(node.left, curr) or helper(node.right, curr)
            elif node.left:
                return helper(node.left, curr)
            elif node.right:
                return helper(node.right, curr)
            else:
                return curr == sum

        return helper(root, 0)
        
"""
Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""
