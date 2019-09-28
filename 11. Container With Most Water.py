class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)-1
        ret = 0
        while left < right:
            ret = max(ret, (right-left)*min(height[left],height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return ret
        
"""
Input: [1,8,6,2,5,4,8,3,7]
Output: 49
"""
