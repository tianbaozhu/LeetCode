class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # time complexity O(n)
        # space complexity O(n)
        stack = []

        for ch in s:
            if len(stack) == 0 or stack[-1][0] != ch:
                stack.append([ch, 1])
            else:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()

        return "".join([x[0]*x[1] for x in stack])

"""
Input: s = "abcd", k = 2
Output: "abcd"
Explanation: There's nothing to delete.

Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation:
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"

Input: s = "pbbcggttciiippooaais", k = 2
Output: "ps"
"""
