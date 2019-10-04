class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # time complexity O(n)
        # space complexity O(1)
        index = 0
        while index < len(nums):
            if nums[index] < 0 or nums[index] >= len(nums):
                index += 1
            elif nums[nums[index]-1] == nums[index]:
                index += 1
            else:
                nums[nums[index]-1], nums[index] = nums[index], nums[nums[index]-1]

        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1

        return len(nums)+1

"""
Input: [1,2,0]
Output: 3

Input: [3,4,-1,1]
Output: 2

Input: [7,8,9,11,12]
Output: 1
"""
