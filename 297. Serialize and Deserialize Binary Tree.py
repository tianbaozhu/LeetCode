# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        ret = ""
        queue = collections.deque()
        queue.append(root)
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node:
                    ret += str(node.val)+","
                else:
                    ret += "None,"
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
        return ret



    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = data.split(",")
        if data[0] == 'None':
            return None

        root = TreeNode(int(data[0]))
        queue = collections.deque()
        queue.append(root)
        index = 1
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if data[index] != "None":
                    node.left = TreeNode(int(data[index]))
                    queue.append(node.left)
                index += 1
                if data[index] != "None":
                    node.right = TreeNode(int(data[index]))
                    queue.append(node.right)
                index += 1
        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
