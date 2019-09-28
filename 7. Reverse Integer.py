class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ret = 0
        flag = True
        if x < 0:
            flag = False
            x = -1*x
        while x > 0:
            ret = ret * 10
            ret += x % 10
            if ret >= 2**31 or ret < -2**31:
                return 0
            x = x // 10

        return ret if flag else -1*ret
        
"""
Input: 123
Output: 321

Input: -123
Output: -321

Input: 120
Output: 21
"""
