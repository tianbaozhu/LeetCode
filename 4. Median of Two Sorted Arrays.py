class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        x = len(nums1)
        y = len(nums2)
        left = 0
        right = x
        while left <= right:
            p1 = (left+right) // 2
            p2 = (x+y+1) // 2 - p1
            max_left_x = float('-inf') if p1 == 0 else nums1[p1-1]
            min_right_x = float('inf') if p1 == x else nums1[p1]
            max_left_y = float('-inf') if p2 == 0 else nums2[p2-1]
            min_right_y = float('inf') if p2 == y else nums2[p2]
            if max_left_x <= min_right_y and max_left_y <= min_right_x:
                if (x+y) % 2 == 0:
                    return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2.0
                else:
                    return max(max_left_x, max_left_y)
            if max_left_x < min_right_y:
                left = p1 + 1
            else:
                right = p1 - 1

"""
nums1 = [1, 3]
nums2 = [2]
The median is 2.0

nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5
"""
