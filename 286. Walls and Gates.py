class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        # time complexity O(m * n)
        # space complexity O(m * n)
        queue = collections.deque()

        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    queue.append((i, j, 0))

        while queue:
            for _ in range(len(queue)):
                row, col, level = queue.popleft()
                rooms[row][col] = min(rooms[row][col], level)
                for x, y in ((1,0),(-1,0),(0,1),(0,-1)):
                    nrow, ncol = row+x, col+y
                    if nrow >= 0 and nrow < len(rooms) and ncol >= 0 and ncol < len(rooms[0]) and rooms[nrow][ncol] == 2147483647:
                        queue.append((nrow, ncol, level+1))
