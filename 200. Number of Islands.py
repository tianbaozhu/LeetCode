class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # BFS
        ret = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    queue = collections.deque()
                    queue.append((i,j))
                    while queue:
                        for _ in range(len(queue)):
                            row, col = queue.popleft()
                            if grid[row][col] == '1':
                                grid[row][col] = '0'
                                if row > 0 and grid[row-1][col] == '1':
                                    queue.append((row-1, col))
                                if row < len(grid)-1 and grid[row+1][col] == '1':
                                    queue.append((row+1, col))
                                if col > 0 and grid[row][col-1] == '1':
                                    queue.append((row, col-1))
                                if col < len(grid[0])-1 and grid[row][col+1] == '1':
                                    queue.append((row, col+1))
                    ret += 1
        return ret

    def numIslands1(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # DFS
        def dfs(row, col):
            grid[row][col] = '0'
            if row > 0 and grid[row-1][col] == '1':
                dfs(row-1, col)
            if row < len(grid)-1 and grid[row+1][col] == '1':
                dfs(row+1, col)
            if col > 0 and grid[row][col-1] == '1':
                dfs(row, col-1)
            if col < len(grid[0])-1 and grid[row][col+1] == '1':
                dfs(row, col+1)
        ret = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    ret += 1
        return ret

"""
Input:
11110
11010
11000
00000
Output: 1

Input:
11000
11000
00100
00011
Output: 3
"""
