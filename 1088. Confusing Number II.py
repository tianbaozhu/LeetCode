class Solution(object):
    def confusingNumber(self, num):
        dic = {0:0,1:1,6:9,8:8,9:6}
        new = 0
        temp = num
        while temp > 0:
            digit = temp % 10
            temp = temp // 10
            new = 10*new + dic[digit]
        return new != num

    def confusingNumberII(self, N):
        """
        :type N: int
        :rtype: int
        """
        self.ret = 0
        self.nums = [0,1,6,8,9]
        
        def dfs(curr, length, target, string):
            if self.confusingNumber(curr) and curr <= target:
                self.ret += 1
            if length == len(string):
                return
            for num in self.nums:
                dfs(curr*10+num, length+1, target, string)
        for num in self.nums[1:]:
            dfs(num, 1, N, str(N))

        return self.ret
