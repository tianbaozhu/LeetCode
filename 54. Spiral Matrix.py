class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # time complexity O(m * n)
        # space complexity O(1)

        if len(matrix) == 0:
            return []

        direction = ((0,1),(1,0),(0,-1),(-1,0))
        count = 0
        row = 0
        col = 0
        ret = []

        for _ in range(len(matrix)*len(matrix[0])):
            ret.append(matrix[row][col])
            matrix[row][col] = 'x'
            if ((col == len(matrix[0])-1 or matrix[row][col+1] == 'x') and count == 0) or ((row == len(matrix)-1 or matrix[row+1][col] == 'x') and count == 1) or ((col == 0 or matrix[row][col-1] == 'x') and count == 2) or ((row == 0 or matrix[row-1][col] == 'x') and count == 3):
                count += 1
                count %= 4
            row += direction[count][0]
            col += direction[count][1]
            
        return ret
