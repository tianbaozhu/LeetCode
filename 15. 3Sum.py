class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []

        nums.sort()
        ret = []
        for i in range(len(nums)-2):
            if nums[i] > 0:
                break
            if i != 0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = len(nums)-1
            while left < right:
                total = nums[i]+nums[left]+nums[right]
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    ret.append([nums[left], nums[i], nums[right]])
                    while left < right and nums[left+1] == nums[left]:
                        left += 1
                    while left < right and nums[right-1] == nums[right]:
                        right -= 1
                    left += 1
                    right -= 1
        return ret

"""
Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
