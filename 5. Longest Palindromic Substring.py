class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ret = ""
        maxL = 0
        for i in range(len(s)):
            temp = 1
            left = i-1
            right = i+1
            while left >= 0 and s[left] == s[i]:
                left -= 1
                temp += 1
            while right < len(s) and s[right] == s[i]:
                right += 1
                temp += 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                temp += 2
                left -= 1
                right += 1
            if temp > maxL:
                maxL = temp
                ret = s[left+1:right]
        return ret

"""
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Input: "cbbd"
Output: "bb
"""
