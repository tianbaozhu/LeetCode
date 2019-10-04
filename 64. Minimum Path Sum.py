class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # time complexity: O(m * n)
        # space complexity: O(m * n)
        if len(grid) == 0:
            return 0
        dp = [[0 for x in range(len(grid[0]))] for y in range(len(grid))]
        dp[0][0] = grid[0][0]
        for i in range(1, len(grid)):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for i in range(1, len(grid[0])):
            dp[0][i] = dp[0][i-1] + grid[0][i]
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[-1][-1]

    def minPathSum1(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # time complexity: O(m * n)
        # space complexity: O(n)
        if len(grid) == 0:
            return 0
        dp = [0 for x in range(len(grid[0]))]
        dp[0] = grid[0][0]
        for i in range(1, len(grid[0])):
            dp[i] = dp[i-1] + grid[0][i]
        print(dp)
        for i in range(1, len(grid)):
            for j in range(len(grid[0])):
                if j == 0:
                    dp[0] += grid[i][j]
                else:
                    dp[j] = min(dp[j-1], dp[j]) + grid[i][j]
        return dp[-1]

    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # time complexity: O(m * n)
        # space complexity: O(1)
        if len(grid) == 0:
            return 0
        for i in range(1, len(grid)):
            grid[i][0] = grid[i-1][0] + grid[i][0]
        for i in range(1, len(grid[0])):
            grid[0][i] = grid[0][i-1] + grid[0][i]
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]
        return grid[-1][-1]
        
"""
Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""
