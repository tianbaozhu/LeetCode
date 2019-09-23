class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)-1
        left_max = 0
        right_max = 0
        ret = 0
        while left < right:
            if height[left] < height[right]:
                left_max = max(left_max, height[left])
                ret += max(left_max - height[left], 0)
                left += 1
            else:
                right_max = max(right_max, height[right])
                ret += max(right_max - height[right], 0)
                right -= 1
        return ret

"""
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""
