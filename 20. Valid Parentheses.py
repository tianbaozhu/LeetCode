class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for item in s:
            if item == '(' or item == '[' or item == '{':
                stack.append(item)
            elif item == ')' or item == ']' or item == '}':
                if len(stack) > 0:
                    temp = stack.pop()
                    if item == ')' and temp != '(':
                        return False
                    elif item == ']' and temp != '[':
                        return False
                    elif item == '}' and temp != '{':
                        return False
                else:
                    return False
            else:
                return False

        return len(stack) == 0

"""
Input: "()"
Output: true

Input: "()[]{}"
Output: true

Input: "(]"
Output: false

Input: "([)]"
Output: false

Input: "{[]}"
Output: true
"""
