class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0

        dict = {}
        ret = 0
        start = 0

        for i in s:
            dict[i] = 0
        for i in range(len(s)):
            dict[s[i]] += 1
            if dict[s[i]] == 2:
                ret = max(ret, i-start)
                while start < i:
                    dict[s[start]] -= 1
                    if dict[s[start]] == 1:
                        start += 1
                        break
                    start += 1
        return max(ret, len(s)-start)
        
"""
Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
