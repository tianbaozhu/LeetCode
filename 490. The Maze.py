class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        # time complexity O(m * n)
        # space complexity O(m * n)
        destination = (destination[0], destination[1])
        visited = set()
        queue = collections.deque()
        queue.append((start[0], start[1]))
        while queue:
            pos = queue.popleft()
            if pos == destination:
                return True
            visited.add(pos)
            row, col = pos[0], pos[1]
            new_row = row
            while new_row > 0 and maze[new_row-1][col] == 0:
                new_row -= 1
            if (new_row, col) not in visited:
                queue.append((new_row, col))
            new_row = row
            while new_row < len(maze)-1 and maze[new_row+1][col] == 0:
                new_row += 1
            if (new_row, col) not in visited:
                queue.append((new_row, col))
            new_col = col
            while new_col > 0 and maze[row][new_col-1] == 0:
                new_col -= 1
            if (row, new_col) not in visited:
                queue.append((row, new_col))
            new_col = col
            while new_col < len(maze[0])-1 and maze[row][new_col+1] == 0:
                new_col += 1
            if (row, new_col) not in visited:
                queue.append((row, new_col))

        return False
