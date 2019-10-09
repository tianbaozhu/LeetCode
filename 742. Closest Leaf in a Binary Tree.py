# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findClosestLeaf(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # time complexity O(n)
        # space complexity O(n)
        graph = collections.defaultdict(list)
        target = None

        queue = collections.deque()
        queue.append((root, None))
        while queue:
            for _ in range(len(queue)):
                node, parent = queue.popleft()
                if node.val == k:
                    target = node
                if parent is not None:
                    graph[node].append(parent)
                if node.left:
                    graph[node].append(node.left)
                    queue.append((node.left, node))
                if node.right:
                    graph[node].append(node.right)
                    queue.append((node.right, node))

        queue = collections.deque()
        queue.append(target)
        visited = set()
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                visited.add(node.val)
                if node.left is None and node.right is None:
                    return node.val
                for neighbor in graph[node]:
                    if neighbor.val not in visited:
                        queue.append(neighbor)
