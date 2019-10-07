class Solution(object):
    # def singleNonDuplicate(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     # time complexity O(n)
    #     # space complexity O(1)
    #     n = 0
    #     for num in nums:
    #         n = n ^ num
    #     return n

    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # time complexity O(log(n))
        # space complexity O(1)
        if len(nums) == 1 or nums[0] != nums[1]:
            return nums[0]
        if nums[-2] != nums[-1]:
            return nums[-1]

        left = 0
        right = len(nums)-1

        while left <= right:
            mid = (left+right) // 2
            if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
                return nums[mid]
            elif nums[mid-1] == nums[mid] and (mid+1) % 2 == 0:
                left = mid + 1
            elif nums[mid-1] != nums[mid] and (mid+1) % 2 == 1:
                left = mid + 2
            elif nums[mid-1] != nums[mid] and (mid+1) % 2 == 0:
                right = mid - 1
            else:
                right = mid - 2
