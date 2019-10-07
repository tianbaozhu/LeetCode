class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # time complexity O(m + log(n))
        # space complexity O(1)
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        index = 0
        while index < len(matrix):
            if target <= matrix[index][-1]:
                break
            index += 1
        if index == len(matrix):
            return False

        left = 0
        right = len(matrix[0])-1
        while left <= right:
            mid = (left+right) // 2
            if matrix[index][mid] == target:
                return True
            elif matrix[index][mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
