class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        # time complexity O(n)
        # space complexity O(n)
        dic = {"0":"0","1":"1","6":"9","8":"8","9":"6"}
        new = []

        for ch in num[::-1]:
            if ch in dic:
                new.append(dic[ch])
            else:
                return False
                
        return "".join(new) == num
