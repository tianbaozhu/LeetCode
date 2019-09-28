class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visited = set()

        while n not in visited:
            visited.add(n)
            modified = 0
            while n > 0:
                modified += (n%10)**2
                n = n // 10
            if modified == 1:
                return True
            else:
                n = modified

        return False

"""
Input: 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""
