class Solution(object):
    def confusingNumber(self, N):
        """
        :type N: int
        :rtype: bool
        """
        # time complexity O(log(n)) base 10
        # space complexity O(1)
        dic = {0:0,1:1,6:9,8:8,9:6}
        new = 0
        temp = N
        while temp > 0:
            digit = temp % 10
            temp = temp // 10
            if digit in dic:
                new = 10*new + dic[digit]
            else:
                return False
        return new != N
