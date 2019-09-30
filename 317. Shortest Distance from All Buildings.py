class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # time complexity O(m^2 * n^2)
        # space complexity O(m * n)
        ret = [[0 for x in range(len(grid[0]))] for y in range(len(grid))]
        min_dis = float('inf')

        # calculate total number of houses
        house = 0
        start = None
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    house += 1
                    start = (i,j)

        # check there is at least one valid path connects all houses
        queue = collections.deque()
        visited = set()
        queue.append(start)
        visited.add(start)
        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                if row > 0 and (row-1,col) not in visited:
                    if grid[row-1][col] == 0:
                        queue.append((row-1, col))
                    elif grid[row-1][col] == 1:
                        house -= 1
                    visited.add((row-1, col))
                if row < len(grid)-1 and (row+1,col) not in visited:
                    if grid[row+1][col] == 0:
                        queue.append((row+1, col))
                    elif grid[row+1][col] == 1:
                        house -= 1
                    visited.add((row+1, col))
                if col > 0 and (row,col-1) not in visited:
                    if grid[row][col-1] == 0:
                        queue.append((row, col-1))
                    elif grid[row][col-1] == 1:
                        house -= 1
                    visited.add((row, col-1))
                if col < len(grid[0])-1 and (row,col+1) not in visited:
                    if grid[row][col+1] == 0:
                        queue.append((row, col+1))
                    elif grid[row][col+1] == 1:
                        house -= 1
                    visited.add((row, col+1))
        if house != 1:
            return -1

        # calculate distance
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    queue = collections.deque()
                    visited = set()
                    queue.append((i, j, 0))
                    while queue:
                        for _ in range(len(queue)):
                            row, col, level = queue.popleft()
                            ret[row][col] += level
                            if row > 0 and grid[row-1][col] == 0 and (row-1,col) not in visited:
                                queue.append((row-1, col, level+1))
                                visited.add((row-1, col))
                            if row < len(grid)-1 and grid[row+1][col] == 0 and (row+1,col) not in visited:
                                queue.append((row+1, col, level+1))
                                visited.add((row+1, col))
                            if col > 0 and grid[row][col-1] == 0 and (row,col-1) not in visited:
                                queue.append((row, col-1, level+1))
                                visited.add((row, col-1))
                            if col < len(grid[0])-1 and grid[row][col+1] == 0 and (row,col+1) not in visited:
                                queue.append((row, col+1, level+1))
                                visited.add((row, col+1))
                    for x in range(len(grid)):
                        for y in range(len(grid[0])):
                            if (x,y) not in visited:
                                ret[x][y] = float('inf')
        # get min_dis
        for i in range(len(ret)):
            for j in range(len(ret[0])):
                min_dis = min(min_dis, ret[i][j])

        return min_dis if min_dis < float('inf') else -1
