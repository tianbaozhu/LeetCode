class Solution(object):
    class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # O(n)
        ret = ""
        min_length = len(s)+1
        dict = {}
        for ch in t:
            if ch in dict:
                dict[ch] += 1
            else:
                dict[ch] = 1
        count = len(t)
        left = right = 0
        while right < len(s):
            if s[right] in dict:
                if dict[s[right]] > 0:
                    count -= 1
                dict[s[right]] -= 1
            right += 1
            while count == 0:
                if right-left < min_length:
                    min_length = right-left
                    ret = s[left:right]
                if s[left] in dict:
                    dict[s[left]] += 1
                    if dict[s[left]] > 0:
                        count += 1
                left += 1
        return ret

    def minWindow1(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # O(n^2)
        ret = ""
        min_length = len(s)+1
        for i in range(len(s)):
            dict = {}
            for ch in t:
                if ch in dict:
                    dict[ch] += 1
                else:
                    dict[ch] = 1
            for j in range(i, len(s)):
                if s[j] in dict:
                    dict[s[j]] -= 1
                    if dict[s[j]] == 0:
                        del dict[s[j]]
                if len(dict) == 0:
                    if min_length > j - i + 1:
                        min_length = j - i + 1
                        ret = s[i:j+1]
        return ret
