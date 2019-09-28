class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.ret = []

        def helper(left, right, n, curr):
            if right == n:
                self.ret.append(curr)
                return
            if left < n:
                helper(left+1, right, n, curr+'(')
            if right < left:
                helper(left, right+1, n, curr+')')
                
        helper(0, 0, n, "")
        return self.ret

"""
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""
