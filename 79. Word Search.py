class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # time complexity O(m^2 * n^2)
        # space complexity O(m * n)
        if len(word) == 0:
            return True

        self.visited = set()
        def dfs(board, row, col, index):
            if index == len(word):
                return True
            if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) or board[row][col] != word[index] or (row,col) in self.visited:
                return False
            self.visited.add((row,col))
            ret = dfs(board, row+1,col,index+1) or dfs(board, row-1,col,index+1) or dfs(board, row,col+1,index+1) or dfs(board, row,col-1,index+1)
            self.visited.remove((row,col))
            return ret
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    self.visited = set()
                    if dfs(board, i, j, 0):
                        return True

        return False
