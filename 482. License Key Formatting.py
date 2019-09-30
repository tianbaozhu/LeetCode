class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = S.replace("-", "")
        first = len(S) % K
        ret = []
        if first > 0 :
            ret = [S[:first].upper()]
        while first < len(S):
            ret.append(S[first:first+K].upper())
            first += K
        return "-".join(ret)

"""
Input: S = "5F3Z-2e-9-w", K = 4
Output: "5F3Z-2E9W"
Explanation: The string S has been split into two parts, each part has 4 characters.
Note that the two extra dashes are not needed and can be removed.

Input: S = "2-5g-3-J", K = 2
Output: "2-5G-3J"
Explanation: The string S has been split into three parts,
each part has 2 characters except the first part as it
could be shorter as mentioned above.
"""
