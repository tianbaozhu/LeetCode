class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0:
            return 0

        ret = 0
        dp = [[0 for x in range(len(matrix[0])+1)] for y in range(len(matrix)+1)]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    dp[i+1][j+1] = min(dp[i][j], dp[i+1][j], dp[i][j+1]) + 1
                    ret = max(ret, dp[i+1][j+1])
                else:
                    dp[i+1][j+1] = 0

        return ret**2

"""
Input:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
"""
