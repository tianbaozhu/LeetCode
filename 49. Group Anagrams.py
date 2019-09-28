class Solution(object):
    def groupAnagrams1(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # sort, O(N*KlogK)
        dict = collections.defaultdict(list)
        ret = []
        for string in strs:
            temp = "".join(sorted(string))
            dict[temp].append(string)
        for key in dict:
            ret.append(dict[key])
        return ret

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # count, O(NK)
        dict = collections.defaultdict(list)
        ret = []
        for string in strs:
            temp = [0 for i in range(26)]
            for ch in string:
                temp[ord(ch)-ord('a')] += 1
            dict[tuple(temp)].append(string)
        for key in dict:
            ret.append(dict[key])
        return ret

"""
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
"""
