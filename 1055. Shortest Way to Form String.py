class Solution(object):
    def shortestWay(self, source, target):
        """
        :type source: str
        :type target: str
        :rtype: int
        """
        # time complexity: O(m * n)
        # space complexity: O(m)
        if len(target) == 0:
            return 0
        dic = collections.defaultdict(list)
        for i in range(len(source)):
            dic[source[i]].append(i)
        ret = 1
        curr = -1
        for i in range(len(target)):
            flag = False
            if target[i] in dic:
                for j in dic[target[i]]:
                    if j > curr:
                        flag = True
                        curr = j
                        break
            else:
                return -1
            if flag == False:
                ret += 1
                curr = dic[target[i]][0]
        return ret

    def shortestWay1(self, source, target):
        """
        :type source: str
        :type target: str
        :rtype: int
        """
        # time complexity: O(n)
        # space complexity: O(m)
        if len(target) == 0:
            return 0
        dic = {}
        for i in range(len(source)):
            if source[i] in dic:
                for j in range(i,-1,-1):
                    if dic[source[i]][j] == float('-inf'):
                        dic[source[i]][j] = i
                    else:
                        break
            else:
                dic[source[i]] = [i for x in range(i+1)]+[float('-inf') for x in range(i+1, len(source))]
        ret = 1
        curr = 0
        print(dic)
        for i in range(len(target)):
            flag = False
            if target[i] in dic:
                curr = dic[target[i]][curr]+1
            else:
                return -1
            if curr == len(source) and i != len(target)-1:
                ret += 1
                curr = 0
            elif curr == float('-inf'):
                ret += 1
                curr = dic[target[i]][0]+1
        return ret

"""
Input: source = "abc", target = "abcbc"
Output: 2
Explanation: The target "abcbc" can be formed by "abc" and "bc", which are subsequences of source "abc".

Input: source = "abc", target = "acdbc"
Output: -1
Explanation: The target string cannot be constructed from the subsequences of source string
due to the character "d" in target string.

Input: source = "xyz", target = "xzyxz"
Output: 3
Explanation: The target string can be constructed as follows "xz" + "y" + "xz".
"""
