class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # time complexity O(n)
        # space complexity O(n)
        stack = []

        for ch in s:
            if ch != "]":
                stack.append(ch)
            else:
                temp = ""
                num = ""
                while stack[-1] != "[":
                    temp = stack.pop() + temp
                stack.pop()
                while len(stack) > 0 and stack[-1].isdigit():
                    num = stack.pop() + num
                stack.append(int(num)*temp)

        return "".join(stack)
