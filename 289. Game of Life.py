class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        ret = [[0 for x in range(len(board[0]))] for y in range(len(board))]
        directions = [(0,1),(0,-1),(1,0),(-1,0),(1,-1),(-1,1),(1,1),(-1,-1)]

        for i in range(len(board)):
            for j in range(len(board[0])):
                neighbors = 0
                for direction in directions:
                    row = i + direction[0]
                    col = j + direction[1]
                    if row >= 0 and row < len(board) and col >= 0 and col < len(board[0]) and board[row][col] == 1:
                        neighbors += 1
                if board[i][j] == 0 and neighbors == 3:
                    ret[i][j] = 1
                elif board[i][j] == 1 and neighbors >= 2 and neighbors <= 3:
                    ret[i][j] = 1
                else:
                    ret[i][j] = 0

        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = ret[i][j]


"""
Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Input:
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output:
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
"""
