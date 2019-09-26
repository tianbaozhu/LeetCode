class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        product = 1
        ret = [1 for i in range(len(nums))]

        for i in range(len(nums)-1):
            product *= nums[i]
            ret[i+1] *= product

        product = 1
        for i in range(len(nums)-1, 0, -1):
            product *= nums[i]
            ret[i-1] *= product

        return ret
        
"""
Input:  [1,2,3,4]
Output: [24,12,8,6]
"""
