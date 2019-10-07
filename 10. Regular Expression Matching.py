class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # time complexity: O(m * n)
        # space complexity: O(m * n)
        dp =[[False for i in range(len(p)+1)] for i in range(len(s)+1)]
        dp[0][0] = True

        for i in range(len(p)):
            if p[i] == "*":
                dp[0][i+1] = dp[0][i-1]

        for i in range(len(s)):
            for j in range(len(p)):
                if p[j] == ".":
                    dp[i+1][j+1] = dp[i][j]
                elif p[j] == "*":
                    if s[i] == p[j-1] or p[j-1] == ".":
                        dp[i+1][j+1] = dp[i+1][j] or dp[i][j] or dp[i+1][j-1] or dp[i][j+1]
                    else:
                        dp[i+1][j+1] = dp[i+1][j-1]
                else:
                    if p[j] == s[i]:
                        dp[i+1][j+1] = dp[i][j]
                    else:
                        dp[i+1][j+1] = False
                        
        return dp[-1][-1]
