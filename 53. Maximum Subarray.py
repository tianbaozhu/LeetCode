class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Greedy
        if len(nums) == 0:
            return 0
        total = nums[0]
        ret = nums[0]
        for i in range(1, len(nums)):
            if total < 0:
                total = nums[i]
            else:
                total += nums[i]
            ret = max(ret, total)
        return ret

    def maxSubArray1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # DP
        if len(nums) == 0:
            return 0

        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]

        ret = nums[0]
        for i in range(1, len(nums)):
            if dp[i-1] <= 0:
                dp[i] = nums[i]
            else:
                dp[i] = nums[i] + dp[i-1]
            ret = max(ret, dp[i])
        return max(ret, dp[-1])

"""
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:

If you have figured out the O(n) solution,
try coding another solution using the
divide and conquer approach, which is more subtle.
"""
