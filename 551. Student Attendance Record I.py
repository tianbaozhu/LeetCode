class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # time complexity O(n)
        # space complexity O(1)
        count_a = 0
        count_l = 0
        for ch in s:
            if ch == "A":
                count_a += 1
                count_l = 0
            elif ch == "L":
                count_l += 1
            else:
                count_l = 0
            if count_a == 2 or count_l == 3:
                return False
        return True
