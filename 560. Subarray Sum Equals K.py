class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dict = {k:1}
        curr = 0
        ret = 0
        for i in range(len(nums)):
            curr += nums[i]
            if curr in dict:
                ret += dict[curr]
            # curr - prev = k
            if k+curr in dict:
                dict[k+curr] += 1
            else:
                dict[k+curr] = 1

        return ret

"""
Input:nums = [1,1,1], k = 2
Output: 2
"""
