class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # time complexity O(n)
        # space complexity O(n)
        dic = {}
        left_most = {}
        max_length = 0
        ret = float('inf')

        for index in range(len(nums)):
            if nums[index] in dic:
                dic[nums[index]] += 1
            else:
                dic[nums[index]] = 1
                left_most[nums[index]] = index
            if max_length < dic[nums[index]]:
                max_length = dic[nums[index]]
                ret = index-left_most[nums[index]]+1
            elif max_length == dic[nums[index]]:
                ret = min(ret, index-left_most[nums[index]]+1)

        return ret
