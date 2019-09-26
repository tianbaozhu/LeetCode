class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(nums)-1
        left_most = -1
        while left <= right:
            mid = (left+right) // 2
            if nums[mid] == target:
                left_most = mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        left = 0
        right = len(nums)-1
        right_most = -1
        while left <= right:
            mid = (left+right) // 2
            if nums[mid] == target:
                right_most = mid
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return [left_most, right_most]

"""
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""
