class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        # time complexity O(n)
        # space complexity O(n)
        stack = []
        for ch in S:
            if len(stack) == 0 or stack[-1] != ch:
                stack.append(ch)
            else:
                stack.pop()
        return "".join(stack)

"""
Input: "abbaca"
Output: "ca"
Explanation:
For example, in "abbaca" we could remove "bb" since the letters are adjacent
and equal, and this is the only possible move.  The result of this move is that
the string is "aaca", of which only "aa" is possible, so the final string is "ca".
"""
